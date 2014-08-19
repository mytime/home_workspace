#coding:utf8
from django.db import models
from django.contrib.auth.models import User

#发帖子
#新建模型后需要用 schemamigration  初始化一下blog应用
#python manage.py schemamigration blog --initial

#发帖
class Post(models.Model):
	title = models.CharField(max_length=50,verbose_name=u'标题')
	content = models.TextField(verbose_name=u'内容')
	p_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.title[:10]

#回帖
#添加模型后需要执行
# python manage.py schemamigration blog --auto	#修改数据库
# python manage.py migrate blog	#同步数据库
class  Reply(models.Model):
	content = models.TextField(verbose_name=u'内容')
	p_date = models.DateTimeField(auto_now=True, auto_now_add=True)
	post = models.ForeignKey(Post)
	user = models.ForeignKey(User)

