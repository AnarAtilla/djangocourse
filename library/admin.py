from django.contrib import admin

from .models import (Author, Category, Library, Member, Posts, Borrow, Review, AuthorDetail, Event,
                     EventParticipant)
from .models import Book


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date', 'rating')
    search_fields = ('first_name', 'last_name')
    list_filter = ('rating',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publishing_date', 'genre', 'page_count')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('genre', 'publishing_date')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'role', 'active')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('role', 'active')


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'library', 'created_at')
    search_fields = ('title', 'author__first_name', 'author__last_name')
    list_filter = ('library', 'created_at')


@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):
    list_display = ('member', 'book', 'library', 'borrow_date', 'return_date', 'returned')
    search_fields = ('member__first_name', 'member__last_name', 'book__title')
    list_filter = ('library', 'returned')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'reviewer', 'rating')
    search_fields = ('book__title', 'reviewer__first_name', 'reviewer__last_name')
    list_filter = ('rating',)


@admin.register(AuthorDetail)
class AuthorDetailAdmin(admin.ModelAdmin):
    list_display = ('author', 'birth_city', 'gender')
    search_fields = ('author__first_name', 'author__last_name', 'birth_city')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'library')
    search_fields = ('title', 'library__name')
    list_filter = ('library', 'date')


@admin.register(EventParticipant)
class EventParticipantAdmin(admin.ModelAdmin):
    list_display = ('event', 'member', 'registration_date')
    search_fields = ('event__title', 'member__first_name', 'member__last_name')
    list_filter = ('event', 'registration_date')
