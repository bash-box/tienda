from django.contrib import admin
from .models import Categoria, Post


class CategoriaAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_field = ('created', 'updated')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)

