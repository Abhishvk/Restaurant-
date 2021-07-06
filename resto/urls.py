
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path(r'^reg/',v.register,name="register"),
    path(r'^editi/',v.edit_info,name="editinfo"),
    path(r'^log/',v.login_view,name="login"),
    path(r'^logo/',v.logout_view,name="logout"),
    path(r'^cmsg/',v.contact_msg,name="contact"),
    path(r'^boo-table/',v.book_table,name="booktable"),
   
]
