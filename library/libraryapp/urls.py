from socket import fromfd


from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'library-home'),
    path('books/', views.show, name = 'library-books'),
    path('books/<int:id>', views.book, name = 'library-book'),
    path('books/new/', views.create, name = 'library-create'),
]
