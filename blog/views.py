from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request,type,size):
    # return HttpResponse("type="+type+";size="+size)
    return render(request,"index.html")
