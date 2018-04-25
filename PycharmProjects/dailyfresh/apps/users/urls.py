from django.conf.urls import include, url

from apps.users import views

urlpatterns = [

 url('^register$',views.register,name="register"),
 url('^do_register$',views.do_register,name="do_register"),

]
