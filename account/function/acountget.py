import re


def getlastname(user):
    full_name = user.get_full_name()
    regexlastname = re.search('(?<=\s).*$', full_name)
    if regexlastname:
        return regexlastname.group(0)
    else:
        return ''
