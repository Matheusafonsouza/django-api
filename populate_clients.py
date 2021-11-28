
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

if __name__ == '__main__':
    import random
    from client.models import Client
    from validate_docbr import CPF
    from faker import Faker

    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(50):
        cpf = CPF().generate()
        name = fake.name()
        email = f'{name.lower()}@{fake.free_email_domain()}'
        rg = f'{random.randrange(10,99)}{random.randrange(100,999)}' + \
            f'{random.randrange(100,999)}{random.randrange(0, 9)}'
        phone = f'{random.randrange(10,21)} 9{random.randrange(4000,9999)}' + \
            f'-{random.randrange(4000,9999)}'
        active = random.choice([True, False])
        Client.objects.create(
            name=name,
            email=email,
            rg=rg,
            cpf=cpf,
            phone=phone,
            active=active
        )
