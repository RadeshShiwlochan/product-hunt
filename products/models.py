from django.db import models

class Products( models.Model ):
    title = models.CharField( max_length=200 )
    url = models.CharField( max_length=200 )
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField()
    image = models.ImageField( upload_to='images/' )
    icon = models.ImageField( upload_to='images/' )
    body = models.CharField( max_length=1000 )
