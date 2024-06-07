from app.utils import urlShortener

u = urlShortener()
long_url = "https://www.tutorialspoint.com/python-url-shortener-using-tinyurl-api"

r = u.convert_long_to_short_url(long_url)
print(r)

