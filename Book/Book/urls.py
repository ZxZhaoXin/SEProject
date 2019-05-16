"""Book URL Configuration

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
from django.urls import path, re_path
from flight import views as flights_view
from account import views as account_views
from base import views as base_views
from administrator import views as admin_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', base_views.base),
    path('base/info/', base_views.info),
    path('base/info/confirm/', base_views.confirm),
    path('account/register/', account_views.register),
    path('account/login/', account_views.login),
    path('administrator/', admin_views.admin),
    path('account/logout/', account_views.logout),
    # r'(?P<good_id>\d+)/$','detail'
    path('account/rate/',account_views.rate),
    path('form_salesman/', flights_view.salesman),
    path('insert_flight/', flights_view.insert_flight),
    path('query_flight/', flights_view.query_flight),
    path('operate_flight/', flights_view.operate_flight),
    path('add_salesman/', admin_views.add_salesman),
    path('check_salesman/', admin_views.check_salesman),
    path('operate_salesman/', admin_views.operate_salesman),
]


