
from django.urls import path
from .views import booklist,book_detail
urlpatterns = [
    path('books/', booklist, name='booklist'),
    path('book/<int:id>', book_detail, name='book_detail')
   ]