from django.shortcuts import render
from django.http import HttpResponse
from .chr import fetch

def index (request):
   return  render(request,'index.html')
def function1(request):
   text = (request.POST.get('text','default'))
   fullcaps = (request.POST.get('upper','off'))
   fulllows = (request.POST.get('lower','off'))
   print(f"Entered text in bar : {text}")
   print(f"fulcaps :{fullcaps}")
   print(f"fullows :{fulllows}")
   if (fullcaps == fulllows == "on"):
     fetch()
     return render(request,'error.html')
   if (fullcaps == "on"):
    cap = text.upper()
    fetch()
    params = {'YOURINPUT':text,'UPPER':cap}
    return render(request,'capi.html',params)
   if (fulllows == "on"):
    low = text.lower()
    params = {'YOURINPUT':text,'UPPER':low}
    return render(request,'capi.html',params)
   else :
     return HttpResponse('error')