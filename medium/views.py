from django.shortcuts import render, redirect
from .models import Medium
from django.http import JsonResponse
from django.views.generic import ListView
from .models import QuestionMedium, AnswerMedium
from .models import ResultMedium
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin




def main_medium_view(request):
  medium_quiz = Medium.objects.all()
  user_id = request.user.id 
  results = ResultMedium.objects.filter(user_id=user_id).order_by('-score')[:10]
  
  context = {
    'medium_quiz' : medium_quiz,
    'results' : results,
  }

  return render(request, 'medium/main.html', context)

@login_required
def medium_view(request,pk):
  quiz = Medium.objects.get(pk=pk)
  # print(quiz)
  return render(request, 'medium/quiz.html', {'obj': quiz})

def medium_data_view(request, pk):
  quiz = Medium.objects.get(pk=pk)
  questions = []

  for q in quiz.get_questions():
    answers = []
    for a in q.get_answers():
      answers.append(a.text)
    questions.append({str(q): answers})
  return JsonResponse({
    'data' :questions,
    'time': quiz.time,
  })

def save_medium_view(request, pk):
  if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    questions = []
    data = request.POST
    data_ = dict(data.lists())

    data_.pop('csrfmiddlewaretoken')

    for k in data_.keys():
      # print('key: ', k)   
      question = QuestionMedium.objects.get(text=k)
      questions.append(question)
    # print(questions)

    user = request.user
    quiz = Medium.objects.get(pk=pk)

    score = 0
    mutiplier = 100 / quiz.number_of_questions
    results = []
    correct_answer = None

    for q in questions:
      a_selected = request.POST.get(q.text)

      if a_selected != "":
        question_answers = AnswerMedium.objects.filter(question=q)
        for a in question_answers:
          if a_selected == a.text:
            if a.correct:
              score += 1
              correct_answer = a.text
          else:
            if a.correct:
              correct_answer = a.text
        results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
      else:
        results.append({str(q): 'not answered'})
    score_ = score * mutiplier
    ResultMedium.objects.create(quiz=quiz, user=user, score=score_)

    if score_ >= quiz.required_score_to_pass:
      return JsonResponse({'passed': True, 'score': score_, 'results': results})
    else:
      return JsonResponse({'passed': False, 'score': score_, 'results': results})
    
@login_required
def result_medium(request):  
  user_id = request.user.id  
  results = ResultMedium.objects.filter(user_id=user_id).order_by('-score')   
  return render(request, 'medium/results.html', {'results': results})

def delete_results_medium(request):
  if request.method == 'POST':
      ResultMedium.objects.all().delete() 
      return redirect('result-medium-view') 

  return render(request, 'results/medium/delete_all_confirm.html') 


