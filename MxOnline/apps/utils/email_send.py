#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/7 18:08

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqSsTtUuVvWwXxYyZz1234567890'
    length= len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0,length)]
    return str


def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "mocc激活"
        eamil_body = "请点击下面的链接激活你的账号:http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title,eamil_body,EMAIL_FROM,[email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "mocc密码重置链接"
        eamil_body = "请点击下面的链接重置你的密码:http://127.0.0.1:8000/resetpwd/{0}".format(code)

        send_status = send_mail(email_title, eamil_body, EMAIL_FROM, [email])
        if send_status:
            pass
