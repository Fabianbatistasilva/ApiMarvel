from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('comicsEspecifico/<int:id>/',views.comicsEspec,name='comicsEspecifico'),
    path('comics/',views.comics,name='comics'),
    path('Series/',views.Serie,name='serie'),
    path('Creators/',views.Creators,name='Creators'),
    path('creatorSpecific/<int:id>/',views.creatorSpecific,name='creatorSpecific'),
    path('',views.index,name='home'),
]
