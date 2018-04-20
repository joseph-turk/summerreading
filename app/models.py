import uuid
from django.db import models
from django.core.validators import RegexValidator
from datetime import date
from time import time
from phonenumber_field.modelfields import PhoneNumberField


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
        return self.date < date.today()

    @property
    def slots_left(self):
        slots = self.capacity - self.registration_set.count()
        if slots < 0:
            return 0
        else:
            return slots

    @property
    def slots_filled(self):
        slots = self.registration_set.count()
        if slots > self.capacity:
            return self.capacity
        else:
            return slots

    @property
    def num_wait_list(self):
        num = self.registration_set.count() - self.capacity
        if num < 0:
            return 0
        else:
            return num

    def __str__(self):
        return self.name


class Adult(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12)
    photo_release = models.BooleanField()

    @property
    def confirmation_number(self):
        return str(self.id)[:8]

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
        return self.program.name + ' Registration for ' + self.child.name
