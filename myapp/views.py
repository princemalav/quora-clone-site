from django.shortcuts import render , reverse , redirect , get_object_or_404
from .forms import UserRegistrationForm
from django.shortcuts import HttpResponse , HttpResponseRedirect
from django.contrib.auth import login , authenticate , logout
from poll.models import Question , Answer
from django.contrib.auth.models import User
from django.utils import timezone



def homepage(request):
    question_list = Question.objects.order_by('-pub_date')

    context = {'home_content':'Welcome to Quora','ask_question':'ask_question','question_list':question_list}
    return render(request,'myapp/base.html',context)
def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserRegistrationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserRegistrationForm()
    return render(request,'myapp/register.html',{'user_form':user_form,
                                                    'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('myapp:home'))
            else:
                return HttpResponse('account not active')
        else:
            return HttpResponse('invalid login details')
    else:
        return render(request,'myapp/login.html')



    return render(request,'myapp/login.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('myapp:home'))

def ask_question(request):
    if request.method == 'POST':
        que_title = request.POST.get('question_title')
        que_detail = request.POST.get('question_detail')
        question = Question(question_title=que_title,question_text=que_detail,author=request.user,pub_date=timezone.now())
        question.save()
        return redirect(reverse('myapp:home'))
    return render(request,'myapp/ask_question.html')

def index(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list':question_list,}
    return render(request,'myapp/questions.html',context)

def question_detail(request , question_id):
    question  = get_object_or_404(Question,pk=question_id)
    answers = question.answer_set.order_by('-pub_date')
    print(answers)
    context = {'question':question,'answers':answers}
    return render(request,'myapp/que_detail.html',context)

def answer_detail(request,answer_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    context = {'answer':answer}
    return render(request,'myapp/ans_detail.html',context)

def add_answer(request,question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        answer = request.POST.get('answer')
        new_answer = Answer(question=question,ans_text=answer,author=request.user,
                            pub_date=timezone.now())
        new_answer.save()
        return redirect(reverse('myapp:home'))

    context = {'question':question}
    return render(request , 'myapp/add_answer.html',context)

def que_vote(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    if request.method=='POST':
        vote = request.POST.get('vote')
        if vote == 'UpVote':
            if request.user not in question.up_list.all() and request.user in question.down_list.all():
                question.down_list.remove(request.user)
                question.down_votes -= 1
                question.up_list.add(request.user)
                question.up_votes += 1

            elif request.user not in question.up_list.all():
                question.up_list.add(request.user)
                question.up_votes += 1

        if vote == 'DownVote':
            if request.user not in question.down_list.all() and request.user in question.up_list.all():
                question.up_list.remove(request.user)
                question.up_votes -= 1
                question.down_list.add(request.user)
                question.down_votes += 1

            elif request.user not in question.down_list.all():
                question.down_list.add(request.user)
                question.down_votes += 1

    question.save()
    return HttpResponseRedirect(reverse('myapp:question_detail',kwargs={'question_id':question_id}))

def ans_vote(request,answer_id,question_id):
    answer = get_object_or_404(Answer,pk=answer_id)
    print(answer_id)
    print('hello')
    if request.method =='POST':
        vote = request.POST.get('vote')
        print(vote)
        if vote == 'UpVote':
            if request.user not in answer.up_list.all() and request.user in answer.down_list.all():
                answer.down_list.remove(request.user)
                answer.down_vote -= 1
                answer.up_list.add(request.user)
                answer.up_vote += 1

            elif request.user not in answer.up_list.all():
                answer.up_list.add(request.user)
                answer.up_vote += 1
        if vote == 'DownVote':
            if request.user not in answer.down_list.all() and request.user in answer.up_list.all():
                answer.up_list.remove(request.user)
                answer.up_vote -= 1
                answer.down_list.add(request.user)
                answer.down_vote += 1

            elif request.user not in answer.down_list.all():
                answer.down_list.add(request.user)
                answer.down_vote += 1
    answer.save()
    return HttpResponseRedirect(reverse('myapp:question_detail',kwargs={'question_id':question_id}))
