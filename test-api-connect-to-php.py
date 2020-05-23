import requests

# response = requests.get('http://localhost/test-api/api.php?id=2&action=connect&time=1')

# print(response)
# print(response.text)

# resp = requests.post('http://localhost/test-api/api.php', {'a': 10})
#
# print(resp)
# print(resp.text)

ip = requests.get('https://ip.activity-monitoring.ir')
print(ip, ip.text)
