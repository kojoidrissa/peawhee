from peewee import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


# interactive examples
grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

# creating pets for people
>>> bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
>>> herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
>>> herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
>>> herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

>>> herb_mittens.delete_instance() # he had a great life
