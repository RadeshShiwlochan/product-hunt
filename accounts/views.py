from django.shortcuts import render

# Create your views here.
def sign_up( request ):
	return render( request, 'accounts/signup.html' )

def login( request ):
	return render( request, 'accounts/login.html' )

def logout( request ):
    return render( request, 'accounts/signout.html' )	

