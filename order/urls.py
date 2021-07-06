
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path(r'^menu/',v.menu_view,name="menu"),
    path(r'^bookin/',v.booking_view,name="bookings"),
    path(r'^deln/',v.delete_view,name="delete"),
]
