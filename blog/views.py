from django.shortcuts import render,get_object_or_404,redirect
from . models import Post


def post_list(request,post_slug=None):
    post=Post.objects.all()
    data=post_slug
    print(data)
    return render(request,'blog/list.html',{'post':post})


# Create your views here.
