# project1
import requests
import json
import  jsonpath

url = 'http://api.k780.com/'
p = {
  'app' : 'finance.rate',
  'scur' : 'USD',
  'tcur' : 'CNY',
  'appkey' : '',
  'sign' : '',
  'format' : 'json',
}
response = requests.get(url, params=p)
j = json.loads(response.text)
rate = jsonpath.jsonpath(j,"$.result.rate")[0]
if rate:
	print("汇率为:",rate)
else:
	print("获取汇率失败，接口返回{}".format(response.test))
rate = float(rate)

def send_wehook(content):
	url = ""

	content = {
		"content": content
	}
	r = requests.post(url, json=content)

a = float(input("请输入footlocker价格:"))
discount = float(input("请输入footlocker折扣:"))
trans_fee = float(input("请输入一双球鞋的运费:"))
b = float(input("请输入该球鞋的最低现货价:"))
du_fee = float(input("请输入你的毒手续费率"))

total_profit = b*(1-du_fee*0.01)-a*rate*discount*0.1-trans_fee

if total_profit > 200:
	send_wehook("coook:{0}".format(total_profit))
elif total_profit > 100:
	send_wehook("搬砖:{0}".format(total_profit))
elif total_profit <= 100:
	send_wehook("有钱冲:{0}".format(total_profit))
