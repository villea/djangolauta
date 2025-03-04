from django.urls import path
from . import views
urlpatterns = [

    path('', views.threads, name='threads'),
    path('new_post/', views.new_post, name='new_post'),
    path('posts/<int:post_id>/', views.show_post, name='show_post'),
    path('posts/<int:post_id>/reply/', views.reply_post, name='reply_post'),
]