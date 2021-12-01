from django.urls import path
from . import views

urlpatterns = [
    path('', views.board_list),
    path('board_create/', views.board_create),
    path('<int:board_pk>/', views.board_detail),
    path('board_update_delete/<int:board_pk>/', views.board_update_delete),
    
    path('<int:board_pk>/comments', views.comment_list),
    path('<int:board_pk>/comment_create/', views.comment_create),
    path('<int:board_pk>/comment/<int:comment_pk>/', views.comment_update_delete),
]
