from django.db import models


# Create your models here.
class Province(models.Model):
    country = models.CharField(default='Nepal',max_length=10)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class District(models.Model):
    province = models.ForeignKey(to=Province, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Municipalities(models.Model):
    district = models.ForeignKey(to=District, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
