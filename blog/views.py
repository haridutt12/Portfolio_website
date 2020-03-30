from django.shortcuts import render
from django.http import  request
from .models import Post, Category, Comment
from .forms import CommentForm
# Create your views here.



def blog_index(request):
    posts  = Post.objects.all().order_by('-created_on')
    context = {
        "posts":posts,
    }
    return render(request,  "blog_index.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(category__category__contains=category).order_by('-created_on')
    context = {
        'category':category,
        'posts':posts
    }
    return render(request, 'blog_category.html', context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            com = Comment(
                author = form.cleaned_data["author"],
                comment = form.cleaned_data["body"],
                post = post                
            )
            com.save()

    comment = Comment.objects.filter(post=post)
    context = {
        'post':post,
        'comments':comment,
        'form': form,
    }
    return render(request, "blog_detail.html", context)

