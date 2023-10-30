from django.urls import path
from . import views

app_name = 'TMTool'

urlpatterns = [
    #main-page
    path('', views.index, name='index'),
    #Topics-page
    path('topics/', views.topics, name='topics'),
    #Topic-page
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]