from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
from django.templatetags.static import static
import os

def walklevel(some_dir, level=1):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]

# Create your views here.
def index(request):
    return render(request,'mysite/index.html')
def download(request):
    if request.user.is_authenticated:
        doc_path = "."+static('mysite/resource/doc')
        doc_list = []
        for _,items,_ in walklevel(doc_path):
            if items:
                for item in items:
                    doc_list.append({'urlpath':'test','name':item})
        return render(request,'mysite/download.html',{"doc_list":doc_list})
    else:
        return redirect('signin_page')

def signin_page(request):
    return render(request,'mysite/signin.html',{'body_color':'bg-dark'})

@csrf_protect
def signin(request):
    """
    if request.method == 'POST':
        if request.session.test_cookie_worked():
            request.session.delete_test_cookie()
        else:
            return render(request,'mysite/signin.html',{'failed_message':'Please enable cookies and try again.'})
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username = username,
            password = password)
    if user is not None:
        login(request,user)
        return redirect('download')
    else:
        return render(request,'mysite/signin.html',{'failed_message':'user or password error'})


def sign_out(request):
    logout(request)
    return redirect('signin_page')

def doc_list(request):
    return redirect('signin_page')
