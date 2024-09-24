from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medium.models import ResultMedium
from easy.models import ResultEasy

@login_required
def home_view(request):
  results_easy = ResultEasy.objects.filter(score=100).order_by('-created')[:5]
  results_medium = ResultMedium.objects.filter(score=100).order_by('-created')[:5]

  context = {
  'results_easy' : results_easy,
  'results_medium' : results_medium,
      
  }
  return render(request, 'quiz/home.html', context)

@login_required
def result_all(request):  
  results_easy = ResultEasy.objects.order_by('-created')
  results_medium = ResultMedium.objects.order_by('-created')

  context = {
     'results_easy': results_easy,
     'results_medium': results_medium,
  }
  return render(request, 'quiz/result_all.html', context)

def delete_results_all(request):
  if request.method == 'POST':
      ResultMedium.objects.all().delete() 
      ResultEasy.objects.all().delete() 
      return redirect('result-all') 

  return render(request, 'results/quiz/delete_all_confirm.html') 


