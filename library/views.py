from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Author, Book, Member, Borrow, Event, Posts, Category, Library, Review, AuthorDetail, EventParticipant
from .serializers import (
    AuthorSerializer, BookSerializer, MemberSerializer, BorrowSerializer, EventSerializer, PostsSerializer,
    CategorySerializer, LibrarySerializer, ReviewSerializer, AuthorDetailSerializer, EventParticipantSerializer
)
from django.shortcuts import render

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = AuthorSerializer
    pagination_class = StandardResultsSetPagination

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = BookSerializer
    pagination_class = StandardResultsSetPagination

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = MemberSerializer
    pagination_class = StandardResultsSetPagination

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = BorrowSerializer
    pagination_class = StandardResultsSetPagination

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = EventSerializer
    pagination_class = StandardResultsSetPagination

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = PostsSerializer
    pagination_class = StandardResultsSetPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = LibrarySerializer
    pagination_class = StandardResultsSetPagination

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = ReviewSerializer
    pagination_class = StandardResultsSetPagination

class AuthorDetailViewSet(viewsets.ModelViewSet):
    queryset = AuthorDetail.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = AuthorDetailSerializer
    pagination_class = StandardResultsSetPagination

class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all().order_by('id')  # Упорядочивание по id
    serializer_class = EventParticipantSerializer
    pagination_class = StandardResultsSetPagination

def home(request):
    return render(request, 'library/home.html')