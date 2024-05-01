from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns=[
    path('',index,name='index'),
    path('add_tache',add_tache,name='add_tache'),
    path('delete_tache/<int:myid>/',delete_tache,name='delete_tache'),
    path('edit_tache/<int:myid>/',edit_tache,name='edit_tache'),
    path('update_tache/<int:myid>/',update_tache,name='update_tache'),
]