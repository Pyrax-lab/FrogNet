from urllib import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
# Create your views here.


#@login_required
def frognet(request):
    return render(request, "frognet/main.html")

def add_post(request):
    post_form = PostForm()

    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            try:
                clear_post = post_form.save(commit=False)
                clear_post.author = request.user
                clear_post.save()
                #return redirect("frognet")
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
    
    return render(request, "frognet/post_id.html", context={"post":post})