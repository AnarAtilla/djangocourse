from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Author, Member, Borrow, Event, Posts, Category, Library, Review, AuthorDetail, EventParticipant, Book
from .models import TemporaryPermission
from .permissions import HasTemporaryPermission
from .serializers import (
    LibraryAuthorSerializer, LibraryMemberSerializer, LibraryBorrowSerializer, LibraryEventSerializer, LibraryPostsSerializer,
    LibraryCategorySerializer, LibraryLibrarySerializer, LibraryReviewSerializer, LibraryAuthorDetailSerializer, LibraryEventParticipantSerializer,
    LibraryBookSerializer, LibraryTemporaryPermissionSerializer
)

class TemporaryPermissionViewSet(viewsets.ModelViewSet):
    queryset = TemporaryPermission.objects.all()
    serializer_class = LibraryTemporaryPermissionSerializer

def home(request):
    return render(request, 'library/home.html')

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by('id')
    serializer_class = LibraryAuthorSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of authors")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new author")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific author")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific author")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific author")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific author")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = LibraryBookSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser | HasTemporaryPermission]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @swagger_auto_schema(operation_description="Retrieve a list of books")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new book")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific book")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific book")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific book")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific book")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('id')
    serializer_class = LibraryMemberSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of members")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new member")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific member")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific member")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific member")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific member")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class BorrowViewSet(viewsets.ModelViewSet):
    queryset = Borrow.objects.all().order_by('id')
    serializer_class = LibraryBorrowSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of borrows")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new borrow")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific borrow")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific borrow")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific borrow")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific borrow")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('id')
    serializer_class = LibraryEventSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of events")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new event")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific event")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific event")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific event")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific event")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all().order_by('id')
    serializer_class = LibraryPostsSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of posts")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new post")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific post")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific post")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific post")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific post")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')
    serializer_class = LibraryCategorySerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of categories")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new category")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific category")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific category")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific category")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific category")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class LibraryViewSet(viewsets.ModelViewSet):
    queryset = Library.objects.all().order_by('id')
    serializer_class = LibraryLibrarySerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of libraries")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new library")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific library")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific library")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific library")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific library")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all().order_by('id')
    serializer_class = LibraryReviewSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of reviews")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new review")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific review")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific review")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific review")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific review")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class AuthorDetailViewSet(viewsets.ModelViewSet):
    queryset = AuthorDetail.objects.all().order_by('id')
    serializer_class = LibraryAuthorDetailSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of author details")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new author detail")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific author detail")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific author detail")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific author detail")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific author detail")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

class EventParticipantViewSet(viewsets.ModelViewSet):
    queryset = EventParticipant.objects.all().order_by('id')
    serializer_class = LibraryEventParticipantSerializer
    pagination_class = StandardResultsSetPagination

    @swagger_auto_schema(operation_description="Retrieve a list of event participants")
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new event participant")
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Retrieve a specific event participant")
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Update a specific event participant")
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Partial update a specific event participant")
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Delete a specific event participant")
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)