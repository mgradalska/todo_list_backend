from django.db import models


class Board(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    STATUS_CHOICES = [
        ('TODO', "TODO"),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('DONE', 'DONE')
    ]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='tasks')
