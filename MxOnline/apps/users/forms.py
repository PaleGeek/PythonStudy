#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/7 15:01
from django import forms
from captcha.fields import CaptchaField,ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=5)
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u"验证码错误"})


class ModifyPwdForm(forms.Form):
    email = forms.CharField(required=True)
    password = forms.CharField(required=True,error_messages={"invalid":u"密码不能为空"})
    password2 = forms.CharField(required=True,error_messages={"invalid": u"重复密码不能为空"})

    def clean(self):
        print(self.cleaned_data['password'])
        print(self.cleaned_data['password2'])
        if self.cleaned_data['password'] == self.cleaned_data['password2']:
            return self.cleaned_data
        else:
            self.add_errors("password2", ValidationError("密码不一致"))
            return self.cleaned_data



