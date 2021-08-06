from django.urls import path

from . import views

app_name = 'question'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:question_id>/answer/', views.answer_create, name='answer_create'),
    path(
        '<int:question_id>/answer/<int:answer_id>/delete/',
        views.answer_delete,
        name='answer_delete'
    ),
]
