#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/6 15:28

import xadmin

from models import Course,CourseResource,Lesson,Video


class CourseAdmin(object):
    list_display = ['name','degree','learn_time']
    search_fields = ['name','degree','learn_time']
    list_filter = ['name','degree','learn_time']


class CourseResourceAdmin(object):
    list_display = ['name','course','add_time']
    search_fields = ['name','course','add_time']
    list_filter = ['name','course','add_time']


class LessonAdmin(object):
    list_display = ['name','course','add_time']
    search_fields = ['name','course','add_time']
    list_filter = ['name','course','add_time']


class VideoAdmin(object):
    list_display = ['name','lesson','add_time']
    search_fields = ['name','lesson','add_time']
    list_filter = ['name','lesson','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(CourseResource,CourseResourceAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)