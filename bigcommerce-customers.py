
# ---
# name: bigcommerce-customers
# deployed: true
# config: index
# title: BigCommerce Customers
# description: Returns a list of customers from a BigCommerce Store
# params:
#   - name: properties
#     type: array
#     description: The properties to return, given as a string or array; defaults to all properties; see "Returns" for available properties
#     required: false
#   - name: filter
#     type: array
#     description: Search query to determine the rows to return, given as a string or array
#     required: false
# returns:
#   - name: id
#     type: integer
#     description: ID of the customer
#   - name: company
#     type: string
#     description: Company of the customer
#   - name: customer_group_id
#     type: integer
#     description: Group ID of the customer
#   - name: email
#     type: string
#     description: Email of the customer
#   - name: first_name
#     type: string
#     description: First name of the customer
#   - name: last_name
#     type: string
#     description: Last name of the customer
#   - name: notes
#     type: string
#     description: Notes for the customer
#   - name: phone
#     type: string
#     description: Phone number of the customer
#   - name: registration_ip_address
#     type: string
#     description: Registration ip address for the customer
#   - name: tax_exempt_category
#     type: string
#     description: Tax exempt category for the customer
#   - name: accepts_product_review_abandoned_cart_emails
#     type: boolean
#     description: Flag field indicating whether or not the customr receives product review abandoned cart emails
#   - name: date_created
#     type: string
#     description: The date on which the customer was created
#   - name: date_modified
#     type: string
#     description: The date on which the customer was modified
# examples:
#   - '"*"'
#   - '"id, email, first_name, last_name"'
#   - '"", "ACME"'
#   - '"id, company, email, first_name, last_name", "company:acme"'
# ---

import json
import urllib
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from collections import OrderedDict

# main function entry point
def flexio_handler(flex):

    flex.output.content_type = 'application/x-ndjson'
    for item in get_data(flex.vars):
        result = json.dumps(item, default=to_string) + "\n"
        flex.output.write(result)

def get_data(params):

    # get the api key from the variable input
    store_hash = dict(params).get('bigcommerce_store_hash')
    client_id = dict(params).get('bigcommerce_client_id')
    access_token = dict(params).get('bigcommerce_access_token')

    # example store:
    # https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/
    # https://buybutton.store/shop-all/

    # customer api:
    # https://developer.bigcommerce.com/api-reference/store-management/customers-v3/customers/customersget

    headers = {
        'X-Auth-Client': client_id,
        'X-Auth-Token': access_token
    }
    url = 'https://api.bigcommerce.com/stores/' + store_hash + '/v3/customers'

    page_size = 250
    page_idx = 1
    while True:

        url_query_params = {'limit': page_size, 'page': page_idx}
        url_query_str = urllib.parse.urlencode(url_query_params)

        page_url = url + '?' + url_query_str
        response = requests_retry_session().get(page_url, headers=headers)
        response.raise_for_status()
        content = response.json()

        data = content.get('data')
        if len(data) == 0:
            break

        for item in data:
            yield get_item_info(item)

        page_idx = page_idx + 1

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def get_item_info(item):

    info = OrderedDict()

    info['id'] = item.get('id')
    info['company'] = item.get('company')
    info['customer_group_id'] = item.get('customer_group_id')
    info['email'] = item.get('email')
    info['first_name'] = item.get('first_name')
    info['last_name'] = item.get('last_name')
    info['notes'] = item.get('notes')
    info['phone'] = item.get('phone')
    info['registration_ip_address'] = item.get('registration_ip_address')
    info['tax_exempt_category'] = item.get('tax_exempt_category')
    info['accepts_product_review_abandoned_cart_emails'] = item.get('accepts_product_review_abandoned_cart_emails')
    info['date_created'] = item.get('date_created')
    info['date_modified'] = item.get('date_modified')

    return info
