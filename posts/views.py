from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Post
from .forms import PostForm
from django.utils.text import slugify

# Create your views here.

class ListView(View):
	def get(self,request):
		template_name = 'con.html'
		return render(request,template_name)


class List2View(View):
	def get(self,request):
		template_name = 'planta.html'
		return render(request,template_name)


class List3View(View):
	def get(self,request):
		template_name = 'contacto.html'
		return render(request,template_name)

class List4View(View):
	def get(self,request):
		template_name = 'organigrama.html'
		return render(request,template_name)

class List5View(View):
	def get(self,request):
		template_name = 'opera.html'
		return render(request,template_name)


class List6View(View):
	def get(self,request):
		template_name = 'proced.html'
		return render(request,template_name)

class List7View(View):
	def get(self,request):
		template_name = 'identifi.html'
		return render(request,template_name)

class AntecedenteView(View):
	def get(self,request):
		template_name = 'antece.html'
		return render(request,template_name)

class FuncionesView(View):
	def get(self,request):
		template_name = 'funcion.html'
		return render(request,template_name)


class MisionView(View):
	def get(self,request):
		template_name = 'mision.html'
		return render(request,template_name)

class ObjetivoView(View):
	def get(self,request):
		template_name = 'obje.html'
		return render(request,template_name)

class NotiView(View):
	def get(self,request):
		template_name ='noticias.html'
		posts = Post.objects.all()
		context={
			'posts':posts
		}
		return render (request,template_name,context)


		