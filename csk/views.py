from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def msd(request):
    return render(request,'msd.html')
def jadeja(request):
    return HttpResponse('<marquee><h1 style="color:red">hai jadeja how are you</h1></marquee>')

