"""定义blogs的URL模式"""
from django.urls import path

from . import views

app_name = 'blogs'
urlpatterns = [
    #主页
    path('',views.index,name='index'),
    #显示所有博客
    path('blog',views.blogs,name='blogs'),
    #显示特定主题的详细页面
    path('bolgs/<int:blog_id>',views.blog,name='blog'),
    #用于添加新Blog的网页
    path('new_blog/',views.new_blog,name='new_blog'),
    #用于编辑现有blog的页面
    path('edit_blog/<int:blog_id>',views.edit_blog,name='edit_blog'),
]
    