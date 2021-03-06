"""MDA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from socius import views as v
from directory import views as vd
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.index, name="index"),
    path('index.html', v.index, name="index"),
    path('directorypage.html', v.directorypage, name="directorypage"),
    path('team.html', v.Team, name="team"),
    path('create', v.create, name="create"),
    path('members',v.members,name="members"),
    path('joined',v.joined,name="joined"),
    path('joindirectory',v.joindirectory,name="joindirectory"),
    path('accounts/',include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('',include('Coupons.urls')),
    path('adduser/',v.simple_upload,name='simple_upload'),
    path('active/<uidb64>/<token>/',v.active, name='active'),
    
]


urlpatterns=urlpatterns+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

