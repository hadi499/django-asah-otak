from django.contrib import admin
from .models import Hard, QuestionHard, AnswerHard, ResultHard

class AnswerHardInline(admin.TabularInline):
  model = AnswerHard

class QuestionHardAdmin(admin.ModelAdmin):
  inlines = [AnswerHardInline]

admin.site.register(QuestionHard, QuestionHardAdmin)
admin.site.register(AnswerHard)
admin.site.register(Hard)
admin.site.register(ResultHard)