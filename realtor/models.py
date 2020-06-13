from django.db import models
from datetime import datetime, timedelta

#   realtor class model
class Realtor(models.Model) : 
    realtor_name = models.CharField(max_length = 200)
    email = models.EmailField()
    description = models.TextField(blank=True)
    phone = models.CharField(max_length = 10, default = None)
    is_mvp = models.BooleanField(default = False)
    hire_date = models.DateTimeField(default = datetime.now(), blank=True)
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d', default = 'default.png')

    #   overriding the save method
    def save(self, *args, **kwargs) : 
        try : 
            prev = Realtor.objects.get(id=self.id)
            if prev.photo != self.photo : 
                prev.photo.delete()
        except : 
            pass
        
        super().save(*args, **kwargs)

    #   overriding the delete method
    def delete(self, *args, **kwargs) : 
        self.photo.delete()
        super().delete(*args, **kwargs)

    def __str__(self) : 
        return self.realtor_name



