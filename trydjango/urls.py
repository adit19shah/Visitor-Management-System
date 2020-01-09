"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path,include

from pages import views
urlpatterns = [
	path('',views.home_view, name='home'),
    path('hform/',views.host_view, name='hform'),
    path('vform/',views.checkin_view,name='vform'),
    path('oform/',views.checkout_view,name='oform'),
    path('eform/',views.exit_view,name='eform'),
    path('submit/',views.submit),
    path('submita/',views.submita),
    path('submitc/',views.submitc),
    path('submitd/',views.submitd),
    path('errora/',views.errora),
    path('errorb/', views.errorb),
    path('admin/', admin.site.urls),
]
