from django import forms
from .models import ResumeModel



gender_choice = [('male','male'),('female','female'),('not to prefer','not to prefer')]
lang_choice = [('Hindi','Hindi'),('English','English'),('Marathi','Marathi')] 
prefered_language_choice = [('python','python'),('javascript','javascript'),('HTML','HTML'),('css','css'),('bootstrap','bootstrap')]

class ResumeForm(forms.ModelForm):

    
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect())
    prefered_language=forms.MultipleChoiceField(choices=prefered_language_choice,widget=forms.CheckboxSelectMultiple())
    language = forms.MultipleChoiceField(choices=lang_choice,widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ResumeModel        
        fields =  ['fname','lname','D_o_b','gender','language','locality','city','state','pin','contact','email','prefered_language','profile_photo']
        
        labels = {
            'fname':'First Name ',
            'lname': 'Last Name ',
            'D_o_b': 'Date Of Birth ',
            'language': 'Language Spoken ',
            'locality':'Locality ',
            'city':'City ' ,
            'state':'State ',
            'pin':'Pin ',
            'contact':'Contact ',
            'email':'Email ',
            'profile_photo':'Profile Photo ',
        }

        widgets = {
            'fname': forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'D_o_b':forms.DateInput(attrs={'class':'form-control'}),
            # 'language':forms.TextInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'city':forms.Select(attrs={'class':'form-control'}),  
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'contact':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            
            
        }