"""bloga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap
from django.conf import settings
from django.conf.urls.static import static

from mbaseApp.sitemaps import ArticlesSitemap
from creationApp.sitemaps import CreationSitemap
from mainApp.sitemaps import MainPageSitemap, ProtfolioSitemap


sitemaps = {
    'articles': ArticlesSitemap,
    'creation': CreationSitemap,
    'portfolio': ProtfolioSitemap,
    'main': MainPageSitemap,
}


handler404 = 'mainApp.views.e_handler404'
handler500 = 'mainApp.views.e_handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('tinymce/', include('tinymce.urls')),
    path('methodical-base/', include('mbaseApp.urls')),
    path('creation/', include('creationApp.urls')),
    path('gallery/', include('galleryApp.urls')),
    path('advices-for-parents/', include('adviceApp.urls')),
    path('achiev-board/', include('boardApp.urls')),
    path('normative-base/', include('nbaseApp.urls')),
    path('feedback/', include('feedbackApp.urls')),
    path('', include('mainApp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)