from django.contrib import admin
from .models import User, Profile, Badge, Notification

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_pic', 'org_email', 'verified_org')
    search_fields = ('user__username', 'org_email')
    list_filter = ('verified_org',)

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ('badge_name', 'badge_image_preview', 'badge_descriptinon')
    search_fields = ('badge_name', 'badge_descriptinon')

    def badge_image_preview(self, obj):
        return obj.badge_image.url if obj.badge_image else None

    badge_image_preview.short_description = 'Badge Image Preview'

admin.site.register(Notification)