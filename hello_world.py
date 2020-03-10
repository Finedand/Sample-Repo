import math
import sys
from os import rename

import requests

test = "test"

print(sys.version)
print(sys.executable)
# print('worlddsda')
r = requests.get("https://coreyms.com")
print(r.status_code)


def greet(who_to_greet):
    greeting = f"hello, {who_to_greet}!"
    return greeting
