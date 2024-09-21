from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from medium.models import ResultMedium
from easy.models import ResultEasy

@login_required
def home_view(request):
  return render(request, 'quiz/home.html')

@login_required
def results_view(request):
    if request.method == 'POST' and 'delete_all' in request.POST:
        ResultEasy.objects.all().delete() 
        ResultMedium.objects.all().delete()        
        return render(request, 'results/delete_all_confirm.html')
    context = {
    'results_easy' : ResultEasy.objects.all().order_by('-score'), 
    'results_medium' : ResultMedium.objects.all().order_by('-score')  
       
    }
    return render(request, 'results/list.html', context)

