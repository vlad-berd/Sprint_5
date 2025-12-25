from faker import Faker


fake_data = Faker('en_US')

def generate_registration_data():
    name = fake_data.first_name()

    name_email = name.lower()
    surname = fake_data.last_name().lower()
    number_group = 36
    three_digits = fake_data.random_int(min=100, max=999)
    domen = fake_data.free_email_domain()
    email = f"{name_email}{surname}{number_group}{three_digits}@{domen}"
    
    password = fake_data.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)

    return name, email, password
