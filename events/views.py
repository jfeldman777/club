from django.shortcuts import render

# Create your views here.def
def home(request,year,month):
    name = 'Joe'
    return render(request,'home.html',{
        "name": name,
        "year": year,
        "month": month,
    })
