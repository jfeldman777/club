from django.urls import path, include
from . import views

urlpatterns = [
#int str path  slug UUID
    path('<int:year>/<str:month>',views.home,name='home'),
    path('',views.home,name='home'),
]
