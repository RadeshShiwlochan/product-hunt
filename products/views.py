from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone

# Create your views here.

def home( request ):
	return render( request, 'products/home.html' )

@login_required
def create( request ):
	#only users that are logged in can visit this page
    if request.method == 'POST':
        title = request.POST['title']
        body  = request.POST['body']
        url   = request.POST['url']
        image = request.FILES['image']
        icon  = request.FILES['icon']
        if title and body and url and image and icon:
            product = Products()
            product.title = title
            product.body = body
            if url.startswith( 'http://' ) or url.startswith( 'https://' ):
            	product.url = url
            else:
                product.url = 'http://' + url
            product.image = image     
            product.icon = icon
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save() 
            return redirect('home')	
        else:
            render( request, 'products/createProducts.html', { 'error': 'All fields are required!!' } )        	
    else:
        render( request, 'products/createProducts.html' )    	
    return render( request, 'products/createProducts.html' )

