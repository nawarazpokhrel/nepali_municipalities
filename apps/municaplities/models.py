import uuid

from django.db import models


# Create your models here.
class Province(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    country = models.CharField(default='Nepal',max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Municipalities(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    district = models.ForeignKey(to=District, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
