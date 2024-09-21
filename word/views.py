from django.shortcuts import render

def buka_word(request):
  return render(request, 'word/buka.html')
