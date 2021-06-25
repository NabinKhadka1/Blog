from django import contrib
from django import urls
from django.contrib import admin, auth
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/',include('accounts.urls')),
    path('',include('blog.urls')),
]
