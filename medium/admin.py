from django.contrib import admin
from .models import Medium, QuestionMedium, AnswerMedium, ResultMedium

class AnswerMediumInline(admin.TabularInline):
  model = AnswerMedium

class QuestionMediumAdmin(admin.ModelAdmin):
  inlines = [AnswerMediumInline]

admin.site.register(QuestionMedium, QuestionMediumAdmin)
admin.site.register(AnswerMedium)
admin.site.register(Medium)
admin.site.register(ResultMedium)
