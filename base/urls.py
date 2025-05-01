from django.urls import path
from base import views
urlpatterns = [
    path('books/', views.get_books, name="books"),
    path('books/<int:id>/', views.get_book, name="book")
]