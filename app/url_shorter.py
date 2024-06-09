import zlib
import base64
import string
import random

class URLShortener:
    def __init__(self):
        self.url_map = {}

    def shorten(self, url):
        compressed_url = zlib.compress(url.encode())
        encoded_url = base64.b64encode(compressed_url).decode()
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
        self.url_map[short_code] = encoded_url
        return short_code

    def expand(self, short_code):
        encoded_url = self.url_map.get(short_code, '')
        if encoded_url:
            compressed_url = base64.b64decode(encoded_url)
            url = zlib.decompress(compressed_url).decode()
            return url
        return ''

url_shortener = URLShortener()

# Use the shorten method to generate a short code for the URL
url = "https://www.youtube.com/watch?v=pPBH2bB1FgI&list=RDauHVlqDIcpA&index=11"
short_code = url_shortener.shorten(url)
print(f"Short code: {short_code}")

# Use the expand method to get the original URL from the short code
original_url = url_shortener.expand(short_code)
print(f"Original URL: {original_url}")