from django.shortcuts import render,redirect
from django.views import View
from .forms import ResumeForm
from .models import ResumeModel

# Create your views here.

class home(View):

    def get(self,request):
        form = ResumeForm()
        return render(request,'resume/home.html',{'form':form})
    
    def post(self,request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            print('valid')
            form.save()
            print('saved')
            return redirect ('home')
        


class all_candidates(View):

    def get(self,request):

        form=ResumeModel.objects.all()
        print('query-set generated')
        return render(request,'resume/all_candidates.html',{'form':form})
    
    def post(self,request):
        return render(request,'resume/all_candidates.html')


class candidate_info(View):

    def get(self,request,pk):
        data=ResumeModel.objects.get(id=pk)
        return render(request,'resume/candidate_info.html',{'data':data})
    
    def post(self,request):
        return render(request,'resume/candidate_info.html')


class contact(View):

    def get(self,request):
        return render(request,'resume/contact.html')
    
    def post(self,request):
        return render(request,'resume/contact.html')


class about(View):

    def get(self,request):
        return render(request,'resume/about.html')
    
    def post(self,request):
        return render(request,'resume/about.html')

class delete(View):

    def get(self,request,pk):
        data=ResumeModel.objects.get(id=pk)
        data.delete()
        form=ResumeModel.objects.all()
        return render(request,'resume/all_candidates.html',{'form':form})
    
    def post(self,request):
        return render(request,'resume/home.html')
        
class update(View):

    def get(self,request,pk):
        data = ResumeModel.objects.filter(id=pk)
        # print(data.fname)
        for d in data:
            print(d.fname)
        return render(request,'resume/update.html',{'data':data})
    
    def post(self,request,pk):
        print('test working')
        print(pk)
        
        # get data

        data = ResumeModel.objects.get(id=pk)

        # get data in variables

        fname = request.POST['fname']
        lname = request.POST['lname']
        D_o_b = request.POST['D_o_b']
        locality = request.POST['locality']
        pin = request.POST['pin']
        contact = request.POST['contact']
        email = request.POST['email']
        # print(fname,lname,D_o_b,locality,pin,contact,email)

        #assign updated values in model

        data.fname=fname
        data.lname=lname
        data.locality = locality
        data.pin = pin
        data.contact=contact
        data.email=email
        data.save()
        
        # print(data.fname,data.lname,data.D_o_b,data.locality,data.pin,data.contact,data.email)
        form=ResumeModel.objects.all()
        return render(request,'resume/all_candidates.html',{'form':form})