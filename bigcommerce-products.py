
# ---
# name: bigcommerce-products
# deployed: true
# title: BigCommerce Products
# description: Returns a list of products from a BigCommerce Store
# params:
#   - name: properties
#     type: array
#     description: The properties to return (defaults to all properties). See "Returns" for a listing of the available properties.
#     required: false
# returns:
#   - name: id
#     type: string
#     description: The id of the product
#   - name: entity_id
#     type: string
#     description: The entity_id of the product
#   - name: name
#     type: string
#     description: The name of the product
#   - name: title
#     type: string
#     description: The name of the product (alias for name currently)
#   - name: sku
#     type: string
#     description: The sku of the product
#   - name: page_url
#     type: string
#     description: The url for the product page
#   - name: description
#     type: string
#     description: A description of the product
#   - name: search_words
#     type: string
#     description: Search words for the product (currently taken from slug)
#   - name: image_url
#     type: string
#     description: The url for the product image
#   - name: price
#     type: string
#     description: The price for the product
#   - name: price_currency
#     type: string
#     description: The price currency for the product price
# examples:
#   - '"entity_id, sku, name, page_url, title, search_words, description"'
#   - '"name, price"'
#   - '"*"'
# ---

import json
import requests
import urllib
import itertools
from datetime import *
from decimal import *
from cerberus import Validator
from collections import OrderedDict
from bs4 import BeautifulSoup

# main function entry point
def flexio_handler(flex):

    # get the api key from the variable input
    store_url = dict(flex.vars).get('bigcommerce_store_url')
    auth_token = dict(flex.vars).get('bigcommerce_api_key')
    if auth_token is None:
        flex.output.content_type = "application/json"
        flex.output.write([[""]])
        return

    # get the input
    input = flex.input.read()
    try:
        input = json.loads(input)
        if not isinstance(input, list): raise ValueError
    except ValueError:
        raise ValueError

    # define the expected parameters and map the values to the parameter names
    # based on the positions of the keys/values
    params = OrderedDict()
    params['properties'] = {'required': False, 'validator': validator_list, 'coerce': to_list, 'default': '*'}
    input = dict(zip(params.keys(), input))

    # validate the mapped input against the validator
    # if the input is valid return an error
    v = Validator(params, allow_unknown = True)
    input = v.validated(input)
    if input is None:
        raise ValueError

    # map this function's property names to the API's property names
    def getDescription(item):
            description = item.get('description','')
            soup = BeautifulSoup(description, 'lxml') # Parse the HTML as a string
            items = soup.find_all(text=True)
            if len(items) == 0:
                return ''
            return items[0]
    def getSearchWords(item):
            path = item.get('path','')
            words = path.split("-")
            keywords = []
            for word in words:
                w = word.strip(' \\/')
                if len(w) >= 3:
                    keywords.append(w)
            keywords.sort()
            return ",".join(keywords)
    property_map = OrderedDict()
    property_map['id'] = lambda item: item.get('id','')
    property_map['entity_id'] = lambda item: item.get('entityId','')
    property_map['name'] = lambda item: item.get('name','')
    property_map['title'] = lambda item: item.get('name','')  # TODO: get the page title rather than the product name
    property_map['sku'] = lambda item: item.get('sku','')
    property_map['page_url'] = lambda item: item.get('path','')
    property_map['description'] = lambda item: getDescription(item)
    property_map['search_words'] = lambda item: getSearchWords(item)
    property_map['image_url'] = lambda item: item.get('defaultImage',{}).get('img640px','')
    property_map['price'] = lambda item: item.get('prices').get('price',{}).get('value','')
    property_map['price_currency'] = lambda item: item.get('prices').get('price',{}).get('currencyCode','')

    try:

        # example store:
        # https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/
        # https://buybutton.store/shop-all/

        url = store_url + '/graphql'
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + auth_token
        }
        columns = list(property_map.values())
        data = { "query": get_product_query() }

        response = requests.post(url, data=json.dumps(data), headers=headers)
        response.raise_for_status()
        content = response.json()

        # get the properties to return and the property map
        properties = [p.lower().strip() for p in input['properties']]

        # if we have a wildcard, get all the properties
        if len(properties) == 1 and properties[0] == '*':
            properties = list(property_map.keys())

        # build up the result
        result = []
        result.append(properties)

        edges = content.get('data',{}).get('site',{}).get('products',{}).get('edges',[])
        for item in edges:
            product = item.get('product',{})
            row = [property_map.get(p, lambda item: '')(product) or '' for p in properties]
            result.append(row)

        flex.output.content_type = "application/json"
        flex.output.write(result)

    except:
        flex.output.content_type = 'application/json'
        flex.output.write([['']])

def validator_list(field, value, error):
    if isinstance(value, str):
        return
    if isinstance(value, list):
        for item in value:
            if not isinstance(item, str):
                error(field, 'Must be a list with only string values')
        return
    error(field, 'Must be a string or a list of strings')

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def to_list(value):
    # if we have a list of strings, create a list from them; if we have
    # a list of lists, flatten it into a single list of strings
    if isinstance(value, str):
        return value.split(",")
    if isinstance(value, list):
        return list(itertools.chain.from_iterable(value))
    return None

def get_product_query():

    return '''
        query Product {
            customer {
            firstName
            lastName
            email
            }
            site {
            products {
                edges {
                product: node {
                    ...ProductFields
                }
                }
            }
            settings {
                storeName
                url {
                vanityUrl
                }
            }
            }
        }
        fragment ProductFields on Product {
            id
            entityId
            name
            sku
            path
            description
            defaultImage {
            img320px: url(width: 320)
            img640px: url(width: 640)
            img960px: url(width: 960)
            img1280px: url(width: 1280)
            altText
            }
            prices {
            price {
                value
                currencyCode
            }
            retailPrice {
                value
                currencyCode
            }
            }
        }
    '''