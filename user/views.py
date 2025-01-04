from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import UserFormAuth, RegisterUserForm
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout
from django.views.generic import CreateView
from .models import Profile
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


def profile(request):



    return render(request, "registration/profile.html")