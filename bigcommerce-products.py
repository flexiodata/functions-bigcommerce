
# ---
# name: bigcommerce-products
# deployed: true
# config: index
# title: BigCommerce Products
# description: Returns a list of products from a BigCommerce Store
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
#     description: ID of the product
#   - name: name
#     type: string
#     description: The product name
#   - name: type
#     type: string
#     description: The product type
#   - name: sku
#     type: string
#     description: User defined product code/stock keeping unit (SKU)
#   - name: description
#     type: string
#     description: The product description, which can include HTML formatting
#   - name: weight
#     type: numeric
#     description: Weight of the product, which can be used when calculating shipping costs
#   - name: width
#     type: numeric
#     description: Width of the product, which can be used when calculating shipping costs
#   - name: depth
#     type: numeric
#     description: Depth of the product, which can be used when calculating shipping costs
#   - name: height
#     type: numeric
#     description: Height of the product, which can be used when calculating shipping costs
#   - name: price
#     type: numeric
#     description: The price of the product
#   - name: cost_price
#     type: numeric
#     description: The cost price of the product
#   - name: retail_price
#     type: numeric
#     description: The retail cost of the product
#   - name: sale_price
#     type: numeric
#     description: If entered, the sale price will be used instead of value in the price field when calculating the product’s cost
#   - name: map_price
#     type: numeric
#     description: Minimum advertised price
#   - name: calculated_price
#     type: numeric
#     description: The price of the product as seen on the storefront
#   - name: tax_class_id
#     type: integer
#     description: The ID of the tax class applied to the product
#   - name: product_tax_code
#     type: string
#     description: AvaTax System tax codes
#   - name: categories
#     type: string
#     description: An comma-delimited list of IDs for the categories to which this product belongs
#   - name: brand_id
#     type: integer
#     description: The brand id
#   - name: option_set_id
#     type: integer
#     description: Indicates that the product is in an Option Set (legacy V2 concept)
#   - name: option_set_display
#     type: string
#     description: Legacy template setting which controls if the option set shows up to the side of or below the product image and description
#   - name: inventory_level
#     type: integer
#     description: Current inventory level of the product
#   - name: inventory_warning_level
#     type: integer
#     description: Inventory warning level for the product
#   - name: inventory_tracking
#     type: string
#     description: The type of inventory tracking for the product
#   - name: reviews_rating_sum
#     type: integer
#     description: The total rating for the product
#   - name: reviews_count
#     type: integer
#     description: The number of times the product has been rated
#   - name: view_count
#     type: integer
#     description: The number of times the product has been viewed
#   - name: total_sold
#     type: integer
#     description: The total quantity of this product sold
#   - name: fixed_cost_shipping_price
#     type: numeric
#     description: A fixed shipping cost for the product
#   - name: is_free_shipping
#     type: boolean
#     description: Flag used to indicate whether the product has free shipping
#   - name: is_visible
#     type: boolean
#     description: Flag to determine whether the product should be displayed to customers browsing the store
#   - name: is_featured
#     type: boolean
#     description: Flag to determine whether the product should be included in the featured products panel when viewing the store
#   - name: related_products
#     type: string
#     description: An comma-delimited list of IDs for the related products
#   - name: warranty
#     type: string
#     description: Warranty information displayed on the product page
#   - name: bin_picking_number
#     type: string
#     description: The BIN picking number for the product
#   - name: layout_file
#     type: string
#     description: The layout template file used to render this product category
#   - name: upc
#     type: string
#     description: The product UPC code, which is used in feeds for shopping comparison sites and external channel integrations
#   - name: mpn
#     type: string
#     description: Manufacturer Part Numbe
#   - name: gtin
#     type: string
#     description: Global Trade Item Numbe
#   - name: search_keywords
#     type: string
#     description: A comma-separated list of keywords that can be used to locate the product when searching the store
#   - name: availability
#     type: string
#     description: Availability of the product
#   - name: availability_description
#     type: string
#     description: Availability text displayed on the checkout page, under the product title
#   - name: gift_wrapping_options_type
#     type: string
#     description: Type of gift-wrapping options
#   - name: gift_wrapping_options_list
#     type: string
#     description: A comma-delimited list of gift-wrapping option IDs
#   - name: sort_order
#     type: integer
#     description: Priority to give this product when included in product lists on category pages and in search results
#   - name: condition
#     type: string
#     description: The product condition
#   - name: is_condition_shown
#     type: boolean
#     description: Flag used to determine whether the product condition is shown to the customer on the product page
#   - name: order_quantity_minimum
#     type: integer
#     description: The minimum quantity an order must contain, to be eligible to purchase this product
#   - name: order_quantity_maximum
#     type: integer
#     description: The maximum quantity an order can contain when purchasing the product
#   - name: page_title
#     type: string
#     description: Custom title for the product page
#   - name: meta_keywords
#     type: string
#     description: A comma-delimited list of custom meta keywords for the product page
#   - name: meta_description
#     type: string
#     description: Custom meta description for the product page
#   - name: preorder_release_date
#     type: string
#     description: Pre-order release date
#   - name: preorder_message
#     type: string
#     description: Custom expected-date message to display on the product page
#   - name: is_preorder_only
#     type: boolean
#     description: If set to true then on the preorder release date the preorder status will automatically be removed
#   - name: is_price_hidden
#     type: boolean
#     description: False by default, indicating that this product’s price should be shown on the product page
#   - name: price_hidden_label
#     type: string
#     description: If is_price_hidden is true, the value of price_hidden_label is displayed instead of the price
#   - name: url
#     type: string
#     description: Category URL on the storefront
#   - name: custom_url
#     type: string
#     description: The custom URL for the category on the storefront
#   - name: base_variant_id
#     type: integer
#     description: The unique identifier of the base variant associated with a simple product
#   - name: open_graph_type
#     type: string
#     description: Type of product, defaults to product
#   - name: open_graph_title
#     type: string
#     description: Title of the product, if not specified the product name will be used instead
#   - name: open_graph_description
#     type: string
#     description: Description to use for the product, if not specified then the meta_description will be used instead
#   - name: open_graph_use_meta_description
#     type: boolean
#     description: Flag to determine if product description or open graph description is used
#   - name: open_graph_use_product_name
#     type: boolean
#     description: Flag to determine if product name or open graph name is used
#   - name: open_graph_use_image
#     type: boolean
#     description: Flag to determine if product image or open graph image is used
#   - name: date_created
#     type: string
#     description: The date on which the product was created
#   - name: date_modified
#     type: string
#     description: The date on which the product was modified
# examples:
#   - '"*"'
#   - '"id, name, sku, description, price"'
#   - '"", "coffeemaker"'
#   - '"id, sku, search_keywords, meta_keywords", "search_keywords:jar"'
# ---

