#coding:utf8
from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    url(r'regist/$',  'blog.views.regist_user'),	#注册
    url(r'login/$',  'blog.views.login_user'),	#登录
    url(r'index/$', 'blog.views.index'),		#主页
    url(r'logout/$' , 'blog.views.logout_user'),	#注销
    url(r'add/$', 'blog.views.post_add'),		#发帖子
    url(r'(\d+)/$' ,'blog.views.post_disp'),		#显示帖子
    url(r'(\d+)/reply/', 'blog.views.reply'),	#回帖
)
