from django.core.management.base import BaseCommand

from faker import Faker

from main.models import Student


class Command(BaseCommand):

    help = 'Add new student(s) to the system'

    def add_arguments(self, parser):

        parser.add_argument('-l', '--len', type=int, default=10)

    def handle(self, *args, **options):
        faker = Faker()
        self.stdout.write('Start inserting Students')
        for _ in range(options['len']):
            self.stdout.write('Start inserting Students')
            student = Student()
            student.name = faker.first_name()
            student.surname = faker.last_name()
            student.sex = (faker.simple_profile()).get('sex')
            student.address = faker.street_address()
            student.description = faker.text()
            student.birthday = faker.date_of_birth()
            student.email = faker.company_email()
            student.save()
        self.stdout.write('End inserting Students')
