from django.contrib.auth.models import User
from django.db import models

answers_choice = (
    ('1', "option1"),
    ('2', "option2"),
    ('3', "option3"),
    ('4', "option4"),

)


class subject(models.Model):
    subject = models.CharField(max_length=20)

    def __str__(self):
        return self.subject


class Exam(models.Model):
    teacher = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    Subject = models.ForeignKey(subject, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.Subject.subject


class Question(models.Model):
    category = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='Question')
    description = models.CharField(max_length=100)
    optiion1 = models.CharField(max_length=500)
    optiion2 = models.CharField(max_length=500)
    optiion3 = models.CharField(max_length=500)
    optiion4 = models.CharField(max_length=500)

    def __str__(self):
        return self.description


class Answer(models.Model):
    question = models.OneToOneField(
        Question, on_delete=models.CASCADE, primary_key=True)
    Answer = models.CharField(max_length=3000)

    def __str__(self):
        return self.question.description


class QuizTaker(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    correct_answers = models.IntegerField(default=0)


class Assign(models.Model):
    Student = models.ForeignKey(User, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
