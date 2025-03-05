#!/usr/bin/python3

import requests
import passwords

user = passwords.username
passwd = passwords.password

requests.get("https://httpbin.org/basic-auth/jpaglia/test", auth=(user,password))
