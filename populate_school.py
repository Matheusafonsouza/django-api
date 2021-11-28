
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

if __name__ == '__main__':
    import random
    import datetime
    from school.models import Student, Course, Enrolment
    from validate_docbr import CPF
    from faker import Faker

    fake = Faker('pt_BR')
    Faker.seed(10)

    # create students
    for _ in range(200):
        cpf = CPF().generate()
        name = fake.name()
        rg = f'{random.randrange(10,99)}{random.randrange(100,999)}' + \
            f'{random.randrange(100,999)}{random.randrange(0, 9)}'
        birth_date = fake.date_between(start_date='-18y', end_date='today')
        Student.objects.create(
            name=name,
            rg=rg,
            cpf=cpf,
            birth_date=birth_date
        )

    # create courses
    description_list = [
        'python fundamentos',
        'python intermediario',
        'python avançado',
        'python data science',
        'python react'
    ]
    for _ in range(5):
        init_code = random.choice('ABCDEF')
        code = f'{init_code}{random.randrange(10,99)}-' + \
            f'{random.randrange(1,9)}'
        description = random.choice(description_list)
        description_list.remove(description)
        level = random.choice(['EASY', 'MEDIUM', 'HARD'])
        Course.objects.create(
            description=description,
            level=level,
            code=code
        )
