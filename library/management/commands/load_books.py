import os
import csv
from datetime import datetime

from django.core.management.base import BaseCommand
from library.models import Book, Author, Library, Category, Member


class Command(BaseCommand):
    help = 'Load books from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The CSV file to load books from')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        csv_file_path = os.path.join(base_dir, '..', '..', 'data', csv_file)

        with open(csv_file_path, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    book_title = row['title']
                    author_name = row['author'].split()  # Разделение имени и фамилии
                    first_name = author_name[0]
                    last_name = author_name[1] if len(author_name) > 1 else ''
                    library_names = row['libraries'].split(',') if row['libraries'] else []
                    publishing_date = datetime.strptime(row['publishing_date'], '%Y-%m-%d').date()
                    category_name = row['category']
                    publisher_name = row['publisher']
                    genre = row['genre']
                    page_count = int(row['page_count']) if row['page_count'] else None
                    birth_date = datetime.strptime(row['birth_date'], '%Y-%m-%d').date() if row['birth_date'] and row['birth_date'] != '***' else None

                    # Create or get the author
                    author, _ = Author.objects.get_or_create(
                        first_name=first_name,
                        last_name=last_name,
                        defaults={'birth_date': birth_date}
                    )

                    # Create or get the category
                    category, _ = Category.objects.get_or_create(name=category_name)

                    # Create or get the member (publisher)
                    member, created = Member.objects.get_or_create(
                        first_name=publisher_name.split()[0],
                        last_name=publisher_name.split()[1] if len(publisher_name.split()) > 1 else '',
                        role='Staff',
                        defaults={'birth_date': None, 'age': None,
                                  'email': f"{publisher_name.replace(' ', '_')}@example.com"}
                    )

                    if not created:
                        # Handle the case where the member already exists
                        member = Member.objects.get(
                            first_name=publisher_name.split()[0],
                            last_name=publisher_name.split()[1] if len(publisher_name.split()) > 1 else '',
                            role='Staff'
                        )

                    # Create or get the book
                    book, created = Book.objects.get_or_create(
                        title=book_title,
                        author=author,
                        publisher=member,
                        category=category,
                        publishing_date=publishing_date,
                        genre=genre,
                        page_count=page_count
                    )

                    # Add libraries to the book
                    for library_name in library_names:
                        library, _ = Library.objects.get_or_create(name=library_name.strip())
                        book.libraries.add(library)

                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded book "{book_title}"'))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f'Error loading book "{book_title}": {e}'))