from django.urls import path
from .views import CreateAccountView
from .views import UserAccountView
from .views import AuthorView

app_name = 'users'

urlpatterns = [
    path('create-account/',
    CreateAccountView.as_view(),
    name ='createAccount'
    ),
    path('<int:pk>/',
    UserAccountView.as_view(),
    name='viewAccount'),
    path('<str:username>', AuthorView.as_view(), name='viewAuthor')
]