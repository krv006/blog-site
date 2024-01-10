from django.db import models

# Create your models here.

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
    # month = models.ForeignKey(Month,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


# class Month(models.Model):
#     name=models.CharField(max_length=200)
    
    


    
   





    


    