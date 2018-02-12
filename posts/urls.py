
from django.conf.urls import url

from .views import posts_list, posts_detail

urlpatterns = [
    url(r'^$', posts_list),
    url(r'^(?P<slug>[\w-]+)/', posts_detail)
]
