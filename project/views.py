from django.shortcuts import render
from .models import Post


def index(request):
    return render(request, 'project/index.html')


def datalogin(request):
    if request.method == "POST":
        post = Post()
        post.Name = request.POST.get('uname')
        post.password = request.POST.get('psw')
        if request.POST.get('login') == 'login':
            if Post.objects.filter(Name=post.Name).exists() and Post.objects.filter(password=post.password).exists():
                return render(request, 'project/result.html', {'result': 'exists'})
            else:
                return render(request, 'project/result.html', {'result': 'Wrong entry'})
        elif  request.POST.get('submit') == 'submit':
            post.password2 = request.POST.get('psw2')
            if post.password == post.password2:
                post.save()
                #Result = Post.objects.all()
                return render(request, 'project/result.html', {'result': 'submit your request'})
            else:
                return render(request,'project/result.html',{'result':'password is not same'})
        else:
            return render(request, 'project/result.html', {'result': 'wrong entry'})

