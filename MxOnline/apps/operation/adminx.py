#_*_coding:utf-8_*_
#作者     : fs
#创建时间 : 2019/3/6 15:52
import xadmin

from models import UserAsk,CourseComments,UserCourse,UserMessage,UserFavorite


class UserAskAdmin(object):
    list_display = ['name','mobile','course_name','add_time']
    search_fields = ['name','mobile','course_name','add_time']
    list_filter = ['name','mobile','course_name','add_time']


class CourseCommentsAdmin(object):
    list_display = ['user','course','comments','add_time']
    search_fields = ['user','course','comments','add_time']
    list_filter = ['user','course','comments','add_time']


class UserCourseAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course', 'add_time']
    list_filter = ['user', 'course', 'add_time']


class UserMessageAdmin(object):
    list_display = ['user', 'message', 'has_read', 'add_time']
    search_fields = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserFavoriteAdmin(object):
    list_display = ['user', 'course', 'add_time']
    search_fields = ['user', 'course', 'add_time']
    list_filter = ['user', 'course',  'add_time']


xadmin.site.register(UserAsk,UserAskAdmin)
xadmin.site.register(CourseComments,CourseCommentsAdmin)
xadmin.site.register(UserCourse,UserCourseAdmin)
xadmin.site.register(UserMessage,UserMessageAdmin)
xadmin.site.register(UserFavorite,UserFavoriteAdmin)

