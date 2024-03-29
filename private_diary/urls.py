"""private_diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from .import settings_common, settings_dev

# djangoの管理用URL
urlpatterns = [
    path("admin/", admin.site.urls),
    # 自作のアプリケーション用URL
    path('', include('diary.urls')),
    path('accounts/', include('allauth.urls')),
]

# 開発サーバーでメディアを配信できる様にする設定
# https://<ホスト名>/urlpatterns(ex.accounts)/MEDIA_URL('media')/MEDIA_ROOT(写真のパス)
# urlpatterns += static(settings_common.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)
