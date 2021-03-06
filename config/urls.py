"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# ---------------------------------- [edit] ---------------------------------- #
from django.urls import path, include
from pybo.views import Upload_views
from django.conf import settings
from django.conf.urls.static import static
# ---------------------------------------------------------------------------- #

urlpatterns = [
    path('admin/', admin.site.urls),
# ---------------------------------- [edit] ---------------------------------- #
    path('gist-graduation/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', Upload_views.upload_start, name='upload_start'),  # '/' 에 해당되는 path
# ---------------------------------------------------------------------------- #
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'common.views.page_not_found'
