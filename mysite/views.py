from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.decorators.csrf import csrf_protect
from django.templatetags.static import static
import os

# Create your views here.
def index(request):
    return render(request,'mysite/index.html')
def download(request):
    if request.user.is_authenticated:
        doc_path = "."+static('mysite/resource/doc')
        doc_list = []
        for doc_dir in os.listdir(doc_path):
            doc_path_full = doc_path+'/'+doc_dir
            if os.path.isdir(doc_path_full):
                subdir_file_dic = []
                for subdir_file in os.listdir(doc_path+"/"+doc_dir):
                    subdir_file_full = doc_path_full+"/"+subdir_file
                    if os.path.isfile(subdir_file_full):
#                        subdir_file_dic.append({'name':subdir_file,'urlpath':subdir_file})
                        subdir_file_dic.append({'name':subdir_file,'urlpath':'mysite/resource/doc/'+doc_dir+"/"+subdir_file})
                doc_list.append({'name':doc_dir,'subdir_files':subdir_file_dic})
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
