from django.conf.urls import include, url

from apps.goods import views

urlpatterns = [
    url('^index$',views.index, name='index'),






]
