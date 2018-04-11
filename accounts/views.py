from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def sign_up( request ):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get( username=request.POST['username'] )
                return render( request, 'accounts/signup.html', { 'error': 'Account Taken!!'} )
            except User.DoesNotExist:
                user = User.objects.create_user( request.POST['username'], password=request.POST['password1'] ) 
                auth.login( request, user )
                return redirect( 'home' )   
        else:
        	return render( request, 'accounts/signup.html', { 'error': 'Password do not match!!'} )
    else:
        # request method is a GET, so render the signup view
	    return render( request, 'accounts/signup.html' )

def login( request ):
    if request.method == 'POST':
        user = auth.authenticate( username = request.POST['username'], password = request.POST['password'] )
        if user is not None:
            auth.login( request, user )
            return redirect( 'home' )
        else:
            return render( request, 'accounts/login.html', { 'error': 'Username or password is incorrect!!'} )   	
    else:
        return render( request, 'accounts/login.html' )

def logout( request ):
    if request.method == 'POST':
        auth.logout( request )
        return redirect( 'home' )        
   

