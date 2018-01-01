from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime
# from datetime import timezone, timedelta


def index(request):
    timenow = datetime.now()
    # timenow2 = strftime("%Y-%m-%d %H:%M %p", gmtime())
    # print(timenow2)
    context = {
        "time" : timenow
    }
    print("The time is", timenow)
    return render(request,'myapp/the_time.html', context)
