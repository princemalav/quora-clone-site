from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from django.shortcuts import reverse , render

# Create your models here.
class Question(models.Model):
    question_title = models.CharField(max_length=100)
    question_text = models.CharField(max_length=1000)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    num_of_answers = models.IntegerField(default=0)
    up_votes = models.IntegerField(default=0)
    down_votes = models.IntegerField(default=0)
    up_list = models.ManyToManyField(User , related_name='que_up_list')
    down_list = models.ManyToManyField(User , related_name='que_down_list')

    def __str__(self):
        return self.question_text

    def get_absolute_url(self):
        return reverse('myapp:question_detail',kwargs = {'question_id':self.id})

    def get_answer_url(self):
        return reverse('myapp:add_answer',kwargs={'question_id':self.id})

    def get_vote_url(self):
        return reverse('myapp:que_vote',kwargs={'question_id':self.id})

class Answer(models.Model):
    question = models.ForeignKey(Question , on_delete=models.CASCADE)
    ans_text = models.CharField(max_length = 1000)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    up_list = models.ManyToManyField(User , related_name='ans_up_list')
    down_list = models.ManyToManyField(User,related_name='ans_down_list')

    def __str__(self):
        return self.ans_text

    def get_absolute_url(self):
        return reverse('myapp:answer_detail',kwargs={'answer_id':self.id})

    def get_vote_url(self):
        return reverse('myapp:ans_vote',kwargs={'answer_id':self.id,'question_id':self.question.id})
