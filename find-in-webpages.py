import requests
import re


def find_title(url):
    resp = requests.get(url)
    title = re.findall("<title>[a-zA-Z0-9.]+</title>", resp.text)
    title = title[0]
    return title[7:-8]


def find_emails(url):
    resp = requests.get(url)
    email_list = re.findall("[a-zA-Z0-9.]+@[a-zA-Z]+.[a-zA-Z]+", resp.text)
    return email_list


def find_phone_numbers(url):
    resp = requests.get(url)
    phone_number_list = re.findall("'+'", resp.text)
    return phone_number_list

def jetBrains():
    for i in range(500, 5000):
        resp = requests.get('https://jb.gg/' + str(i))
        print('https://jb.gg/' + str(i))
        print(resp.text)


def main():
    while True:
        url = input("Please enter the url or address of web page:")
        action = input("m > emails || t > title || n > phone numbers\nChoose an option : ")
        if 'http' not in url and 'https' not in url:
            url = 'http://' + url
        if action == 'm':
            print(find_emails(url))
        elif action == 't':
            print(find_title(url))
        elif action == 'n':
            print(find_phone_numbers(url))
# def main():
#     # jetBrains()
#     resp = requests.get('https://jb.gg/' + '501')
#     print('https://jb.gg/' + '500')
#     print(len(resp.text))


if __name__ == '__main__':
    main()
