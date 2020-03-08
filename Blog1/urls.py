from django.urls import path
from . import views


app_name = 'Blog1'
urlpatterns = [
    path('', views.index, name= 'index'),
    path('Blog1/nowy', views.nowy, name='nowy'),
    path('Blog1/<int:pk>', views.wpis, name='wpis'),
    path('Blog1/<int:pk>/edit', views.edycja, name='edycja'),

]