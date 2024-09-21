from django.db import models
from django.contrib.auth.models import User


class Easy(models.Model):
  name = models.CharField(max_length=120)
  topic = models.CharField(max_length=120)
  number_of_questions = models.IntegerField()
  time = models.IntegerField()
  required_score_to_pass = models.IntegerField()
 

  def __str__(self):
    return f'{self.name} - {self.topic}' 
  
  def get_questions(self):
    return self.questioneasy_set.all() [:self.number_of_questions]
  

class QuestionEasy(models.Model):
  text = models.CharField(max_length=200)
  quiz = models.ForeignKey(Easy, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.text)
  
  def get_answers(self):
    return self.answereasy_set.all()
  
class AnswerEasy(models.Model):
  text = models.CharField(max_length=200)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(QuestionEasy, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'question: {self.question.text}, answer: {self.text} correct: {self.correct}'
  

class ResultEasy(models.Model):
  quiz = models.ForeignKey(Easy, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.pk)