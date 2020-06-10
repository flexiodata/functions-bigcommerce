
# ---
# name: bigcommerce-orders
# deployed: true
# config: index
# title: BigCommerce Orders
# description: Returns a list of orders for a BigCommerce Store
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
#     description: The id of the order
#   - name: customer_id
#     type: integer
#     description: The customer id associated with the order
#   - name: billing_address_first_name
#     type: string
#     description: The first name of the person on the billing address
#   - name: billing_address_last_name
#     type: string
#     description: The last name of the person on the billing address
#   - name: billing_address_company
#     type: string
#     description: The company on the billing address
#   - name: billing_address_street_1
#     type: string
#     description: The first part of the street address for the billing address
#   - name: billing_address_street_2
#     type: string
#     description: The second part of the street address for the billing address
#   - name: billing_address_city
#     type: string
#     description: The city part of the street address for the billing address
#   - name: billing_address_state
#     type: string
#     description: The state part of the street address for the billing address
#   - name: billing_address_zip
#     type: string
#     description: The zip part of the street address for the billing address
#   - name: billing_address_country
#     type: string
#     description: The country part of the street address for the billing address
#   - name: billing_address_country_iso2
#     type: string
#     description: The country part, in ISO2 format, of the street address for the billing address
#   - name: billing_address_phone
#     type: string
#     description: The phone number associated with the billing address
#   - name: billing_address_email
#     type: string
#     description: The email associated with the billing address
#   - name: order_source
#     type: string
#     description: The source of the order
#   - name: date_created
#     type: string
#     description: The date the order was created
#   - name: date_modified
#     type: string
#     description: The date the order was last modified
#   - name: date_shipped
#     type: string
#     description: The date the order was shipped
#   - name: cart_id
#     type: integer
#     description: The cart id associated with the order
#   - name: status_id
#     type: integer
#     description: The status id of the order
#   - name: status
#     type: string
#     description: The status of the order
#   - name: is_deleted
#     type: boolean
#     description: Indicates whether the order was deleted
#   - name: order_is_digital
#     type: boolean
#     description: Whether this is an order for digital products
#   - name: items_total
#     type: integer
#     description: The total number of items in the order
#   - name: items_shipped
#     type: integer
#     description: The number of items that have been shipped
#   - name: payment_method
#     type: string
#     description: The payment method for this order
#   - name: payment_status
#     type: string
#     description: The status of the payment for this order
#   - name: staff_notes
#     type: string
#     description: Any additional notes for staff
#   - name: customer_message
#     type: string
#     description: Message that the customer entered in the Order Comments box during checkout
#   - name: subtotal_ex_tax
#     type: number
#     description: Override value for subtotal excluding tax
#   - name: subtotal_inc_tax
#     type: number
#     description: Override value for subtotal including tax
#   - name: subtotal_tax
#     type: number
#     description: Override value for tax
#   - name: base_shipping_cost
#     type: number
#     description: The value of the base shipping cost
#   - name: shipping_cost_ex_tax
#     type: number
#     description: The value of shipping cost, excluding tax
#   - name: shipping_cost_inc_tax
#     type: number
#     description: The value of shipping cost, including tax
#   - name: shipping_cost_tax
#     type: number
#     description: The tax part of the value of the shipping cost
#   - name: shipping_cost_tax_class_id
#     type: integer
#     description: The shipping cost tax class id
#   - name: base_handling_cost
#     type: number
#     description: The value of the base handling cost
#   - name: handling_cost_ex_tax
#     type: number
#     description: The value of the handling cost, excluding tax
#   - name: handling_cost_inc_tax
#     type: number
#     description: The value of the handling cost, including tax
#   - name: handling_cost_tax
#     type: number
#     description: The tax part of the value of the handling cost
#   - name: handling_cost_tax_class_id
#     type: integer
#     description: The handling cost tax class id
#   - name: base_wrapping_cost
#     type: number
#     description: The value of the base wrapping cost.
#   - name: wrapping_cost_ex_tax
#     type: number
#     description: The value of the wrapping cost, excluding tax
#   - name: wrapping_cost_inc_tax
#     type: number
#     description: The value of the wrapping cost, including tax
#   - name: wrapping_cost_tax
#     type: number
#     description: The tax part of the value of the wrapping cost
#   - name: wrapping_cost_tax_class_id
#     type: integer
#     description: The wrapping cost tax class id
#   - name: total_ex_tax
#     type: number
#     description: Override value for the total, excluding tax
#   - name: total_inc_tax
#     type: number
#     description: Override value for the total, including tax
#   - name: total_tax
#     type: number
#     description: The tax part of the value of the total cost
#   - name: discount_amount
#     type: number
#     description: The discount amount associated with this order
#   - name: gift_certificate_amount
#     type: number
#     description: The gift certificate amount associated with this order
#   - name: coupon_discount
#     type: number
#     description: The coupon amount associated with this order
#   - name: store_credit_amount
#     type: number
#     description: The store credit that the shopper has redeemed on this order
#   - name: refunded_amount
#     type: number
#     description: The amount refunded from this transaction
#   - name: ip_address
#     type: string
#     description: The IP Address of the customer, if known
#   - name: geoip_country
#     type: string
#     description: The full name of the country where the customer made the purchase, based on the IP
#   - name: geoip_country_iso2
#     type: string
#     description: The country where the customer made the purchase, in ISO2 format, based on the IP
#   - name: default_currency_code
#     type: string
#     description: The currency code of the default currency for this type of transaction
#   - name: currency_code
#     type: string
#     description: The currency code of the currency being used in the order
#   - name: currency_exchange_rate
#     type: number
#     description: The currency exchange rate associated with the order
# examples:
#   - '"*"'
#   - '"id, customer_id, date_created, status"'
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
    for data in get_data(flex.vars):
        flex.output.write(data)

