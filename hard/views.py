from django.shortcuts import render, redirect
from .models import Hard
from django.http import JsonResponse

from .models import QuestionHard, AnswerHard
from .models import ResultHard
from django.contrib.auth.decorators import login_required






def main_hard_view(request):
  hard_quiz = Hard.objects.all()
  user_id = request.user.id 
  results = ResultHard.objects.filter(user_id=user_id).order_by('-score')[:10]
  
  context = {
    'hard_quiz' : hard_quiz,
    'results' : results,
  }

  return render(request, 'hard/main.html', context)

@login_required
def hard_view(request,pk):
  quiz = Hard.objects.get(pk=pk)
  # print(quiz)
  return render(request, 'hard/quiz.html', {'obj': quiz})

def hard_data_view(request, pk):
  quiz = Hard.objects.get(pk=pk)
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

def save_hard_view(request, pk):
  if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
    questions = []
    data = request.POST
    data_ = dict(data.lists())

    data_.pop('csrfmiddlewaretoken')

    for k in data_.keys():
      # print('key: ', k)   
      question = QuestionHard.objects.get(text=k)
      questions.append(question)
    # print(questions)

    user = request.user
    quiz = Hard.objects.get(pk=pk)

    score = 0
    mutiplier = 100 / quiz.number_of_questions
    results = []
    correct_answer = None

    for q in questions:
      a_selected = request.POST.get(q.text)

      if a_selected != "":
        question_answers = AnswerHard.objects.filter(question=q)
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
    ResultHard.objects.create(quiz=quiz, user=user, score=score_)

    if score_ >= quiz.required_score_to_pass:
      return JsonResponse({'passed': True, 'score': score_, 'results': results})
    else:
      return JsonResponse({'passed': False, 'score': score_, 'results': results})
    
@login_required
def result_hard(request):  
  user_id = request.user.id  
  results = ResultHard.objects.filter(user_id=user_id).order_by('-score')   
  return render(request, 'hard/results.html', {'results': results})

def delete_results_hard(request):
  if request.method == 'POST':
      ResultHard.objects.all().delete() 
      return redirect('result-hard-view') 

  return render(request, 'results/hard/delete_all_confirm.html') 


