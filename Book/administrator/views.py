from django.shortcuts import render, render_to_response
import hashlib
from account.models import User

# Create your views here.
def admin(request):
	if request.method == "GET":
		return render(request, "admin.html")

def add_salesman(request):
   NAME=request.GET['user_id']
   PW=hashlib.md5(request.GET['password'].encode(encoding='UTF-8')).hexdigest()
   MAIL=request.GET['mail']
   IDEN=request.GET['identity']
   this_user=User.objects.filter(username=NAME)
   User.objects.create(username=NAME,password=PW,email=MAIL,identity=IDEN)
   return render_to_response('admin.html', {'user':this_user, 'add':True})


def check_salesman(request):
   NAME=request.GET['user_id']
   user=User.objects.filter(username__icontains=NAME)
   return render_to_response('process_user.html', {'query':NAME,'user':user})

def operate_salesman(request):
   if request.GET['subject'] == 'delete user':
      NAME=request.GET['username']
      search_word = request.GET['search_word']
      User.objects.filter(username=NAME).delete()
      user=User.objects.filter(username__icontains=search_word)
      return render_to_response('process_user.html', {'query':search_word,'user':user,'delete':True})
   elif request.GET['subject'] == 'change user':
      search_word = request.GET['search_word']
      o_NAME = request.GET['o_username']
      NAME=request.GET['username']
      PW=hashlib.md5(request.GET['password'].encode(encoding='UTF-8')).hexdigest()
      MAIL=request.GET['email']
      IDEN=request.GET['identity']
      User.objects.filter(username=o_NAME).update(username=NAME,password=PW,email=MAIL,identity=IDEN)
      user=User.objects.filter(username__icontains=search_word)

      return render_to_response('process_user.html', {'query':search_word,'user':user,'devise':True})
   
