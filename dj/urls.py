
from django.conf.urls import url
from django.contrib import admin

from posts.views import posts_list

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^posts/', posts_list),
]
