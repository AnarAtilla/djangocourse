from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    AuthorViewSet, BookViewSet, MemberViewSet, BorrowViewSet, EventViewSet, PostsViewSet,
    CategoryViewSet, LibraryViewSet, ReviewViewSet, AuthorDetailViewSet, EventParticipantViewSet, home,
    TemporaryPermissionViewSet
)

router = DefaultRouter()
router.register(r'authors', AuthorViewSet, basename='author')
router.register(r'books', BookViewSet, basename='book')
router.register(r'members', MemberViewSet, basename='member')
router.register(r'borrows', BorrowViewSet, basename='borrow')
router.register(r'events', EventViewSet, basename='event')
router.register(r'posts', PostsViewSet, basename='posts')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'libraries', LibraryViewSet, basename='library')
router.register(r'reviews', ReviewViewSet, basename='review')
router.register(r'author-details', AuthorDetailViewSet, basename='author-detail')
router.register(r'event-participants', EventParticipantViewSet, basename='event-participant')
router.register(r'temporary-permissions', TemporaryPermissionViewSet, basename='temporary-permission')

urlpatterns = [
    path('', include(router.urls)),
    path('home/', home, name='library-home'),
]