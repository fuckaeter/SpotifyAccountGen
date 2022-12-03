import requests
import string
import random
import os
from datetime import datetime
os.system("cls")

colours = ['\u001b[35;1m', '\u001b[32;1m']
num = 2
ls = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0']
print("""\u001b[31;1m
 ██████ ██   ██ ██████   ██████  ███    ██  ██████  ███████ 
██      ██   ██ ██   ██ ██    ██ ████   ██ ██    ██ ██      
██      ███████ ██████  ██    ██ ██ ██  ██ ██    ██ ███████ 
██      ██   ██ ██   ██ ██    ██ ██  ██ ██ ██    ██      ██ 
 ██████ ██   ██ ██   ██  ██████  ██   ████  ██████  ███████                                                         
""")
print("""\u001b[32;1m                 _   _  __                          
 ___ _ __   ___ | |_(_)/ _|_   _    __ _  ___ _ __  
/ __| '_ \ / _ \| __| | |_| | | |  / _` |/ _ \ '_ \ 
\__ \ |_) | (_) | |_| |  _| |_| | | (_| |  __/ | | |
|___/ .__/ \___/ \__|_|_|  \__, |  \__, |\___|_| |_|
    |_|                    |___/   |___/            
"""
)
current_datetime = datetime.now()
time = current_datetime.strftime("%D:%H:%M:%S")
str_current_datetime = str(time)
new = str_current_datetime.replace(" ", "_")
new2 = new.replace(":", "-")
new3 = new2.replace('/', '-')
  
file_name = new3+".txt"

in0 = input("Basic Settings [0] Advanced Settings [1]: ")
in1= input("Input the base name/email of account: ")
in2= input("Input base of password (leave blank if you want it completely randomised): ")
browser = ls[0]
refferal = ''
if in0 == '1':
    in3 = int(input("Input what browser you want to use [1] for chrome, [2] for firefox: "))
    refferal = input("Input a refferer (leave blank if you dont have one): ")
    in3 -=1
    if browser != ' ':
        browser =  ls[in3]
      
f= open(file_name, 'w')
f.write(' ')




while True:
    if (num % 2) == 0:
        colour =  colours[0]
    else:
        colour = colours[1]
    letters = string.ascii_lowercase
    result_str1 = ''.join(random.choice(letters) for i in range(8))
    result_str2 = ''.join(random.choice(letters) for i in range(8))

    email= in1 + result_str1 + '@xitroo.com'
    password= in2 + result_str2 
    name = in1
    headers = {
    'authority': 'spclient.wg.spotify.com',
    'accept': '*/*',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'origin': 'https://www.spotify.com',
    'referer': 'https://www.spotify.com/',
    'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': browser,
    }

    json_data = {
        'account_details': {
            'birthdate': '2000-11-11',
            'consent_flags': {
                'eula_agreed': True,
                'send_email': True,
                'third_party_email': False,
            },
            'display_name': name,
            'email_and_password_identifier': {
                'email': email,
                'password': password,
            },
            'gender': 1,
        },
        'callback_uri': 'https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=uk',
        'client_info': {
            'api_key': 'a1e486e2729f46d6bb368d6b2bcda326',
            'app_version': 'v2',
            'capabilities': [
                1,
            ],
            'installation_id': 'ae34e9d333dceaa91a8eacd8408ce664',
            'platform': 'www',
        },
        'tracking': {
            'creation_flow': '',
            'creation_point': 'https://open.spotify.com/?sp_cid=ae34e9d333dceaa91a8eacd8408ce664&device=desktop',
            'referrer': refferal,
        },
    }

    okur = requests.post('https://spclient.wg.spotify.com/signup/public/v2/account/create', headers=headers, json=json_data)
    num +=1
    if okur.status_code == 200:
        print(colour + 'account created: ' + email + ' ' + ': ' + password)
        with open(file_name, "a") as f1:
            f1.write('email: ' + email + '\n password: ' + password +'\n')
 
    else:
        print("\u001b[31;1mError.")
    
    




