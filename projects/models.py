from django.db import models
from employees.models import Employee


class Project(models.Model):

    STATUS_CHOICES = [
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    project_name = models.CharField(max_length=200)
    client_name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Not Started'
    )
    project_manager = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name='managed_projects'
    )
    employees = models.ManyToManyField(
        Employee,
        related_name='projects',
        blank=True
    )

    def __str__(self):
        return self.project_name