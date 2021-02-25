from django.db import models

class data(models.Model):
    username = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=100, default="")
    full_name = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=150, default="")
    image = models.ImageField(upload_to='media',default="")

    def  __str__(self):
        return self.username
        
class password_resets(models.Model):
    email = models.EmailField(max_length=100, default="")
    token = models.CharField(max_length=100, default="")
    is_used = models.SmallIntegerField()
    created_at = models.DateTimeField()


    
