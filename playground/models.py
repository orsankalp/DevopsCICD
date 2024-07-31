from django.db import models

# Create your models here.
class MVRS_Category(models.Model):
    MVRS_cat_name = models.CharField(max_length=100)
    MVRS_cat_description =models.TextField()
    def __str__(self):
        return self.MVRS_cat_name
class Cars(models.Model):
    MVRS_car_name = models.CharField(max_length=255)
    MVRS_car_description =models.CharField(max_length=255)
    car_category = models.ForeignKey(MVRS_Category, on_delete =models.CASCADE)
    MVRS_car_image = models.ImageField(upload_to='Cars' )
class Booking(models.Model):
    client_name = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=10)
    client_email =models.EmailField()
    select_vehicle = models.CharField(max_length=255)
    period_from = models.DateField()
    period_to = models.DateField()
class contact(models.Model):
    client_id  = models.CharField(max_length=255)
    client_phone = models.CharField(max_length=10)
    client_problem = models.CharField(max_length=255)
    raised_on = models.DateField(auto_now=True)
    def __str__(self):
        return f"Help Message for phone number {self.client_phone}"
