from django.db import models

# Create your models here.
class Addition(models.Model):
    data_input  = models.CharField(max_length=50)


    def __str__(self):
        return self.data_input


class Static_informations(models.Model):
    data_of_filed   = models.CharField(max_length=50)
    data_of_filed1   = models.CharField(max_length=50,default=0)

    colour   = models.CharField(max_length=50)
    text_alingment   = models.CharField(max_length=50,default='center')
    inputtype   = models.CharField(max_length=50,default='text')




    def __str__(self):
        return self.data_of_filed