import json
import urllib


def isrobot(request):
    url = 'https://www.google.com/recaptcha/api/siteverify'
    values = {
                'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
                'response': request,
            }
    data = urllib.parse.urlencode(values).encode()
    req =  urllib.request.Request(url, data=data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode())
    return result
