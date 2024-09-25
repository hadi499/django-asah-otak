from django.db import models
from django.contrib.auth.models import User
import random


class Hard(models.Model):
  name = models.CharField(max_length=120)
  topic = models.CharField(max_length=120)
  number_of_questions = models.IntegerField()
  time = models.IntegerField(help_text="time in second")
  required_score_to_pass = models.IntegerField()
 

  def __str__(self):
    return f'{self.name} - {self.topic}' 
  
  def get_questions(self):
    questions = list(self.questionhard_set.all())
    random.shuffle(questions)
    return questions[:self.number_of_questions]
  

class QuestionHard(models.Model):
  text = models.CharField(max_length=200)
  quiz = models.ForeignKey(Hard, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.text)
  
  def get_answers(self):
    return self.answerhard_set.all()
  
class AnswerHard(models.Model):
  text = models.CharField(max_length=200)
  correct = models.BooleanField(default=False)
  question = models.ForeignKey(QuestionHard, on_delete=models.CASCADE)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'question: {self.question.text}, answer: {self.text} correct: {self.correct}'
  

class ResultHard(models.Model):
  quiz = models.ForeignKey(Hard, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return str(self.pk)