from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('packages/',views.packages, name='packages'),
    path('destination/',views.destination, name='destination'),
    path('about/',views.about_us,name='about_us'),
    path('create/', views.tour_create, name='tour_create'),
    path('update/<int:pk>/', views.tour_update, name='tour_update'),
    path('delete/<int:pk>/', views.tour_delete, name='tour_delete'),
]
