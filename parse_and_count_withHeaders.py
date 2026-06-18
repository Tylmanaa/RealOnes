from urllib.request import Request, urlopen
url = "https://ru.wikipedia.org/wiki/Python"
req = Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
)
file = urlopen(req).read().decode('utf-8')
print(file.count('C++'))