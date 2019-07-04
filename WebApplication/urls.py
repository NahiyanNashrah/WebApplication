"""WebApplication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from crudApplication import views

urlpatterns = [
    path('admin/', admin.site.urls),
  #  path('emp/', views.emp),
   # path('show/', views.show),
    #path('edit/<int:eid>', views.edit),
    #path('update/<int:eid>', views.update),
    #path('delete/<int:eid>', views.delete),
    path('consent_method/', views.consent_method),
    path('show_consent/', views.show_consent),
    path('receive/', views.receive),
    path('show_recipient/', views.show_recipient),
    path('cost/', views.cost),
    path('show_charge/', views.show_charge),
    path('blood_test_method/', views.blood_test_method),
    path('show_blood_test/', views.show_blood_test),
    path('store/', views.store),
    path('show_storage/', views.show_storage),
    path('create/', views.create),
    path('show_donor/', views.show_donor),
    path('info/', views.info),
    path('show_info/', views.show_info),
]
