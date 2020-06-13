from django.db import models
from datetime import datetime
 
from realtor.models import Realtor

class Listing (models.Model) : 
    realtor = models.ForeignKey(
        Realtor,
        on_delete=models.DO_NOTHING
    )
    title = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    state = models.CharField(max_length = 200)
    city = models.CharField(max_length = 200)
    zipcode = models.IntegerField()
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    garage = models.IntegerField()
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to = 'photos/%Y/%m/%d', blank=True, default = 'default.png')    

    def save(self, *args, **kwargs) : 
        try : 
            prev = Realtor.objects.get(id=self.id)
            if prev.photo != self.photo : 
                prev.photo.delete()
        except : 
            pass
        
        super().save(*args, **kwargs)

    def __str__(self) : 
        return self.title


