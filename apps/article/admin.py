from django.contrib import admin
from .models import Categories, Tags, Articles, Comments


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "icon", "slug")
    list_display_links = ("id", "name", "icon")
    search_fields = ("id", "name", "icon")
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Categories, CategoriesAdmin)


class TagsAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    search_fields = ("id", "name")
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tags, TagsAdmin)


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "image", "min_to_read")
    list_display_links = ("id", "title")
    search_fields = ("id", "title")
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("category", "tag")


admin.site.register(Articles, ArticlesAdmin)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ("id", "article", "commenter", "text", "parent")
    list_display_links = ("id", "article")
    search_fields = ("id", "article", "text")
    date_hierarchy = 'created_at'


admin.site.register(Comments, CommentsAdmin)
