import time, num

print(time.asctime())
print(num.square(5))

from urllib.request import urlopen

response = urlopen('http://python.org')
print(response.headers)
# content=request.read()
# print(content)
