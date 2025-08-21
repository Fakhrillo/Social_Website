from django.contrib import admin
from images.models import Image
# Register your models here.

admin.site.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'image', 'created', 'modified')
    list_display_links = list_display
    list_filter = ('created', 'modified', 'user')

    