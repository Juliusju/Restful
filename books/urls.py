from django.urls import path
from .views import home, BookListView


urlpatterns = [
    path('home',home, name="home"),
    path('', BookListView.as_view(), name = 'books'),
]
