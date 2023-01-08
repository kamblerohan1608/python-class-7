from django.contrib import admin
from .models import ResumeModel
# Register your models here.

@admin.register(ResumeModel)
class ResumeAdminModel(admin.ModelAdmin):
    list_display = ['fname','lname','D_o_b','gender','language','locality','city','state','pin','contact','email','prefered_language','profile_photo']