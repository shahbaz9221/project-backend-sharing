from django.db import models
from userregistration.models import UserRegistration
from django.contrib.auth.models import User
# Create your models here.

class Questionnaire(models.Model):
    questions = models.CharField(max_length=1000)
    time = models.IntegerField()

    def __str__(self):
        return f"{self.questions} | {self.time}"
    
    class Meta:
        verbose_name_plural = 'Questionnaire'


class UserQuestionnaire(models.Model):
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    recording = models.FileField()

    def __str__(self):
        return f"{self.user} | {self.questionnaire} | {self.recording}"
    
    class Meta:
        verbose_name_plural = 'User Questionnaire'



