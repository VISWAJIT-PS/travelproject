from django.shortcuts import render
from . models import Place,People

def demo(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    return render(request,"index.html",{'result':obj,'result2': obj1})



