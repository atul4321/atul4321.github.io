from django.contrib import admin
from .models import Exam, Question, QuizTaker, Answer
from import_export.admin import ImportExportModelAdmin


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass


@admin.register(QuizTaker)
class QuizTakerAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
