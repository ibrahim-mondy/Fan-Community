from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from Community.models import Movie, FootballTeam

class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **kwargs):
        # Create users
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write(self.style.SUCCESS('Admin user created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists'))

        if not User.objects.filter(username='member').exists():
            User.objects.create_user('member', password='member123')
            self.stdout.write(self.style.SUCCESS('Member user created (username: member, password: member123)'))
        else:
            self.stdout.write(self.style.WARNING('Member user already exists'))

        # Create movies
        Movie.objects.get_or_create(
            title="Se7en",
            genre="Thriller",
            description="A crime thriller about seven deadly sins.",
            release_date="1995-09-22"
        )
        Movie.objects.get_or_create(
            title="Shutter Island",
            genre="Mystery",
            description="A mystery thriller set on an isolated island.",
            release_date="2010-02-19"
        )

        # Create football teams
        FootballTeam.objects.get_or_create(
            name="Real Madrid",
            country="Spain",
            founded_year=1902
        )
        FootballTeam.objects.get_or_create(
            name="Al Ahly",
            country="Egypt",
            founded_year=1907
        )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
