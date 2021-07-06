
import order
from django.contrib import admin
from django.urls import path,include
from resto.views import home 

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path(r'^order/',include(('order.urls','order'),namespace="orders")),
    path(r'^resto/',include(('resto.urls','resto'),namespace="restos")),
]
