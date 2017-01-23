__author__ = 'vladbirukov'
import re
email_my = 'vlan+bs.ui.r@ma.ill.ru'
def email_check(email):
    com = re.compile('[-a-z0-9_]{3,} @ [-a-z0-9_]{2,} \. [a-z]{2,3}',re.I|re.X)
    ser = com.match(email)
    if ser == None:
        check = False
    else:
        check = True
    return check
print email_check(email_my)

num ='2re.3r'
def number_check(number):
    com = re.compile('[0-9]{1,}\.[0-9]{1,}', re.I|re.X)
    ser = com.match(str(number))
    if ser == None:
        check = False
    else:
        check = True
    return check
print number_check(num)

# IEEE75

url = 'http://otvet.mail.ru/mail/ipv12345/   /'
def url_check(url):
    com = re.compile(r'^(?:http|ftp)s?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.I|re.X)
    ser = com.match(url)
    if ser == None:
        check = False
    else:
        check = True
    return check
print url_check(url)
