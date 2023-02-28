from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Profiles, Technologies, Courses
from django.forms import ModelForm
from .models import *



class ProfileUpdateForm(UserCreationForm):
    username = forms.CharField()
    agency = forms.CharField(max_length=100)
    profile_image = forms.ImageField()
    private = forms.BooleanField()
    goals = forms.Textarea()
    bio = forms.Textarea()
    github = forms.URLField()
    linkedin = forms.URLField()
    website = forms.URLField()
    my_tags = forms.CharField()
    my_courses = forms.CharField()

    class Meta:
        model = Profiles
        fields = (
            'username',
            'agency',
            'profile_image',
            'private',
            'goals',
            'bio',
            'github',
            'linkedin',
            'website',
            'my_tags',
            'my_courses',
        )


class AddTechForm(forms.ModelForm):  
    class Meta:
        model = Technologies
        fields = (
            'title',
            'description',
            'link',
            'tech_image',
            )

    def __init__(self, *args, **kwargs):
        super(AddTechForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})




    # title = forms.CharField()   
    # description = forms.CharField()
    # link = forms.URLField()
    # tech_image = forms.ImageField()

    # class Meta:
    #     model = Technologies
        # fields = (
        #     'title',
        #     'description',
        #     'link',
        #     'tech_image',
        #     )


class TechChangeForm(forms.Form): 
    title = forms.CharField()   
    description = forms.CharField(widget=forms.Textarea)
    link = forms.URLField()


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


class UserChangeForm(UserCreationForm):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()


    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            
        )


class NewCourseForm(forms.Form):
    title = forms.CharField()
    level = forms.IntegerField()
    cost = forms.CharField()
    length = forms.CharField()
    link = forms.URLField()
    website = forms.URLField()
    instructor = forms.CharField()
    course_image = forms.ImageField()
    description = forms.Textarea()

    class Meta:
        model = Courses
        fields = (
            'title',
            'level',
            'cost',
            'length',
            'link',
            'website',
            'instructor',
            'course_image',
            'description'
        )



class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=100, label="First Name")
    last_name = forms.CharField(max_length=100, label="Last Name")
    email = forms.EmailField(required=True, label ="Your Email Address")
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

   