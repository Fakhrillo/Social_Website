from django.contrib import admin
from account.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "date_of_birth", "photo")
    list_display_links = list_display
    raw_id_fields = ['user']