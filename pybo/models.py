from django.contrib.auth.models import User
from django.db import models

# ---------------------------------- [edit] ---------------------------------- #
class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)#글자 수 제한 가능
    content = models.TextField()#글자 수 제한 없는 항목 작성 가능
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)#Question 모델을 내용을 가져옴
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)


class Graduation(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    result = models.IntegerField(default=0)
    least = 130
    ecpt = models.IntegerField(default=0)
    major = models.IntegerField(default=0)
    ppe = models.IntegerField(default=0)
    hus = models.IntegerField(default=0)
    other_humanity = models.IntegerField(default=0)
    core_eng1 = models.IntegerField(default=0)
    core_eng2 = models.IntegerField(default=0)
    core_writing = models.IntegerField(default=0)
    core_math1 = models.IntegerField(default=0)
    core_math2 = models.IntegerField(default=0)
    core_science = models.IntegerField(default=0)
    core_exp = models.IntegerField(default=0)
    music = models.IntegerField(default=0)
    exercise = models.IntegerField(default=0)

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True)

# ---------------------------------------------------------------------------- #