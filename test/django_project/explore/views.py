from django.shortcuts import render

posts = [
    {
        'author': 'Oki',
        'title': 'Blog 1',
        'content': 'First post content',
        'date_posted': 'August 08, 2021'
    },
    {
        'author': 'Oki 2',
        'title': 'Blog 2',
        'content': 'Second post content',
        'date_posted': 'August 07, 2021'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'explore/home.html', context)

def about(request):
    return render(request, 'explore/about.html', {'title':'About'})

def shop(request):
    return render(request, 'explore/shop.html', {'title':'Store'})
