from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'main/base.html'

    def get_context_data(self, **kwargs):
        return {
            'navbar_dark': True,
        }


class NewsView(TemplateView):
    template_name = 'news/base.html'


class PricingView(TemplateView):
    template_name = 'pricing/base.html'


class GalleryView(TemplateView):
    template_name = 'gallery/base.html'


class GalleryVideoView(TemplateView):
    template_name = 'gallery/base_video.html'
