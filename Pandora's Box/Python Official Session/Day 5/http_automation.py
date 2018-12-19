print('-' * 70)

from urllib.request import urlopen

# urlopen
page = urlopen('http://www.google.co.in')
print('Status ->', page.getcode())
print(page.read(500))

print('-' * 70)

# Used to parse values into the url
from urllib.parse import urlencode

values = {
    'q': 'python scripting'
}
data = urlencode(values)

url = 'http://www.google.co.in?%s' % data
resp = urlopen(url)

with open('data.html', 'w') as fhtml:
    fhtml.write(str(resp.read()))

print('HTML Created Successfully')

print('-' * 70)
