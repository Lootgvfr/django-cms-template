from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'),
    url('^news/$', views.NewsView.as_view(), name='news'),
    url('^pricing/$', views.PricingView.as_view(), name='pricing'),
    url('^faq/$', views.FAQView.as_view(), name='faq'),
    url('^contact/$', views.ContactView.as_view(), name='contact'),
]
