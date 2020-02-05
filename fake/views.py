from django.shortcuts import render
from django.http.response import HttpResponse
from fake.models import Paper

# Create your views here.


def home(request):
    return render(request, 'fake/home.html', context={'title': 'Hello, Fake!'})

def test(request):
    if request.method == 'GET':
        uid = request.session['uid'] = request.GET.get('uid', "19351023")
        mid = request.session['mid'] = request.GET.get('mid', "1")
        request.session['answer'] = 'aabb'
        return render(request, 'fake/test.html', context={
            'title': 'Fake测试',
            'uid': uid,
            'mid': mid
        })

    elif request.method == 'POST':
        # raise Exception("Breakpoint")
        ans = request.session['answer']
        res = request.POST['result']
        cnt = len(ans)
        true_cnt = sum((ans[i] == res[i] for i in range(cnt)))
        paper = Paper(
            uid=request.session['uid'],
            mid=request.session['mid'],
            cnt=cnt,
            true_cnt=true_cnt)
        paper.save()
        return render(request, 'fake/result.html');
        # return HttpResponse(request.session['answer'] + '<br />' + request.POST['result']);
    else:
        return render(request, 'fake/base.html', context={'title': 'Unknown method'})

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
def form2(request):
    if request.method == 'POST':
        # raise Exception("Breakpoint")
        ans = request.session['answer']
        res = request.POST['result']
        cnt = len(ans)
        true_cnt = sum((ans[i] == res[i] for i in range(cnt)))
        paper = Paper(
            uid=request.session['uid'],
            mid=request.session['mid'],
            cnt=cnt,
            true_cnt=true_cnt)
        paper.save()
        return render(request, 'fake/result.html');
        # return HttpResponse(request.session['answer'] + '<br />' + request.POST['result']);
    else:
        request.session['uid'] = "19351023"
        request.session['mid'] = "1"
        request.session['answer'] = 'aabb'
        return render(request, 'fake/form.html', context={'title': 'Hello, Fake',
                                                       'img_paths': ['note.png',
                                                                     'home.png',
                                                                     'search.png',
                                                                     'tag.png']})

