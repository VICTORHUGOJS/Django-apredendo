from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category

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
    if 'category_id' in request.GET:
        category = Category.objects.get(id=request.GET['category_id'])
        posts = Post.objects.filter(categories=category)
    else:     
        posts = Post.objects.all()
    categories = Category.object.all()    
    return render(request,'post_list.html',{ 
        'posts': posts,
        'categories': categories
    })



def post_show(request, post_id):
    post = Post.objects.get(id=post_id)
    categories = Category.objects.all()
    return render(request,'post_show.html',{
        'post': post,
        'categories': categories
        })