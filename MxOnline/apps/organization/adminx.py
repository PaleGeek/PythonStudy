#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/6 15:52
import xadmin

from models import CityDict,Teacher,CourseOrg


class CityDictAdmin(object):
    list_display = ['name','desc','add_time']
    search_fields = ['name','desc','add_time']
    list_filter = ['name','desc','add_time']


class TeacherAdmin(object):
    list_display = ['name','org','work_years','work_company','work_position','points']
    search_fields = ['name','org','work_years','work_company','work_position','points']
    list_filter = ['name','org','work_years','work_company','work_position','points']


class CourseOrgAdmin(object):
    list_display = ['name', 'address', 'city', 'add_time']
    search_fields = ['name', 'address', 'city', 'add_time']
    list_filter = ['name', 'address', 'city', 'add_time']


xadmin.site.register(CityDict,CityDictAdmin)
xadmin.site.register(Teacher,TeacherAdmin)
xadmin.site.register(CourseOrg,CourseOrgAdmin)

