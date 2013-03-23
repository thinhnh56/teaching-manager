# Create your views here.
from django.contrib.auth import authenticate, login
from django.shortcuts import render_to_response
from django.template import RequestContext
def nonStaffLogin(request):
	state = "Login"
	username = password = ''
	
	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')
		
		user = authenticate(username = username, password = password)
		if user is not None:
			if user.is_active:
				login(request, user)
				state = "You've login succesfully"
			else:
				state = "Your account has been deactivated"
		else:
			state = "Your account is invalid"
	
	return render_to_response('login_non_staff.html',  {'state' : state, 'username':username}, context_instance= RequestContext(request) )

