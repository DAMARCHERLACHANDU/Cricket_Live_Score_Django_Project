from django.shortcuts import render 

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def indiateam(request):
    return render(request,'india.html')

def austeam(request):
    return render(request,'australia.html')

def engteam(request):
    return render(request,'england.html')

def sriteam(request):
    return render(request,'srilanka.html')

def witeam(request):
    return render(request,'westindes.html')

def matches(request):
    return render(request,'match.html')

def seriesm(request):
    return render(request,'series.html')

def live(request):
    return render(request,'livescore.html')

def live1(request):
    return render(request,'afg.html')

def live2(request):
    return render(request,'eng.html')

def live3(request):
    return render(request,'sa.html')

def about(request):
    return render (request,'about.html')