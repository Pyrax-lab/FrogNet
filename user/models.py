from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Profile(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile = models.ImageField(default="default.jpg", upload_to="iamges", verbose_name="Профиль")
    bio = models.TextField(blank=True, null=True , verbose_name="Биография")
    baner = models.ImageField(default = "5.jpg", upload_to="images", verbose_name="Банер профиля")


    def __str__(self):
        return self.user.username 
    
    class Meta:
        db_table = "profile"
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        