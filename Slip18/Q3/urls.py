from django.urls import path
from . import views
urlpatterns =[
    path('',views.learn_dj,name='learn_dj')
]
