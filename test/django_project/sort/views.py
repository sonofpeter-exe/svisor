from django.shortcuts import render

# Create your views here.

def sort(request):
    return render(request, 'sort/index.html')
