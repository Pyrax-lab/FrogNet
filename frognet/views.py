from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post, Coment
from .forms import PostForm, ComentForm
from django.contrib.auth import get_user_model
# Create your views here.


#@login_required
def frognet(request):
    return render(request, "frognet/main.html")


@login_required
def add_post(request):
    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            try:
                clear_post = post_form.save(commit=False)
                clear_post.author = request.user
                clear_post.save()
                return redirect("post_list")
            except Exception as a:
                post_form.add_error(None, a)
    else:
        post_form = PostForm()



    return render(request, "frognet/posts.html", context={"post_form": post_form})



def post_list(request):
    posts = Post.objects.all()
    return render(request, "frognet/post_list.html", context={"posts": posts})


def post_list_id(request, id):
    post = Post.objects.get(id = id)
    author = get_user_model().objects.filter(id = post.author_id)[0]

    coments = Coment.objects.filter(post_id = id)

    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            coment = form.save(commit=False)
            coment.author_id = request.user.id 
            coment.post_id = post.id
            coment.save()
            #redirect 
    else:
        form = ComentForm()
    
    return render(request, "frognet/post_id.html", context={"post":post, "author": author, "coments": coments, "form": form})