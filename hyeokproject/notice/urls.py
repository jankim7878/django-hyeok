from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [

    path('<int:notice_id>/', views.detail, name='detail'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('aboutme/', views.aboutme, name='aboutme'),
    path('<int:notice_id>/delete', views.delete, name='delete'),
    path('<int:notice_id>/edit', views.edit, name='edit'),
    path('<int:notice_id>/update', views.update, name='update'),
]