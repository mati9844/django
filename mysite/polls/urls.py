from django.conf.urls import url
from django.urls import path

from . import views
from .views import PozycjaZakupowaListView, SklepListView, ListaView, FormView

urlpatterns = [
    path('', views.index, name='index'),
    path("zad3/", PozycjaZakupowaListView.as_view()),
    url("lista/", ListaView.as_view()),
    url("form/", FormView.as_view())

]