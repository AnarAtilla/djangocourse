# library/views.py
from rest_framework import viewsets
from .models import Author, Book, Member, Borrow, Event, Posts, Category, Library, Review, AuthorDetail, EventParticipant
from .serializers import (
    AuthorSerializer, BookSerializer, MemberSerializer, BorrowSerializer, EventSerializer, PostsSerializer,
    CategorySerializer, LibrarySerializer, ReviewSerializer, AuthorDetailSerializer, EventParticipantSerializer
)
from django.shortcuts import render

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class AuthorDetailViewSet(viewsets.ModelViewSet):
    queryset = AuthorDetail.objects.all()
    serializer_class = AuthorDetailSerializer

class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all()
    serializer_class = EventParticipantSerializer

def home(request):
    return render(request, 'library/home.html')