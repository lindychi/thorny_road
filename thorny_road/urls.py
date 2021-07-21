"""conf URL Configuration

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
from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'thorny_road'

urlpatterns = [
    path('', views.index, name='index'),

    path('add_asset/', views.add_asset, name="add_asset"),
    path('detail_asset/<int:aid>/', views.detail_asset, name="detail_asset"),

    path('ajax_collateral_name/', views.ajax_collateral_name, name="ajax_collateral_name"),
]
