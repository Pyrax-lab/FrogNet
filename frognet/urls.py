from django.urls import path 
from . import views

urlpatterns = [
    path('',views.frognet, name="frognet"),
    path("add_post/", views.add_post, name="add_post"),
    path("post_list/", views.post_list, name="post_list"),
    path("post_list/<int:id>/", views.post_list_id, name="id_post"),
]