from django.shortcuts import render, redirect
from django.contrib.auth import login,logout,authenticate
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method == 'POST':
        print(request.POST)
        questions = QuesModel.object.all()
        score = 0
        wrong =0
        correct =0
        total = 0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q.ans)
            print()
            if q.ans == request.POST.get(q.question):
                score +=1
            else:
                wrong+=1
        percent = score/(total*10)*100
        context = {
            'socre':score,
            'time':request.POST.get('timer'),
            'wrong':wrong,
            'percent':percent,
            'total':total
            }
        return render(request, 'result.html',context)
    else:
        questions = QuesModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'index.html',context)

    
def addQuestion(request):
    if request.user.is_staff:
        form = addQuestiionform()
        if request.method == 'POST':
            form = addQuestiionform(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
        context ={
            'form':form 
        }
        return render(request, 'addQuestion.html', context)
    else:
        return redirect('index')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = createuserform()
        if request.method == 'POST':
            form = createuserform(request.POST)
            if form.is_valid():
                user=form.save()
                return redirect('login')
        context = {'form':form}
        return render(request,'register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('/')
            context = {}
            return render(request,'login.html',context)

def logoutPage(request):
    logout(request)
    return redirect('/')
