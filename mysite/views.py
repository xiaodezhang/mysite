from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect


# Create your views here.
def index(request):
    return render(request,'mysite/index.html')
def download(request):
    if request.user.is_authenticated:
        return render(request,'mysite/download.html')
    else:
        return redirect('signin_page')

def signin_page(request):
    return render(request,'mysite/signin.html',{'body_color':'bg-dark'})

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
