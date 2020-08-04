from django.db import models


# Create your models here.
class Employee(models.Model):

    def __str__(self):
        return f"{self.surname} {self.name} {self.patronymic}"

    citizenship_choices = [
        ("ru", "Россия"),
        ("us", "Америка")
    ]

    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    age = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    citizenship = models.CharField(max_length=50, choices=citizenship_choices)
    description = models.CharField(max_length=300)
    work_schedule = models.CharField(max_length=300)
    skills = models.CharField(max_length=1000)
    hobbies = models.CharField(max_length=1000)
    personal_qualities = models.CharField(max_length=1000)
    additional_training = models.CharField(max_length=1000)



