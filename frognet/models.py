from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length = 200, null = False, blank = False, verbose_name = "Название поста")
    slug = models.SlugField(max_length = 200, null = False,unique=True,blank = False, verbose_name = "URL")
    description = models.TextField(null = True, blank=True, verbose_name="Описание")
    image = models.ImageField(upload_to="images", verbose_name="Картинка")
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
    time_created = models.DateTimeField(auto_now_add = True, verbose_name="Дата создания поста")
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"   

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)