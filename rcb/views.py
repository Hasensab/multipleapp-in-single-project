from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return render(request,'kohli.html')
def ABD(request):
    return HttpResponse('He is Mr 360 in IPL')