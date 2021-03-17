from django.shortcuts import render,redirect

def index(request):
    return render(request,"index.html")

def survey(request):
    print("Got Post Info....................")
    print(request.POST)
    return render(request,"index.html")

def result(request):
    context = {
    "name" : request.POST['name'],
    "location" : request.POST['location'],
    "language" : request.POST['language'],
    "comment" : request.POST['comment'],
    }
    return render(request,"sucess.html",context)


