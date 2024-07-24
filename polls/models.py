
# Create your models here.
from django.db import models


class Question(models.Model):
    def __str__(self):
      self.question_text = models.CharField(max_length=200)
      self.pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    def __str__(self):
        self.question = models.ForeignKey(Question, on_delete=models.CASCADE)
        self.choice_text = models.CharField(max_length=200)
        self.votes = models.IntegerField(default=0)