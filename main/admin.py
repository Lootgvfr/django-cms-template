from django.contrib import admin

from .models import PhotoItem, VideoItem, QuickPhotoItem


class PhotoGallery(admin.ModelAdmin):
    list_display = ('id', 'image',)
    list_editable = ('image',)


class VideoGallery(admin.ModelAdmin):
    list_display = ('id', 'src',)
    list_editable = ('src',)


class QuickPhotoGallery(admin.ModelAdmin):
    list_display = ('id', 'image',)
    list_editable = ('image',)


admin.site.register(PhotoItem, PhotoGallery)
admin.site.register(VideoItem, VideoGallery)
admin.site.register(QuickPhotoItem, QuickPhotoGallery)
