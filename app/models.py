from django.db import models
from django.core.validators import RegexValidator
from datetime import date


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    capacity = models.IntegerField()
    is_teen = models.BooleanField(default=False)
    graphic = models.ImageField(upload_to='graphics', default='graphic.jpg')
    is_full = models.BooleanField()

    @property
    def is_past(self):
        return False

    @property
    def slots_left(self):
        slots = self.capacity - self.registration_set.count()
        if slots < 0:
            return 0
        else:
            return slots

    def __str__(self):
        return self.name


class Adult(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_regex = RegexValidator(
        regex=r'^d{3}\-?d{3}-?d{4}$',
        message='Phone number must be in the format \'123-456-7890\'.')
    phone = models.CharField(
        validators=[phone_regex],
        max_length=12)
    notify = models.BooleanField()

    def __str__(self):
        return self.name


class Child(models.Model):
    name = models.CharField(max_length=100)
    adult = models.ForeignKey(Adult, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Registration(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    is_wait_list = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.program} Registration for {self.child}'
