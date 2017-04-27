from django.contrib import admin
from website.models import Author,Article,Video,ResourceCategory,Resource


class AuthorAdmin(admin.ModelAdmin):
    fields = ('name','bio')
    list_display = ('name', 'bio', )
    list_filter = ('name', )
    search_fields = ('name', )


class ArticleAdmin(admin.ModelAdmin):
    fields = ('title','post','picture','author','video_url',)
    list_display = ('title', 'date','author',)
    list_filter = ('title', 'date','author',)
    search_fields = ('title,author',)


class VideoAdmin(admin.ModelAdmin):
    fields = ('title', 'video_url','video_thumbnail' , 'author',)
    list_display = ('title', 'date', 'author',)
    list_filter = ('title', 'date', 'author',)
    search_fields = ('title,author',)


class ResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name',)


class ResourceAdmin(admin.ModelAdmin):
    list_display = ('category','title','description')
    list_filter = ('category','title','description')
    search_fields = ('title',)


# Register your models here.

admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(ResourceCategory, ResourceCategoryAdmin)
admin.site.register(Resource, ResourceAdmin)