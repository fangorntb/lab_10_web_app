from django.urls import path

from vacancies import views

urlpatterns = [
    path('hello/', views.Hello.as_view(), name='get hello')
]
