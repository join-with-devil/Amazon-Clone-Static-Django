from django.shortcuts import render , HttpResponse

# Create your views here.
def home(request):
    return render(request,'amzhome.html')
def computer(request):
    return render(request,'computer.html')

def sell(request):
    return render(request,'sell.html') 

def mobiles(request):
    return render(request,'mobiles.html')

def fresh(request):
    return render(request,'fresh.html') 

def signup(request):
    return render(request,'signup.html')
  
def newrelease(request):
    return render(request,'newrelease.html')

def fashion(request):
    return render(request,'fashion.html')  

def bestseller(request):
    return render(request,'bestseller.html')  

def customserv(request):
    return render(request,'customserv.html') 

def todaydeals(request):
    return render(request,'todaydeals.html')


def electronics(request):
    return render(request,'electronics.html')   

def handk(request):
    return render(request,'handk.html')      