from django.db import models

# Create your models here.

class Month(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name 

class Blog (models.Model) :
    title = models.CharField(max_length = 255 )
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.title
    

class About(models.Model) : 
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    
    def __str__(self):
        return self.info
    
   
class Work(models.Model) :
    title = models.CharField(max_length = 255 )
    info = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(auto_now_add = True)
    is_published = models.BooleanField(default = True)
    month = models.ForeignKey(Month,on_delete=models.CASCADE)
    date_start = models.DateField(auto_now_add = False, null=True )
    date_end = models.DateField(auto_now_add = False, null=True)

    def __str__(self):
        return self.title



    
    


    
   





    


    