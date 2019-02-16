from django.urls import path
from .views import register , user_login , homepage , user_logout , ask_question,index , question_detail
from .views import add_answer , que_vote , ans_vote , answer_detail

app_name = 'myapp'
urlpatterns = [
    path('register/',register,name='register'),
    path('login/',user_login,name='login'),
    path('',homepage,name='home'),
    path('logout',user_logout,name='logout'),
    path('ask_question',ask_question,name = 'ask_question'),
    path('questions/',index,name='question_list'),
    path('question/<question_id>/',question_detail,name='question_detail'),
    path('question/<question_id>/add_answer/',add_answer,name='add_answer'),
    path('question/<question_id>/vote/',que_vote,name='que_vote'),
    path('question/<question_id>/<answer_id>/vote/',ans_vote,name='ans_vote'),
    path('answers/<answer_id>/',answer_detail,name='answer_detail'),

]
