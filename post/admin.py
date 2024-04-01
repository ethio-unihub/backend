from django.contrib import admin
from .models import Tag, Post, PostImage, Comment, CommentImage, Report

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'added_time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(CommentImage)
class CommentImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reported_post', 'description', 'time')
    list_filter = ('time',)  # Adjust list_filter according to your needs
    search_fields = ('description',)
    date_hierarchy = 'time'