import json
import requests
from collections import OrderedDict

# main function entry point
def flexio_handler(flex):

    # get the api key from the variable input
    store_hash = dict(flex.vars).get('bigcommerce_store_hash')
    client_id = dict(flex.vars).get('bigcommerce_client_id')
    access_token = dict(flex.vars).get('bigcommerce_access_token')

    # example store:
    # https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/
    # https://buybutton.store/shop-all/

    # products api:
    # https://api.bigcommerce.com/stores/z1koq2uxgr/v3/catalog/products

    url = 'https://api.bigcommerce.com/stores/' + store_hash + '/v3/catalog/products'
    headers = {
        'X-Auth-Client': client_id,
        'X-Auth-Token': access_token
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    content = response.json()

    # build up the result
    result = []

    products = content.get('data')
    for item in products:
        result.append(getProductInfo(item))

    result = json.dumps(result, default=to_string)
    flex.output.content_type = "application/json"
    flex.output.write(result)

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def getProductInfo(item):

    info = OrderedDict()

    info['id'] = item.get('id')
    info['name'] = item.get('name')
    info['type'] = item.get('type')
    info['sku'] = item.get('sku')
    info['description'] = item.get('description')
    info['weight'] = item.get('weight')
    info['width'] = item.get('width')
    info['depth'] = item.get('depth')
    info['height'] = item.get('height')
    info['price'] = item.get('price')
    info['cost_price'] = item.get('cost_price')
    info['retail_price'] = item.get('retail_price')
    info['sale_price'] = item.get('sale_price')
    info['map_price'] = item.get('map_price')
    info['calculated_price'] = item.get('calculated_price')
    info['tax_class_id'] = item.get('tax_class_id')
    info['product_tax_code'] = item.get('product_tax_code')
    info['categories'] = ', '.join([str(i) for i in item.get('categories',[])]) # convert to comma-delimited string
    info['brand_id'] = item.get('brand_id')
    info['option_set_id'] = item.get('option_set_id')
    info['option_set_display'] = item.get('option_set_display')
    info['inventory_level'] = item.get('inventory_level')
    info['inventory_warning_level'] = item.get('inventory_warning_level')
    info['inventory_tracking'] = item.get('inventory_tracking')
    info['reviews_rating_sum'] = item.get('reviews_rating_sum')
    info['reviews_count'] = item.get('reviews_count')
    info['view_count'] = item.get('view_count')
    info['total_sold'] = item.get('total_sold')
    info['fixed_cost_shipping_price'] = item.get('fixed_cost_shipping_price')
    info['is_free_shipping'] = item.get('is_free_shipping')
    info['is_visible'] = item.get('is_visible')
    info['is_featured'] = item.get('is_featured')
    info['related_products'] = ', '.join([str(i) for i in item.get('related_products',[])]) # convert to comma-delimited string
    info['warranty'] = item.get('warranty')
    info['bin_picking_number'] = item.get('bin_picking_number')
    info['layout_file'] = item.get('layout_file')
    info['upc'] = item.get('upc')
    info['mpn'] = item.get('mpn')
    info['gtin'] = item.get('gtin')
    info['search_keywords'] = item.get('search_keywords')
    info['availability'] = item.get('availability')
    info['availability_description'] = item.get('availability_description')
    info['gift_wrapping_options_type'] = item.get('gift_wrapping_options_type')
    info['gift_wrapping_options_list'] = ', '.join([str(i) for i in item.get('gift_wrapping_options_list',[])]) # convert to comma-delimited string
    info['sort_order'] = item.get('sort_order')
    info['condition'] = item.get('condition')
    info['is_condition_shown'] = item.get('is_condition_shown')
    info['order_quantity_minimum'] = item.get('order_quantity_minimum')
    info['order_quantity_maximum'] = item.get('order_quantity_maximum')
    info['page_title'] = item.get('page_title')
    info['meta_keywords'] = ', '.join([i for i in item.get('meta_keywords',[])]) # convert to comma-delimited string
    info['meta_description'] = item.get('meta_description')
    info['preorder_release_date'] = item.get('preorder_release_date')
    info['preorder_message'] = item.get('preorder_message')
    info['is_preorder_only'] = item.get('is_preorder_only')
    info['is_price_hidden'] = item.get('is_price_hidden')
    info['price_hidden_label'] = item.get('price_hidden_label')
    info['url'] = item.get('url')
    info['custom_url'] = item.get('custom_url',{}).get('url','') # get url part of object
    info['base_variant_id'] = item.get('base_variant_id')
    info['open_graph_type'] = item.get('open_graph_type')
    info['open_graph_title'] = item.get('open_graph_title')
    info['open_graph_description'] = item.get('open_graph_description')
    info['open_graph_use_meta_description'] = item.get('open_graph_use_meta_description')
    info['open_graph_use_product_name'] = item.get('open_graph_use_product_name')
    info['open_graph_use_image'] = item.get('open_graph_use_image')
    info['date_created'] = item.get('date_created')
    info['date_modified'] = item.get('date_modified')

    return info
