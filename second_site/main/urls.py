from django.urls import path
from . import views


urlpatterns = [
  path('',views.index),
  path('front',views.about, name='about'),
  path('down',views.back, name='down'),
  path('point',views.pie, name='point'),

]