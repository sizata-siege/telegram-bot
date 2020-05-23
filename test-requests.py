import requests

response = requests.get('https://ip.activity-monitoring.ir')

print(response)
ip = response.text
print(ip)
