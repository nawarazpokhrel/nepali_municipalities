import uuid

from django.db import models


# Create your models here.
class Province(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    country = models.CharField(default='Nepal',max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Municipalities(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    district = models.ForeignKey(to=District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
