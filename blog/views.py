from django.shortcuts import render
from .models import Blog
# Create your views here.
def allblogs(request):
    allblog = Blog.objects

    return render(request,'blog/allblogs.html',{'allblog': allblog})
