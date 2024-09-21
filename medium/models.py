from django.db import models
from django.contrib.auth.models import User
import random


class Medium(models.Model):
  name = models.CharField(max_length=120)
  topic = models.CharField(max_length=120)
  number_of_questions = models.IntegerField()
  time = models.IntegerField(help_text="time in second")
  required_score_to_pass = models.IntegerField()
 

  def __str__(self):
    return f'{self.name} - {self.topic}' 
  
  def get_questions(self):
    questions = list(self.questionmedium_set.all())
    random.shuffle(questions)
    return questions[:self.number_of_questions]
  

class QuestionMedium(models.Model):
  text = models.CharField(max_length=200)
  quiz = models.ForeignKey(Medium, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.text)
  
  def get_answers(self):
    return self.answermedium_set.all()
  
class AnswerMedium(models.Model):
  text = models.CharField(max_length=200)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(QuestionMedium, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'question: {self.question.text}, answer: {self.text} correct: {self.correct}'
  

class ResultMedium(models.Model):
  quiz = models.ForeignKey(Medium, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.pk)