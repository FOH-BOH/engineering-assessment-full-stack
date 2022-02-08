from django.db import models

from candidates.models import Candidate


class Position(models.Model):
    name = models.CharField(max_length=100, help_text='The name of the position and establishment')
    matching_positions = models.CharField(max_length=100, help_text='Tab-delimited list of positions to match candidates')
    city = models.CharField(max_length=100, choices=Candidate.CITY_CHOICES)
