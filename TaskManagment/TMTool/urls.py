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
    #Create-topic-page
    path('new_topic/', views.new_topic, name='new_topic'),
    #Create-entry-page
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    #Edit-entry-page
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

]