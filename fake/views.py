from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'fake/home.html', context={'title': 'Hello, Fake'})

def table(request):
    if request.method == 'POST':
        raise Exception("Breakpoint")
    return render(request, 'fake/table.html', context={'title': 'Hello, Fake',
                                                       'img_paths': ['note.png',
                                                                     'home.png',
                                                                     'search.png',
                                                                     'tag.png']})
def lst(request):
    return render(request, 'fake/list.html', context={'title': 'Hello, Fake',
                                                       'img_paths': ['note.png',
                                                                     'home.png',
                                                                     'search.png',
                                                                     'tag.png']})
def form(request):
    if request.method == 'POST':
        return HttpResponse(request.POST['result']);
    return render(request, 'fake/form.html', context={'title': 'Hello, Fake',
                                                       'img_paths': ['note.png',
                                                                     'home.png',
                                                                     'search.png',
                                                                     'tag.png']})
