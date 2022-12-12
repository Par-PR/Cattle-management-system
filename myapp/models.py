from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField()
    number = models.BigIntegerField()
    massage = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
    
class buyer(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)
    address = models.TextField()
    
    def __str__(self):
        return self.name  
    
class seller(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.BigIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=25)
    address = models.TextField()
    
    def __str__(self):
        return self.name
    

STATUS_cattle = (('Sold', 'Sold'), ('Purcharsed', 'Purchased'))
class cattler(models.Model):
    name = models.CharField(max_length=25)
    image = models.ImageField(upload_to='Cattleimages')
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    cost = models.BigIntegerField()
    status = models.CharField(choices=STATUS_cattle, max_length=25, default= "Sold")
    
    
    def __str__(self):
        return self.name
    
class registration(models.Model):
    registration_id= models.AutoField(primary_key=True)
    typec=models.CharField(max_length=25)
    name=models.CharField(max_length=90)
    mobile=models.CharField(max_length=111, default="")
    email=models.CharField(max_length=111)
    amount=models.IntegerField(default=0)
    address=models.CharField(max_length=111)
    
    def __str__(self):
        return self.name
    