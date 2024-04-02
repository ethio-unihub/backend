from rest_framework import serializers
from .models import Organization, Hashtag



class OrganizationSerializer(serializers.ModelSerializer):
    # hashtags=HashtagSerializer(read_only=True, many=True)
    class Meta:
        model=Organization
        fields='__all__'


class HashtagSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()
    class Meta:
        model=Hashtag
        fields=['id','name', 'organization','subscribers', ' slug']





