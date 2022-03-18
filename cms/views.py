from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Menu, Article
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    #mainpage = Menu.objects.get(slug='main')
    #articles = Article.objects.all().filter(active=True,).order_by('-id')[:7] 


    return render(request, 'cms/home.html', {})
