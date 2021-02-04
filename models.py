from django.db import models

class Mcq_exam(models.Model):
    questions=models.CharField(max_length=100)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correctAnswer=models.CharField(max_length=100)
    class Meta:
        db_table="questions"