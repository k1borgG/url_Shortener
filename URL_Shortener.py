# It's my first day of work on GitHub
import bitly_api
BITLY_ACCESS_TOKEN = "ecd91fb52a39c362bee2bd577099ef61c1748c30"
access = bitly_api.Connection(access_token=BITLY_ACCESS_TOKEN)
full_link = input()
short_url = access.shorten(full_link)
print('Short URL = ', short_url['url'])
