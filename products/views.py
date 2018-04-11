from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def home( request ):
	return render( request, 'products/home.html' )

@login_required
def create( request ):
	#only users that are logged in can visit this page
    return render( request, 'products/createProducts.html' )

