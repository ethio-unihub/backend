from rest_framework import serializers
from .models import Post, PostImage, Comment, CommentImage
from django.contrib.contenttypes.models import ContentType

from user.serializers import ProfileSerializer


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    person = ProfileSerializer()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'person', 'replies']

    def get_replies(self, obj):
        replies = Comment.objects.filter(parent=obj)
        return CommentSerializer(replies, many=True).data


class PostSerializer(serializers.ModelSerializer):
    owner = ProfileSerializer()
    images = PostImageSerializer(many=True, read_only=True)
    # comments = CommentSerializer(many=True, read_only=True)
    save_count = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'name', 'slug', 'video', 'images', 'description', 'tags', 'save_count', 'upvote_count', 'downvote_count', 'added_time', 'updated_time']

    def get_save_count(self, obj):
        return obj.saves.count()

    def get_upvote_count(self, obj):
        return obj.upvote.count()

    def get_downvote_count(self, obj):
        return obj.downvote.count()
    
    def get_comments_count(self, obj):
        return self.count_comments(obj)

    def count_comments(self, obj):
        main_comments = Comment.objects.filter(content_type__model='post', object_id=obj.id, parent=None)
        count = main_comments.count()
        for comment in main_comments:
            count += self.count_replies(comment)
        return count

    def count_replies(self, comment):
        count = 0
        replies = Comment.objects.filter(parent=comment)
        count += replies.count()
        for reply in replies:
            count += self.count_replies(reply)
        return count

    def get_comments(self, obj):
        main_comments = Comment.objects.filter(content_type__model='post', object_id=obj.id, parent=None)
        return CommentSerializer(main_comments, many=True).data