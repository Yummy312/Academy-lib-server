from django.urls import path
from book import views
from book.views import FilterBookByTitle

urlpatterns = [
    path('categories/', views.get_list_categories, name='categories-list'),
    path('books/', views.get_list_books, name='books-list'),
    path('categories/<int:pk>/', views.get_category, name='category-detail'),
    path('books/<int:pk>/', views.get_book, name='book-detail'),
    path('related-books/<int:pk>/', views.get_related_books, name='related-books'),
    path('add_recently_viewed/<int:book_id>', views.add_recently_viewed, name='add-recently-viewed'),
    path('get_recently_viewed/', views.get_recently_viewed),
    path('books/filter/', FilterBookByTitle.as_view(), name='books-filter'),

]


