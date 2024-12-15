import requests

url = "https://lf-douyin-pc-web.douyinstatic.com/obj/douyin-pc-web/ies/douyin_web/route.manifest.1-0-5-9119.json"

payload = {}
headers = {
		"sec-ch-ua-platform": "\"Windows\"",
		"Referer": "https://www.douyin.com/",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0",
		"sec-ch-ua": "\"Microsoft Edge\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
		"sec-ch-ua-mobile": "?0",
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

print(response.text)
with open ('1.json','w') as f:
    f.write(response.text)