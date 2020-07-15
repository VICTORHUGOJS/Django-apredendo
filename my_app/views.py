from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

#M - models.py
#V - html
#C - views.py

#MTV
#M- models-py
#T - Template.py
# V - viwes.py

def home(request):
    return HttpResponse('Hello!!')

def post_list(request):
   #name = 'Victor Hugo'
   #return render(request, 'post_list.html', {'name': name})
   posts = Post.objects.all()
   return render(request, 'post_list.html', {'posts': posts})


def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request,'post_show.html',{'post': post})