from django.http import Http404, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.views import LoginView
from .forms import UserFormAuth, RegisterUserForm, ProfileUser
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.views.generic import CreateView
from .models import Profile
from django.contrib.auth import get_user_model
from frognet.models import Post, Coment
from django.contrib.auth.decorators import login_required
# Create your views here.


class UserLogin(LoginView):
    form_class = UserFormAuth
    template_name = "registration/login.html"
    extra_context = {}

    # def get_success_url(self):
    #     print("yes")
    #     return reverse_lazy("frognet")
    

# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = "registration/regist.html"
#     #success_url = reverse_lazy("login")
def register(request):
    
    form = RegisterUserForm()
    if request.method == "POST":
        
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password1"])
            user.save()

            Profile.objects.create(user = user)
            
            return render(request, "registration/regist_done.html", {"form":form })
    else:
        return render(request, "registration/regist.html", {"form":form })



    return render(request, "registration/regist.html", {"form": form})





def logout_user(reqeust):
    logout(reqeust)
    return HttpResponseRedirect(reverse("login"))


def profile(request, id = None):

    #print(id)
    if id != None and id != request.user.id:
        another_user = get_user_model().objects.filter(id = id)
        another_user_profile = Profile.objects.filter(user_id = id)

        post = Post.objects.filter(author_id = another_user[0].id)
        coment_count = Coment.objects.filter(post_id = post[0].id).count()
        
        return render(request,"registration/another_user.html",{"another_user": another_user[0], "another_user_profile" : another_user_profile[0], "posts": post, "coment_count": coment_count})
    
    else:

        posts = Post.objects.filter(author_id = request.user.id)
        #print(posts[0].id)
        coment_count = Coment.objects.filter(post_id = posts[0].id).count()
        #print(coment_count)
        return render(request, "registration/profile.html", {"posts": posts, "coment_count": coment_count})


@login_required
def change_profile(request):

    try:
        profile = request.user.profile
    except  Profile.DoesNotExist:
        profile = None

    form = ProfileUser(instance=profile)

    if request.method == "POST":

        form = ProfileUser(request.POST, request.FILES, instance=profile)
        print("sss")
        if form.is_valid():
            # profile = form.save(commit = False)
            # profile.user = request.user
            # profile.save()
            form.save()

            return redirect("/user/profile/")

    return render(request, "registration/change_profile.html", {"form" : form})