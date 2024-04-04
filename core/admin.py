from django.contrib import admin
from .models import Organization, Hashtag

'''
@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('community_name', 'owner')
    search_fields = ('community_name',)
'''
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name',)

@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_name', 'subscribers_list')
    list_filter = ('organization',)
    search_fields = ('name', 'organization__name')
    readonly_fields = ('slug',)

    def organization_name(self, obj):
        return obj.organization.name
    organization_name.short_description = 'Organization'

    def subscribers_list(self, obj):
        return ", ".join([profile.user.username for profile in obj.subscribers.all()])
    subscribers_list.short_description = 'Subscribers'

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['organization'].widget.can_add_related = False
        return form
