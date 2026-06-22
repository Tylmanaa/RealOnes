# Скачать файл, обработать и 

from urllib import request

html=request.urlopen('https://google.com').read().decode('utf-8')

print(html)

try: 
    with open('report.txt','w') as file:
        file.write(html)

except FileNotFoundError:
    print('Файл не найден')