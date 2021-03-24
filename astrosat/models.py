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

    equatorial_ra = models.DecimalField( 
        max_digits=6,
        decimal_places=3,
    )
    
    equatorial_dec = models.DecimalField( 
        max_digits=5,
        decimal_places=3,
    )
    
    galactic_longitude = models.DecimalField( 
        max_digits=6,
        decimal_places=2,
    )
    
    galactic_latitude = models.DecimalField( 
        max_digits=8,
        decimal_places=4,
    )
    
    type_of_observation = models.CharField( 
        max_length=500,
        blank=True, 
        null=True
    )
    
    positional_accuracy = models.DecimalField( 
        max_digits=7,
        decimal_places=2,
        blank=True, 
        null=True
    )
    
    optical_counterpart_name = models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )
    
    v_magnitude = models.DecimalField( 
        max_digits=6,
        decimal_places=3,
        blank=True, 
        null=True
    )
    
    b_v_color_index  = models.DecimalField( 
        max_digits=6,
        decimal_places=3,
        blank=True, 
        null=True
    )
     
    u_b_color_index  = models.DecimalField( 
        max_digits=5,
        decimal_places=2,
        blank=True, 
        null=True
    )
    
    spectral_type =  models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )
    
    x_ray_flux = models.DecimalField( 
        max_digits=11,
        decimal_places=3,
        blank=True, 
        null=True
    )
    
    orbital_period = models.DecimalField( 
        max_digits=10,
        decimal_places=6,
        blank=True, 
        null=True
    )
    
    pulse_period = models.DecimalField( 
        max_digits=11,
        decimal_places=5,
        blank=True, 
        null=True
    )

    name2 = models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )

    name3 = models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )
    
    class Meta:
        verbose_name = "CosmicSource"
        verbose_name_plural = "CosmicSources"

    def __str__(self):
        return self.name


class Astrosat(models.Model):
    
    cosmic_source =  models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )
    
    

class Publication(models.Model):

    title = models.CharField( 
        max_length=500,
        blank=True, 
        null=True
    )

    abstract = models.TextField(
        blank=True, 
        null=True
    )
    
    author = models.CharField(
        max_length=500,
        blank=True, 
        null=True
    )
    
    paper_url = models.URLField(
        blank=True, 
        null=True
    )


    keyword = models.TextField(
        blank=True, 
        null=True
    )
    
    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __str__(self):
        return self.title
 
