from django.shortcuts import render

# Create your views here.
def StudentHomePage(request):
    return render(request,'studentapp/StudentHomePage.html')

