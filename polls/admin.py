# _*_ coding:utf-8 _*_
from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('题目内容', {'fields': ['question_text']}),
        ('出题时间', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date')


admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)