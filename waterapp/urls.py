from django.urls import path
from waterapp import views
urlpatterns=[
    path('calculate',views.calculate,name='cal'),
]