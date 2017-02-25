from django.shortcuts import render,redirect
from apps.core.models import *

def login(request):

	error = ''
	request.session['user'] = None

	if 'username' in request.POST :
		username = request.POST['username']
		password = request.POST['password']
		# check whether the user is in database or not
		if username == "admin@radd3.com" and password == "DT@N@LYTICS":
		    request.session['user'] = {
		        # "id": user[0].id,
		        "username": "admin@radd3.com", #user[0].email,
		        "password": "DT@N@LYTICS", #user[0].name.split(" ")[0],
		    }

		    return redirect("/admin")

		user = Account.objects.filter(email=username, password=password)

		if len(user) > 0:	
		    request.session['user'] = {
                "username": user[0].username,
                "email": user[0].email,
                "password": user[0].password,
		    }

		    return redirect("/dashboard")
		else :
			error = "incorrect username and password."
	return render(request, 'login.html', {"params" : error})

def logout(request):
	request.session['user'] = None
	return redirect("/")

def register(request):
	username = ""
	if request.POST :
		username = request.POST["username"]
		account = Account()
		account.username = request.POST["username"]
		account.email = request.POST["email"]
		account.password = request.POST["password"]
		account.save()
		return redirect("/")
	return render(request, 'register.html', {})

def dashboard(request):
	# Here insert real code
	return render(request, 'dashboard.html', {"params" : "Dashboard"})

def games(request):
	# Here insert real code
	
	return render(request, 'dashboard.html', {"params": "Games"})

def grades(request):
	# Here insert real code
	
	return render(request, 'dashboard.html', {"params" : "Grades"})

def players(request):
	# Here insert real code
	
	return render(request, 'dashboard.html', {"params" : "Players"})	
