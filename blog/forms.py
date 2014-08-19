#coding:utf8
from django import forms
from django.contrib.auth.models import User		#用户表
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate	#用户验证
from blog.models import Post ,Reply	#Post表(模型）

#用户注册
class UserRegistForm(forms.Form):
	username = forms.CharField(label=u'姓名')
	email = forms.EmailField(label=u'邮箱')
	password = forms.CharField(label=u'密码',widget=forms.PasswordInput())
	repassword = forms.CharField(label=u'确认密码',widget=forms.PasswordInput())
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		users = User.objects.filter(username = username)
		if len(users) > 0:
			raise forms.ValidationError(u'用户名已存在')
		return username
	
	def clean_email(self):
		email = self.cleaned_data.get('email')
		emails = User.objects.filter(email = email)
		if len(emails) > 0:
			raise forms.ValidationError(u'邮箱被占用')
		return emails
		
 	def clean(self):
 		password = self.cleaned_data.get('password')
 		repassword = self.cleaned_data.get('repassword')
 		if password != repassword:
 			raise forms.ValidationError(u'口令不一致')
 		else:
 			return self.cleaned_data
  #用户登录			
class UserLoginForm(forms.Form):
	username = forms.CharField(label=u'姓名')	
	password = forms.CharField(label=u'密码',widget=forms.PasswordInput())
	
	def clean_username(self):
		username = self.cleaned_data.get('username')
		users = User.objects.filter(username = username)	#筛选是“X”的用户，有是1，无是0
		if len(users) != 1:
			raise forms.ValidationError(u'用户不存在')
		return username	
	
	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		
		user = authenticate(username=username,password=password)
		if user is None:
			raise forms.ValidationError(u'用户/密码不正确')
		return self.cleaned_data

#发帖
class Post_addForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title','content']

#回帖
class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		field = ['content']

		
	
	
	
