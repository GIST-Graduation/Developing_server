from django.contrib import admin
# ---------------------------------- [edit] ---------------------------------- #
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
# ---------------------------------------------------------------------------- #