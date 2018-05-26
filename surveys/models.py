from django.db import models

# Create your models here.

class survey(models.Model):
	title = models.CharField(max_length = 300)
	Catagories = models.CharField(max_length = 100)
	Date_Needed = models.DateTimeField('Date Needed')

class Question(models.Model):
	Survey = models.ForeignKey(survey, on_delete=models.CASCADE)
	Question_Text = models.CharField(max_length=2000)
	Question_Weight = models.IntegerField(default = 0)

class Option(models.Model):
	Question = models.ForeignKey(Question, on_delete=models.CASCADE)
	Option_Text = models.CharField(max_length=1000)
	Option_Value = models.IntegerField(default=0)

