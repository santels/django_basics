from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
	url(r'^edit/(?P<pk>\d+)/$', views.Update.as_view(), name='update'),
]
