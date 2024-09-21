from django.contrib import admin
from .models import Easy, QuestionEasy, AnswerEasy, ResultEasy

class AnswerEasyInline(admin.TabularInline):
  model = AnswerEasy

class QuestionEasyAdmin(admin.ModelAdmin):
  inlines = [AnswerEasyInline]

admin.site.register(QuestionEasy, QuestionEasyAdmin)
admin.site.register(AnswerEasy)
admin.site.register(Easy)
admin.site.register(ResultEasy)
