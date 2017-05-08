import json
import urllib.parse as parse
import urllib.request as request

from django.conf import settings


def isrobot(requests):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
              'response': requests}
    data = parse.urlencode(values).encode()
    req = request.Request(url, data=data)
    response = request.urlopen(req)
    result = json.loads(response.read().decode())
    return result
