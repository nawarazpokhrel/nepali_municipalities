import uuid

from django.db import models


# Create your models here.
from django_extensions.db.fields import ShortUUIDField


class Province(models.Model):
    # id = ShortUUIDField(
    #     primary_key=True,
    #     auto=True,
    #     editable=False,
    #     unique=True,
    # )
    country = models.CharField(default='Nepal',max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    # id = ShortUUIDField(
    #     primary_key=True,
    #     auto=True,
    #     editable=False,
    #     unique=True,
    # )
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Municipalities(models.Model):
    # id = ShortUUIDField(
    #     primary_key=True,
    #     auto=True,
    #     editable=False,
    #     unique=True,
    # )
    district = models.ForeignKey(to=District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
