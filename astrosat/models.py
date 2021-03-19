from django.db import models

# Create your models here.

class Satellite(models.Model):

    name = models.CharField( 
        max_length=500,
    )

    class Meta:
        verbose_name = "Satellite"
        verbose_name_plural = "Satellites"

    def __str__(self):
        return self.name



class CosmicSource(models.Model):
    
    name = models.CharField( 
        max_length=500,
    )
    
    class Meta:
        verbose_name = "CosmicSource"
        verbose_name_plural = "CosmicSources"

    def __str__(self):
        return self.name


class Publication(models.Model):

    title = models.CharField( 
        max_length=500,
    )

    abstract = models.TextField(
        
    )
    
    author = models.CharField(
        max_length=500,
    )
    
    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title
 
