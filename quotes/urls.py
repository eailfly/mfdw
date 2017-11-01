from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.quote_req, name='quote-request'),
]
