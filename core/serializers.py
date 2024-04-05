from rest_framework import serializers
from .models import Organization, Hashtag, Report


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


class HashtagSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = Hashtag
        fields = ['id', 'name', 'organization', 'subscribers', 'slug']

    def validate_slug(self, value):
        if Hashtag.objects.filter(slug=value).exists():
            raise serializers.ValidationError("This slug already exists.")
        return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['organization'] = {
            'id': instance.organization.id,
            'name': instance.organization.name
        }
        return representation


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'