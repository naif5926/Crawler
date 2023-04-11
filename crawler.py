#!/usr/bin/env python

import requests
from requests import exceptions


def request(url):
    try:
        res = requests.get("http://" + url)
        if res != "<Response [200]>":
            print("site not accessible")
        else:
            print(url + " returns ", res)
    except exceptions:
        print(exceptions)


target_url = input("Enter target url: ")
cmd = input("Enter 1 to find files and enter 2 to find subdomains: ")

if cmd == "1":
    with open("files.txt", "r") as wordlist:
        for x in wordlist:
            line = x.strip()
            url = target_url + "/" + line
            request(url)
elif cmd == "2":
    with open("subdomain.txt", "r") as wordlist:
        for x in wordlist:
            line = x.strip()
            url = line + "." + target_url
            request(url)
