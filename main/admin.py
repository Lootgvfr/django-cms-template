from django.contrib import admin

from .models import PhotoItem, VideoItem


class PhotoGallery(admin.ModelAdmin):
    list_display = ('id', 'image',)
    list_editable = ('image',)


class VideoGallery(admin.ModelAdmin):
    list_display = ('id', 'src',)
    list_editable = ('src',)


admin.site.register(PhotoItem, PhotoGallery)
admin.site.register(VideoItem, VideoGallery)
