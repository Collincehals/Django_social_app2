from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import *


@login_required(login_url='/accounts/login')
def create_post(request):
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            form.save_m2m()
            messages.success(request, "Post created successfully")
            return redirect('posts')
    return render(request, 'main/post_create_form.html', {'form': form})

def Posts(request, tag=None):
    if tag:
        posts = Post.objects.filter(tags__slug=tag)
        tag = get_object_or_404(Tag, slug=tag)
    else:
        posts = Post.objects.all()
    categories =Tag.objects.all()
    context ={
        'posts': posts,
        'tag': tag,
        'categories': categories
    }
    return render(request, 'main/home.html', context)

def PostPage(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'main/post_page.html', {'post':post})

def PostDelete(request, pk):
    post = get_object_or_404(Post, id=pk )
    if request.method =='POST':
        post.delete()
        messages.success(request, "Post deleted Successfully!!")
        return redirect('posts')
    return render(request, 'main/post_delete.html', {'post':post})

def PostEditView(request, pk):
    post = get_object_or_404(Post, id=pk)
    form = PostEditForm(instance=post)
    if request.method =='POST':
       form = PostEditForm(request.POST, instance=post)
       if form.is_valid:
           form.save()
           messages.success(request, 'Post edited Successfully!')
           return redirect('posts')
    return render(request, 'main/post_edit.html', {'post':post, 'form':form})

def Profile(request, username=None):
    if username:
        user = get_object_or_404(User, username=username)
        profile = user.profile
        posts = Post.objects.filter(author=user)
    else:
        try:
            profile = request.user.profile
            posts = Post.objects.filter(author=request.user)
        except:
            raise Http404()      
    return render(request, 'main/profile.html', {'profile':profile, 'posts':posts})

def EditProfileView(request):
    profile= request.user.profile
    form = ProfileEditForm(instance=profile)
    if request.method == 'POST':
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile edited Successfully!')
            return redirect('profile') 
    context = {
        'profile':profile, 
        'form':form
        }
    return render(request, 'main/edit_profile.html',context)


def DeleteProfile(request):
    user=request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, "Profile deleted successfully")
        return redirect('posts')
    return render(request, 'main/delete_profile.html')


def URLVideos(request):
    videos = Item.objects.all()
    return render(request,'main/urlvideos.html', {'videos': videos})