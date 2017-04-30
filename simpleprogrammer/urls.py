"""simpleprogrammer URL Configuration
f
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from website import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',views.home, name='home'),
    url(r'^article/(?P<pk>[0-9]*)$', views.ArticleDetail.as_view(), name='article'),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG and settings.MEDIA_URL[0] == '/':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




