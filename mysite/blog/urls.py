from django.conf.urls import url
from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [
    path('', PostLV.as_view(), name='index'),
    path('post/', PostLV.as_view(), name='post_list'),
    path('post/<str:slug>/', PostDV.as_view(), name='post_detail'),
    path('archive/', PostAV.as_view(), name='post_archive'),
    path('<int:year>/', PostYAV.as_view(), name='post_year_archive'),
    path('<int:year>/<str:month>/', PostMAV.as_view(), name='post_month_archive'),
    path('<int:year>/<str:month>/<int:day>/', PostDAV.as_view(), name='post_day_archive'),
    path('today/', PostTAV.as_view(), name='post_today_archive'),
]
