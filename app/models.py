from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    capacity = models.IntegerField()
    is_full = models.BooleanField()

    def __str__(self):
        return self.name


class Adult(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
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
