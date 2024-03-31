from django.contrib import admin
from .models import Tag, Post, PostImage, Comment, CommentImage, Report

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'added_time', 'updated_time')
    list_filter = ('owner',)
    search_fields = ('name', 'description')
    date_hierarchy = 'added_time'
    prepopulated_fields = {'slug': ('name',)}
    exclude = ('owner_content_type', 'owner_object_id')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'added_time')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'comment_time')  # Exclude 'for_post' from list display
    list_filter = ('comment_time',)  # Adjust list_filter according to your needs
    search_fields = ('comment',)
    date_hierarchy = 'comment_time'

@admin.register(CommentImage)
class CommentImageAdmin(admin.ModelAdmin):
    list_display = ('comment', 'added_time')

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('reported_post', 'description', 'time')
    list_filter = ('time',)  # Adjust list_filter according to your needs
    search_fields = ('description',)
    date_hierarchy = 'time'
