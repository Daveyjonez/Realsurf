from django.conf.urls import url
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # /index/
    url(r'^$', views.index, name='index'),

    # /report/
    url(r'(?P<beach_id>[0-9]+)$', views.get_report, name='get_report'),
]
