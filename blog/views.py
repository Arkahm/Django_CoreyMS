from django.shortcuts import render

posts = [
    {
        'author': 'Ray',
        'title': 'Blog 1',
        'content': 'First post',
        'date_posted': 'Today'
    },
    {
        'author': 'Someone Else',
        'title': 'Blog 2',
        'content': 'Second post',
        'date_posted': 'Tomorrow'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html', {'title': 'About'})
