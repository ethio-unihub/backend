from rest_framework import serializers

from .models import UserFile
from post.serializers import TagSerializer
from user.serializers import ProfileDetailSerializer

class FileListSerializer(serializers.ModelSerializer):
    save_count = serializers.SerializerMethodField()
    upvote_count = serializers.SerializerMethodField()
    downvote_count = serializers.SerializerMethodField()
    download_count = serializers.SerializerMethodField()
    tag = TagSerializer(many=True, read_only=True)
    author = ProfileDetailSerializer(many=False, read_only=True)
    class Meta:
        model = UserFile
        fields = ['id', 'save_count', 'upvote_count', 'downvote_count', 'download_count', 'tag', 'author', 'file']
    
    def get_save_count(self, obj):
        return obj.saves.count()

    def get_upvote_count(self, obj):
        return obj.upvotes.count()

    def get_downvote_count(self, obj):
        return obj.downvotes.count()

    def get_download_count(self, obj):
        return obj.downloads.count()
    

class FileCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['id', 'name', 'file', 'tag', 'author']
    

class FileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFile
        fields = ['id', 'upvotes', 'downvotes', 'downloads', 'saves']