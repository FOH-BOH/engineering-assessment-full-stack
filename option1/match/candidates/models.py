from django.db import models


class Candidate(models.Model):

    CITY_CHOICES = (
        ('mtjuliet', 'Mt. Juliet',),
        ('murfreesboro', 'Murfreesboro',),
        ('nashville', 'Nashville',),
    )

    POSITION_CHOICES = (
        ('bartender', 'Bartender',),
        ('manager', 'Manager',),
        ('server', 'Server',),
    )

    name = models.CharField(max_length=100, help_text='First and last name of candidate')
    city = models.CharField(max_length=100, choices=CITY_CHOICES, help_text='The city where the candidate lives')
    positions = models.CharField(max_length=200, help_text='Tab-delimited list of position types that a candidate is seeking')