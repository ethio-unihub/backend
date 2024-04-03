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
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'created_at', 'replies']

    def get_replies(self, obj):
        replies = obj.replies.all()
        serializer = self.__class__(replies, many=True, context=self.context)
        return serializer.data

class PostSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    save_count = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'name', 'slug', 'video', 'images','comments_count', 'tags', 'save_count', 'upvote_count', 'downvote_count', 'added_time', 'updated_time']

    def create(self, validated_data):
        validated_data['person'] = self.context['request'].user.profile
        return super().create(validated_data)
    
    def get_save_count(self, obj):
        return obj.saves.count()

    def get_upvote_count(self, obj):
        return obj.upvote.count()

    def get_downvote_count(self, obj):
        return obj.downvote.count()
    
    def get_comments_count(self, obj):
        return self.count_comments(obj)
    
    def count_comments(self, obj):
        main_comments = Comment.objects.filter(post=obj, parent_comment=None)
        count = main_comments.count()
        for comment in main_comments:
            count += self.count_replies(comment)
        return count

    def count_replies(self, comment):
        count = comment.replies.count()
        for reply in comment.replies.all():
            count += self.count_replies(reply)
        return count

