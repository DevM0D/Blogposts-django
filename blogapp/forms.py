from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from django import forms 
from .models import post , Catagory , Coment

# choices = [('Coding','Coding'), ('Sports' ,'Sports') , ('Social Media','Social Media')]

choices = Catagory.objects.all().values_list('name','name')

choices_list = []

for item in choices :
    choices_list.append(item)

class UserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ("username", "email", "password1" ,"password2")
       


class postForm(forms.ModelForm):
    class Meta:
        model = post
        fields = ('title' , 'author' , 'title_tags' , 'catagory' , 'body', 'imgup')

        widgets ={
            'title' :forms.TextInput(attrs={'class': 'form-control'}),
            # 'author' :forms.Textarea(attrs={'class': 'form-control' , 'value':'' , 'id' : 'elder' , 'disabled' : '' }),
            'author' :forms.Select(attrs={'class': 'form-control', }),
            'title_tags' :forms.TextInput(attrs={'class': 'form-control'}),
            'catagory' :forms.Select(choices=choices_list , attrs={'class': 'form-control'}),
            'body' :forms.Textarea(attrs={'class': 'form-control'}),
            'imgup': forms.ClearableFileInput(attrs={'multiple': True}),
 

        
}

class AddCommentform(forms.ModelForm):
    class Meta:
        model = Coment
        fields = ("name" , 'body')

        widgets ={
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body':forms.Textarea(attrs={'class': 'form-control'}),
}