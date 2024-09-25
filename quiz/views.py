from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from medium.models import ResultMedium
from easy.models import ResultEasy
from hard.models import ResultHard

@login_required
def home_view(request):
  results_easy = ResultEasy.objects.filter(score=100).order_by('-created')[:3]
  results_medium = ResultMedium.objects.filter(score=100).order_by('-created')[:3]
  results_hard = ResultHard.objects.filter(score=100).order_by('-created')[:3]

  context = {
  'results_easy' : results_easy,
  'results_medium' : results_medium,
  'results_hard' : results_hard,
      
  }
  return render(request, 'quiz/home.html', context)

@login_required
def result_all(request):    
  return render(request, 'quiz/result_all.html')

@login_required
def result_all_easy(request):  
  results_easy = ResultEasy.objects.order_by('-created')
  

  context = {
     'results_easy': results_easy,     
  }
  return render(request, 'results/all/easy.html', context)

@login_required
def result_all_medium(request):  
  results_medium = ResultMedium.objects.order_by('-created') 

  context = {
     'results_medium': results_medium,     
  }
  return render(request, 'results/all/medium.html', context)

@login_required
def result_all_hard(request):  
  results_hard = ResultHard.objects.order_by('-created') 

  context = {
     'results_hard': results_hard,     
  }
  return render(request, 'results/all/hard.html', context)


   

def delete_results_all(request):
  if request.method == 'POST':
      ResultMedium.objects.all().delete() 
      ResultEasy.objects.all().delete() 
      return redirect('result-all') 

  return render(request, 'results/quiz/delete_all_confirm.html') 


def delete_results_easy(request):
  if request.method == 'POST':     
      ResultEasy.objects.all().delete() 
      return redirect('result-all-easy') 

  return render(request, 'results/all/easy_delete_confirm.html') 

def delete_results_medium(request):
  if request.method == 'POST':     
      ResultMedium.objects.all().delete() 
      return redirect('result-all-medium') 

  return render(request, 'results/all/medium_delete_confirm.html') 

def delete_results_hard(request):
  if request.method == 'POST':     
      ResultHard.objects.all().delete() 
      return redirect('result-all-hard') 

  return render(request, 'results/all/hard_delete_confirm.html') 


