from django import forms
from .models import Question, Answer, Comment, Graduation, UploadFileModel
from django.views.generic.edit import ModelFormMixin as FormView


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ['title', 'file']
        labels ={
            'title': 'title_name',
            'file': 'file_content',
        }

    def __init__(self, *args, **kwargs):
        super(UploadFileForm, self).__init__(*args, **kwargs)
        self.fields['file'].required = False

"""
class MyFormView(FormView):
    form_class = UploadFileForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
"""

class GraduationForm(forms.ModelForm):
    class Meta:
        model = Graduation
        fields = ['my_major']
        labels = {'my_major': '나의 전공'}