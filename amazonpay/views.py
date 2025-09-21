from django.shortcuts import render , HttpResponse

# Create your views here.
def amzonpay(request):
    return render(request,'amazonpay.html')