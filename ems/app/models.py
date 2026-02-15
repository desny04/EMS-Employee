from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    phone = models.IntegerField()
    department = models.TextField()
    designation = models.TextField()

    def __str__(self):
        return self.user.username

class Work(models.Model):

    STATUS_CHOICES = [
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('On Testing', 'On Testing'),
        ('Done', 'Done'),
    ]

    title = models.TextField()
    description = models.TextField()
    assigned_date = models.DateField()
    deadline = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='To Do'
    )

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
