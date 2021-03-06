"""innv URL Configuration

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
from django.urls import path
from . import views
from .views import HelpView
app_name='disaster'
from disaster.views import DisasterDetailsView
urlpatterns = [
    path('', views.home,name='home'),
    path('help/',views.help_page,name='help'),
    path('notify/',views.notify,name='notify'),
    path('disasters/<int:pk>',DisasterDetailsView.as_view(),name='disasterdetailview'),
    path('signup',views.sign_up,name='sign_up')
]
