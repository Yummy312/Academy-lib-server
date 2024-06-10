from django.shortcuts import get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CategorySerializer, BookSerializer
from .models import Book, Category
from rest_framework import filters


@api_view(['GET'])
def get_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer = CategorySerializer(category)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    book.view_count += 1
    book.save()
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_list_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_related_books(request, pk):
    category = get_object_or_404(Category, pk=pk)
    books = category.books.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_recently_viewed(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    recently_viewed = request.session.get('recently_viewed', [])
    if book_id not in recently_viewed:
        recently_viewed.append(book_id)
    request.session['recently_viewed'] = recently_viewed
    serializer = BookSerializer(book)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_recently_viewed(request):
    recently_viewed_ids = request.session.get('recently_viewed', [])
    recently_viewed_books = Book.objects.filter(pk__in=recently_viewed_ids)
    serializer = BookSerializer(recently_viewed_books, many=True)
    return Response(serializer.data)


class FilterBookByTitle (generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def get_queryset(self):
        title = self.request.query_params.get('title')
        if title:
            return Book.objects.filter(title=title)
        return Book.objects.all()
