from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
 
from realtor.models import Realtor

#   Listing Model
class Listing (models.Model) : 
    #   Realtor as the foreign key
    realtor = models.ForeignKey(
        Realtor,
        on_delete=models.DO_NOTHING
    )
    #   rest of the field of the table
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
    pub_date = models.DateTimeField(default=datetime.now())

    #   overriding the save method
    def save(self, *args, **kwargs) : 
        try : 
            prev = Listing.objects.get(id=self.id) 
            if prev.photo_main != self.photo_main : 
                prev.photo_main.delete()
        except : 
            pass
        super().save(*args, **kwargs)
        

    #   function to check if the current listing is recent
    def is_recent(self) : 
        return True if self.pub_date >= (timezone.now() - timedelta(days=2)) else False

    #   __str__ method
    def __str__(self) : 
        return self.title


