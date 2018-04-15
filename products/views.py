from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Products
from django.utils import timezone

# Create your views here.

def home( request ):
    products = Products.objects
    return render( request, 'products/home.html', { 'products': products } )

@login_required( login_url="/accounts/signup" )
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
            return redirect('/products/' + str(product.id) ) 	
        else:
            render( request, 'products/createProducts.html', { 'error': 'All fields are required!!' } )        	
    else:
        render( request, 'products/createProducts.html' )    	
    return render( request, 'products/createProducts.html' )

@login_required( login_url="/accounts/signup" )
def detail( request, product_id ):
    product = get_object_or_404(Products, pk=product_id )
    return render( request, 'products/detail.html', { 'product': product } )

@login_required( login_url="/accounts/signup" )
def upvote( request, product_id ):
    if request.method == 'POST':
        product = get_object_or_404( Products, pk=product_id )
        product.votes_total += 1
        product.save()
        return redirect( '/products/' + str(product_id) )         

















