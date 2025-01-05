from django.contrib import admin
from .models import Post, Coment
from django.utils.safestring import mark_safe
# Register your models here.

# admin.site.register(Post)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",),}
    list_per_page = 5   
    #list_display_links = ("post_photo",)
    readonly_fields = ["post_photo"] # если хотим чтоб в админке отоброжалось фото тогда надо его записать еще и в переменную только чтения
    ordering = ["author_id"]
    save_on_top = True

    @admin.display(description="Фотография")
    def post_photo(self, ps:Post):
        if ps.image:
            return mark_safe(f"<img src = '{ps.image.url}' width=50>") # С помошью mark_safe html теги будут отображатся как теги а не как обычный текст
        else:
            return "Нету фотографии"


@admin.register(Coment)
class ComentAdmin(admin.ModelAdmin):
    save_on_top = True
    
    
    