from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from .models import RegisterForm, User, LoginForm
import hashlib
from zxcvbn import zxcvbn


def register(request):
    if request.method == "GET":
        regform = RegisterForm()
        return render(request, "userRegister.html", {"regform": regform})
    else:
        regform = RegisterForm(request.POST)
        error_info = []
        if regform.is_valid():
            cd = regform.cleaned_data
            if cd["password"] != cd["password2"]:
                error_info.append("两次密码不一致!")
                return render(request, "userRegister.html", {"regform": regform, "error_info": error_info})
            if zxcvbn(cd["password"])['score'] <= 2:
                error_info.append("密码太弱!")
                return render(request, "userRegister.html", {"regform": regform, "error_info": error_info})
            new_user =User.objects.create()
            new_user.username = cd["username"]
            new_user.email = cd["email"]
            new_user.password = hashlib.md5(cd["password"].encode(encoding='UTF-8')).hexdigest()
            new_user.save()
            #自动登陆
            request.session['islogin'] = True
            user_info = {}
            user_info['username'] = new_user.username
            request.session['user_info'] = user_info
            return HttpResponseRedirect('/')
        else:
            cd = request.POST
            try:
                old_user = User.objects.get(username=cd["username"])
                error_info.append("该用户名已被注册!")
                return render(request, "userRegister.html", {"regform": regform, "error_info": error_info})
            except:
                pass
            try:
                old_user = User.objects.get(email=cd["email"])
                error_info.append("该邮箱已被注册!")
                return render(request, "userRegister.html", {"regform": regform, "error_info": error_info})
            except:
                 pass
            error_info.append("    输入无效!")
            return render(request, "userRegister.html", {"regform": regform,"error_info": error_info})

def login(request):
    if request.method == "GET":
        lgform = LoginForm()
        return render(request, "userLogin.html", {"lgform": lgform})
    else:
        lgform = LoginForm(request.POST)
        error_info = []
        if lgform.is_valid():
            cd = lgform.cleaned_data
            try:
                user = User.objects.get(username=cd["username"])
            except:
                error_info.append("该用户不存在！")
                return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})
            if user.password != hashlib.md5(cd["password"].encode(encoding='UTF-8')).hexdigest():
                error_info.append("密码不正确！")
                return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})
            if cd["identity"] == "tourist" and user.identity != "tourist":
                error_info.append("you are not tourist!")
                return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})
            if cd["identity"] == "salesman" and user.identity != "salesman":
                error_info.append("you are not salesman!")
                return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})
            if cd["identity"] == "admin" and user.identity != "admin":
                error_info.append("you are not administrator!")
                return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})
            if cd["identity"] == "admin" and user.identity == "admin":
                request.session['islogin'] = True
                user_info = {}
                user_info['username'] = user.username
                request.session['user_info'] = user_info
                return HttpResponseRedirect('/administrator/')
            if cd["identity"] == "salesman" and user.identity == "salesman":
                request.session['islogin'] = True
                user_info = {}
                user_info['username'] = user.username
                request.session['user_info'] = user_info
                return HttpResponseRedirect('/form_salesman/')
            request.session['islogin'] = True
            user_info = {}
            user_info['username'] = user.username
            request.session['user_info'] = user_info
            return HttpResponseRedirect('/')
        else:
            error_info.append("    输入无效!")
            return render(request, "userLogin.html", {"lgform": lgform,"error_info": error_info})

def logout(request):
    if request.method == 'GET':
        if  request.session['islogin'] ==True:
            del request.session['user_info']
            del request.session['islogin']
            return HttpResponseRedirect('/')
    else:
        return HttpResponse("您还未登录")

def rate(request):
    if request.method == "GET":
        try:
            pts = int(request.GET.get("pts"))
        except:
            return HttpResponse("您还未打分ψ(*｀ー´)ψ")
        username = request.GET.get("username")
        user_id = User.objects.get(username = username).id
        movie_id = request.GET.get("movie_id")
        try:
            a = Rating.objects.get(user_id=user_id, movie_id=int(movie_id))
            a.pts = pts
            a.save()
            return HttpResponseRedirect("../../subject/"+str(movie_id))
        except:
            user = User.objects.get(username=str(username))
            movie = Movie.objects.get(id=int(movie_id))
            a = Rating.objects.create( user_id = user,movie_id = movie,pts = pts)
            a.save()
            return HttpResponseRedirect("../../subject/"+str(movie_id))

            
