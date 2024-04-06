from django.db.models import Count

from rest_framework import serializers

from .models import Post, PostImage, Comment, CommentImage, Tag


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = '__all__'


class CommentImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentImage
        fields = '__all__'


class CommentListSerializer(serializers.ModelSerializer):
    replies = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    comment_images = CommentImageSerializer(many=True, read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'comment_images', 'created_at','upvote_count', 'downvote_count', 'replies']

    def get_replies(self, obj):
        replies = obj.replies.annotate(upvote_count=Count('upvote')).order_by('-upvote_count')
        serializer = self.__class__(replies, many=True, context=self.context)
        return serializer.data

    def get_upvote_count(self, obj):
        return obj.upvote.count()

    def get_downvote_count(self, obj):
        return obj.downvote.count()
    
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['parent_comment', 'content',]
    

class PostListSerializer(serializers.ModelSerializer):
    images = PostImageSerializer(many=True, read_only=True)
    comments_count = serializers.SerializerMethodField()
    save_count = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'owner', 'name', 'slug', 'video', 'images', 'description', 'comments_count', 'tags', 'save_count', 'upvote_count', 'downvote_count', 'added_time', 'updated_time']

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
        return count

    def get_owner(self, obj):
        profile = obj.owner
        return {
            'id': profile.id,
            'username': profile.user.username,
            'profile_pic': profile.profile_pic.url if profile.profile_pic else None,
        }


class PostCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['name', 'video', 'description', 'tags']

        
class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['name', 'video', 'description', 'tags']

class PostChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['saves', 'upvote', 'downvote']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name",'hashtags']