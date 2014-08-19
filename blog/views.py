#coding:utf8
from django.shortcuts import render, redirect	#导入redirect 重定向
from django.http import HttpResponse
from blog.forms import UserRegistForm, UserLoginForm, Post_addForm, ReplyForm	#导入form.py里的UserRegistForm对象
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User	#连接数据库
from blog.models import Post,Reply
#装饰器，发帖/回帖 判断用户是不是已经登录@login_required
from django.contrib.auth.decorators import login_required	

#用户注册
def regist_user(req):
	if req.method == "POST":
		urf = UserRegistForm(req.POST)
		if urf.is_valid():
		
			#print urf.cleaned_data
			username = urf.cleaned_data.get('username')
			email = urf.cleaned_data.get('email')
			password = urf.cleaned_data.get('password')
			#插入数据库
			User.objects.create_user(username=username, 
				password=password ,email=email)
			
			#return HttpResponse('regist ok!')
			return redirect('/user_login/')
	else:
		urf = UserRegistForm()
	return render(req,'regist.html',{'urf':urf})
	
#用户登录	
def login_user(req):
	if req.method == 'POST':
		urf = UserLoginForm(req.POST)
		if urf.is_valid():
			username = urf.cleaned_data.get('username')
			password = urf.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			login(req,user)
			#return HttpResponse('login ok ')
			return redirect('/blog/index/')

	else:
		urf = UserLoginForm()
		
	return render(req,'user_login.html', {'urf':urf})

#首页
def index(req):
	posts = Post.objects.all()
	return render(req, 'index.html',{'posts':posts})

#注销	
def logout_user(req):
	logout(req)
	return redirect('/blog/index/')

#发帖前执行登录检查
@login_required(login_url='/blog/login/')
#发帖
def post_add(req):
	if req.method == 'POST':
		urf = Post_addForm(req.POST)
		if urf.is_valid():
			urf = urf.save(commit = False)
			urf.user = req.user
			urf.save()
			return redirect('/blog/index')
	else:
		urf = Post_addForm()
	return render(req,'post_add.html',{'urf':urf})

#显示帖子
def post_disp(req,post_id):
	post = Post.objects.get(id=post_id)
	return render(req,'post_disp.html', {'post':post})

#回帖
#回帖前执行登录检查
@login_required(login_url='/blog/login/')
def reply(req,post_id):
	post = Post.objects.get(id=post_id)
	if req.method == "POST":
		urf = ReplyForm(req.POST)
		if urf.is_valid():
			urf = urf.save(commit=False)
			print req.user
			urf.user = req.user
			urf.post = post
			urf.save()
			return redirect('/blog/%s/' % post.id)
	else:
		urf = ReplyForm()
	return render(req, 'reply.html',{'urf':urf})

