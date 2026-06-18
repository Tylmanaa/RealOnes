from urllib import request
html= request.urlopen('https://google.com').read().decode('utf-8')
s=str(html)
print(s.count('g')) 