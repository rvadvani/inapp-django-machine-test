import csv
from api.models import Movie
from django.core.management.base import BaseCommand

# python3 manage.py import_movie_titles
class Command(BaseCommand):
    help = 'Importing movie titles ...'
    def handle(self, *args, **kwargs):
        
        with open('/home/vikramaditya/Downloads/title.basics.tsv', 'r', encoding='utf-8') as movies_file:
            reader = csv.DictReader(movies_file, delimiter='\t')
            for row in reader:
                movie = Movie(
                    tconst=row['tconst'],
                    title_type=row['titleType'],
                    primary_title=row['primaryTitle'],
                    original_title=row['originalTitle'],
                    is_adult=row['isAdult'] == 'TRUE',
                    start_year=int(row['startYear']) if row['startYear'] and row['startYear'] != '\\N' else None,
                    end_year=int(row['endYear']) if row['endYear'] and row['endYear'] != '\\N' else None,
                    runtime_minutes=int(row['runtimeMinutes']) if row['runtimeMinutes'] and row['runtimeMinutes'] != '\\N' else None,
                    genres=row['genres']
                )
                movie.save()
                self.stdout.write(self.style.SUCCESS(f'Imported tconst: {movie.tconst} and primary_title: {movie.primary_title}'))
        self.stdout.write(self.style.SUCCESS('All the titles imported successfully!'))