"""
Run below two commands in shell -

from scripts.populate_data import populate_data 
populate_data(100, 200, 30)

"""

import random
from string import ascii_uppercase
from account.logic.service import svc_register_user
from contacts.logic.service import svc_create_contact, svc_mark_phone_spam

names = [
    "Blakely Vaughan",
    "Castiel Crosby",
    "Keily Vaughn",
    "Remy Jensen",
    "Jane Wilkinson",
    "Leonard McDaniel",
    "Dahlia Morgan",
    "Hunter Meadows",
    "Pearl OConnor",
    "Princeton Frazier",
    "Octavia Page",
    "Pablo Logan",
    "Kora Collins",
    "Miles Weiss",
    "Lennox Dickerson",
    "Flynn Dejesus",
    "Julissa Strickland",
    "Keegan Bradshaw",
    "Berkley Brady",
    "Reed Fischer",
    "Maci Romero",
    "Bryson Lang",
    "Amirah Price",
    "Brooks McKee",
    "Kori Quintana",
    "Kelvin Reyes",
    "Audrey Luna",
    "Erick Hansen",
    "Hope Griffin",
    "Ayden James",
    "Quinn Hart",
    "Joel Roach",
    "Lyanna Griffith",
]


def _get_random_name():
    return random.choice(names)


def _get_random_phone():
    return random.randint(1000000000, 9999999999)


def _get_random_email():
    return "".join(random.choice(ascii_uppercase) for i in range(5)) + "@gmail.com"


def _get_random_password():
    return "".join(random.choice(ascii_uppercase) for i in range(8))


def _create_random_users(number_of_users: int):
    users = []
    for i in range(number_of_users):
        error, user = svc_register_user(
            {
                "name": _get_random_name(),
                "phone": str(_get_random_phone()),
                "email": _get_random_email(),
                "password": _get_random_password(),
            }
        )
        if not error:
            users.append(user)
    return users


def _create_random_contacts(number_of_contacts: int, users: list):
    contacts = []
    for i in range(number_of_contacts):
        contact = svc_create_contact(
            name=_get_random_name(),
            phone=_get_random_phone(),
            email=_get_random_email(),
            owner=random.choice(users),
        )
        contacts.append(contact)
    # TODO: create more contacts with different cases like -
    # same phone multiple names, same name multiple phones, etc
    return contacts


def populate_data(number_of_users: int, number_of_contacts: int, number_of_spams: int):
    users = _create_random_users(number_of_users)
    print(f"{len(users)} users created successfully")

    contacts = _create_random_contacts(number_of_contacts, users)
    print(f"{len(contacts)} contacts created successfully")

    # marking some existing phone numbers spam
    for contact in contacts[:number_of_spams]:
        svc_mark_phone_spam(phone=contact.phone, spammed_by=random.choice(users))

    return "script ran successfully!"
