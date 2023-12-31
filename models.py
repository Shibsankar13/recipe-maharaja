from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Contact Table"



class Recipe(models.Model):
   
    recipe_name = models.CharField(max_length=250)
    recipe_ingredients = models.CharField(max_length=250)
    recipe_description = models.TextField()
    recipe_image= models.ImageField(upload_to="recipe")


class UserInfo(models.Model):
   
    Uname = models.CharField(max_length=250)
    Email = models.CharField(max_length=250)
