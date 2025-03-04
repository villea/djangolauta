from django.shortcuts import render,redirect

# Create your views here.

from django.http import HttpResponse
from .models import Post, Comment


def threads(request):
    posts = Post.objects.all()
    return render(request, 'threads/posts.html', {'posts': posts})

def show_post(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post)
    return render(request, 'threads/show_post.html', {'post': post, 'comments': comments})


def new_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(title=title, content=content)
        
        return redirect('threads')
    return render(request, 'threads/new_post.html')

def reply_post(request, post_id):
    print("DEBUG")
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
      
        print(f"DEBUG: Post ID: {post_id}")
        print(f"DEBUG: Request POST data: {request.POST}")
        content = request.POST['content']
        Comment.objects.create(post=post, content=content)
        return redirect('show_post', post_id=post_id)
    return redirect('show_post', post_id=post_id)