def get_data(params):

    # get the api key from the variable input
    store_hash = dict(params).get('bigcommerce_store_hash')
    client_id = dict(params).get('bigcommerce_client_id')
    access_token = dict(params).get('bigcommerce_access_token')

    # example store:
    # https://bigcommerce.github.io/storefront-api-examples/html-bootstrap-vanillajs/
    # https://buybutton.store/shop-all/

    # orders api:
    # https://developer.bigcommerce.com/api-reference/store-management/orders/orders/getallorders

    headers = {
        'X-Auth-Client': client_id,
        'X-Auth-Token': access_token,
        'Accept': 'application/json'
    }
    url = 'https://api.bigcommerce.com/stores/' + store_hash + '/v2/orders'

    # note: documentation doesn't seem to indicate any paginator mechanism for orders
    page_url = url

    response = requests_retry_session().get(page_url, headers=headers)
    response.raise_for_status()
    content = response.json()

    data = content # top-level is array
    for item in data:
        item = get_item_info(item)
        buffer = json.dumps(item, default=to_string) + "\n"
        yield buffer

def requests_retry_session(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(429, 500, 502, 503, 504),
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

def to_date(value):
    # TODO: convert if needed
    return value

def to_number(value):
    try:
        v = value
        return float(v)
    except ValueError:
        return value

def to_string(value):
    if isinstance(value, (date, datetime)):
        return value.isoformat()
    if isinstance(value, (Decimal)):
        return str(value)
    return value

def get_item_info(item):

    info = OrderedDict()

    info['id'] = item.get('id')
    info['customer_id'] = item.get('customer_id')
    info['billing_address_first_name'] = (item.get('billing_address') or {}).get('first_name')
    info['billing_address_last_name'] = (item.get('billing_address') or {}).get('last_name')
    info['billing_address_company'] = (item.get('billing_address') or {}).get('company')
    info['billing_address_street_1'] = (item.get('billing_address') or {}).get('street_1')
    info['billing_address_street_2'] = (item.get('billing_address') or {}).get('street_2')
    info['billing_address_city'] = (item.get('billing_address') or {}).get('city')
    info['billing_address_state'] = (item.get('billing_address') or {}).get('state')
    info['billing_address_zip'] = (item.get('billing_address') or {}).get('zip')
    info['billing_address_country'] = (item.get('billing_address') or {}).get('country')
    info['billing_address_country_iso2'] = (item.get('billing_address') or {}).get('country_iso2')
    info['billing_address_phone'] = (item.get('billing_address') or {}).get('phone')
    info['billing_address_email'] = (item.get('billing_address') or {}).get('email')
    info['order_source'] = item.get('order_source')
    info['date_created'] = to_date(item.get('date_created'))
    info['date_modified'] = to_date(item.get('date_modified'))
    info['date_shipped'] = to_date(item.get('date_shipped'))
    info['cart_id'] = item.get('cart_id')
    info['status_id'] = item.get('status_id')
    info['status'] = item.get('status')
    info['is_deleted'] = item.get('is_deleted')
    info['order_is_digital'] = item.get('order_is_digital')
    info['items_total'] = item.get('items_total')
    info['items_shipped'] = item.get('items_shipped')
    info['payment_method'] = item.get('payment_method')
    info['payment_status'] = item.get('payment_status')
    info['staff_notes'] = item.get('staff_notes')
    info['customer_message'] = item.get('customer_message')
    info['subtotal_ex_tax'] = to_number(item.get('subtotal_ex_tax'))
    info['subtotal_inc_tax'] = to_number(item.get('subtotal_inc_tax'))
    info['subtotal_tax'] = to_number(item.get('subtotal_tax'))
    info['base_shipping_cost'] = to_number(item.get('base_shipping_cost'))
    info['shipping_cost_ex_tax'] = to_number(item.get('shipping_cost_ex_tax'))
    info['shipping_cost_inc_tax'] = to_number(item.get('shipping_cost_inc_tax'))
    info['shipping_cost_tax'] = to_number(item.get('shipping_cost_tax'))
    info['shipping_cost_tax_class_id'] = item.get('shipping_cost_tax_class_id')
    info['base_handling_cost'] = to_number(item.get('base_handling_cost'))
    info['handling_cost_ex_tax'] = to_number(item.get('handling_cost_ex_tax'))
    info['handling_cost_inc_tax'] = to_number(item.get('handling_cost_inc_tax'))
    info['handling_cost_tax'] = to_number(item.get('handling_cost_tax'))
    info['handling_cost_tax_class_id'] = item.get('handling_cost_tax_class_id')
    info['base_wrapping_cost'] = to_number(item.get('base_wrapping_cost'))
    info['wrapping_cost_ex_tax'] = to_number(item.get('wrapping_cost_ex_tax'))
    info['wrapping_cost_inc_tax'] = to_number(item.get('wrapping_cost_inc_tax'))
    info['wrapping_cost_tax'] = to_number(item.get('wrapping_cost_tax'))
    info['wrapping_cost_tax_class_id'] = item.get('wrapping_cost_tax_class_id')
    info['total_ex_tax'] = to_number(item.get('total_ex_tax'))
    info['total_inc_tax'] = to_number(item.get('total_inc_tax'))
    info['total_tax'] = to_number(item.get('total_tax'))
    info['discount_amount'] = to_number(item.get('discount_amount'))
    info['gift_certificate_amount'] = to_number(item.get('gift_certificate_amount'))
    info['coupon_discount'] = to_number(item.get('coupon_discount'))
    info['store_credit_amount'] = to_number(item.get('store_credit_amount'))
    info['refunded_amount'] = to_number(item.get('refunded_amount'))
    info['ip_address'] = item.get('ip_address')
    info['geoip_country'] = item.get('geoip_country')
    info['geoip_country_iso2'] = item.get('geoip_country_iso2')
    info['default_currency_code'] = item.get('default_currency_code')
    info['currency_code'] = item.get('currency_code')
    info['currency_exchange_rate'] = to_number(item.get('currency_exchange_rate'))

    return info
