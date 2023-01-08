from django.db import models

# Create your models here.

state_choice = (("Andhra Pradesh","Andhra Pradesh"),("Arunachal Pradesh ","Arunachal Pradesh "),("Assam","Assam"),("Bihar","Bihar"),("Chhattisgarh","Chhattisgarh"),("Goa","Goa"),("Gujarat","Gujarat"),("Haryana","Haryana"),("Himachal Pradesh","Himachal Pradesh"),("Jammu and Kashmir ","Jammu and Kashmir "),("Jharkhand","Jharkhand"),("Karnataka","Karnataka"),("Kerala","Kerala"),("Madhya Pradesh","Madhya Pradesh"),("Maharashtra","Maharashtra"),("Manipur","Manipur"),("Meghalaya","Meghalaya"),("Mizoram","Mizoram"),("Nagaland","Nagaland"),("Odisha","Odisha"),("Punjab","Punjab"),("Rajasthan","Rajasthan"),("Sikkim","Sikkim"),("Tamil Nadu","Tamil Nadu"),("Telangana","Telangana"),("Tripura","Tripura"),("Uttar Pradesh","Uttar Pradesh"),("Uttarakhand","Uttarakhand"),("West Bengal","West Bengal"),("Andaman and Nicobar Islands","Andaman and Nicobar Islands"),("Chandigarh","Chandigarh"),("Dadra and Nagar Haveli","Dadra and Nagar Haveli"),("Daman and Diu","Daman and Diu"),("Lakshadweep","Lakshadweep"),("National Capital Territory of Delhi","National Capital Territory of Delhi"),("Puducherry","Puducherry"))


city_choice = [('Mumbai','Mumbai'),('Vashi','Vashi'),('Dadar','Dadar'),('Virar','Virar'),('Thane','Thane'),('Kurla','Kurla')]

class ResumeModel(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    D_o_b = models.DateField(auto_now=False,auto_now_add=False)
    gender = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    locality= models.CharField(max_length=100)
    city=models.CharField(choices=city_choice, max_length=100)
    state=models.CharField(choices=state_choice,max_length=100)
    pin = models.PositiveIntegerField()
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    prefered_language = models.CharField(max_length=100)
    profile_photo =  models.ImageField(upload_to = 'profile_image/')