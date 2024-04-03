from django.shortcuts import render

# Create your views here.

def jot(request):
    d={'a':100,'b':20,'c':3}
    return render(request,'cond.html',d)

def jotf(request):
    d={'name':'SINDHU'}
    return render(request,'cond.html',d)