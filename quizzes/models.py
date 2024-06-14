from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return self.title
