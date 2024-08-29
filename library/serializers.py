from rest_framework import serializers
from .models import Author, Book, Member, Borrow, Event, Posts, Category, Library, Review, AuthorDetail, EventParticipant, TemporaryPermission

class LibraryAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class LibraryBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LibraryMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class LibraryBorrowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrow
        fields = '__all__'

class LibraryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class LibraryPostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = '__all__'

class LibraryCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class LibraryLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = '__all__'

class LibraryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class LibraryAuthorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorDetail
        fields = '__all__'

class LibraryEventParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventParticipant
        fields = '__all__'

class LibraryTemporaryPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TemporaryPermission
        fields = ['id', 'user', 'permission', 'start_time', 'end_time']