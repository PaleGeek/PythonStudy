#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/6 14:24

import xadmin

from models import EmailVerifyRecord,Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "mooc后台管理系统"
    site_footer = "mooc在线"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type']
    list_filter = ['code','email','send_type','send_time']


class BannerAdmin(object):
    list_display = ['title','image','url','index','add_time']
    search_fields = ['title','image','url','index','add_time']
    list_filter = ['title','image','url','index','add_time']


xadmin.site.register(EmailVerifyRecord,EmailVerifyRecordAdmin)
xadmin.site.register(Banner,BannerAdmin)
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)