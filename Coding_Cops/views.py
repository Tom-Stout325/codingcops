from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django import forms
from .models import Technologies, Profiles, Courses
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from .forms import RegisterForm, UserChangeForm, TechChangeForm, NewCourseForm, ContactForm, AddTechForm, ProfileUpdateForm
from django.views.generic.edit import FormView
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.http import HttpResponseRedirect


def HomePage(request):
    return render(request, 'Coding_Cops/home.html')

def InfoPage(request):
    tech = Technologies.objects.all()
    context = {'tech': tech}
    return render(request, 'Coding_Cops/info.html', context)


def ContactPage(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            html = render_to_string('Coding_Cops/contact.html', {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'subject': subject,
                'message': message,
            })

            send_mail('{{ self.subject }}', '{{ self.message }}', 'tom.stout325@gmail.com', ['tom.stout325@gmail.com'], html_message=html)

            return redirect('thanks')
    else:
        form = ContactForm()

    return render(request, 'Coding_Cops/contact.html', {
        'form': form
    })



def Thanks(request):
    return render(request, 'Coding_Cops/contact_thanks.html')



# def InfoPage(request):
#     tech = Technologies.objects.all()
#     context = {'tech': tech}
#     return render(request, 'Coding_Cops/info.html', context)



class UserRegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


class UserChangeForm(generic.UpdateView):
    form_class = UserChangeForm
    template_name = 'registration/user_edit_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')


class AllProfiles(generic.ListView):
    template_name = 'Coding_Cops/profiles.html'
    model = Profiles

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profiles'] = Profiles.objects.all()
        return context


class ProfileDtl(generic.DetailView):
    template_name = 'Coding_Cops/profile-dtl.html'
    model = Profiles
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        return context



# def AddTechForm(request):
#     my_tags = Technologies.objects.all()
#     context = { 
#         'my_tags': my_tags
#     }
#     return render(request, 'Coding_Cops/tech_form.html', context)


def Add_Tech(request):
    form = AddTechForm(request.POST)
    print(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('thanks')

    else:
        form = AddTechForm()
        
    context = {
        'form': form
    }
    return render(request, 'Coding_Cops/tech_form.html', context=context)
        
    #     if form.is_valid():
    #     #     title = form.cleaned_data['title']
    #     #     description = form.cleaned_data['description']
    #     #     link = form.cleaned_data['link']
    #     #     tech_image = form.cleaned_data['tech_image']
            
    #         form.save()
    #     return redirect('thanks')

    # else:
    #     form = AddTechForm()



class CourseDetail(generic.DetailView):
    template_name = 'Coding_Cops/Courses_dtl.html'
    model = Courses
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Courses.objects.filter(slug=self.kwargs.get('slug'))
        return context



@login_required(login_url='login')
def MyProfile(request):
    profile = request.user.profiles

    context = {'profile': profile}
    return render(request, 'Coding_Cops/profile.html', context)






def AddTech(request):
    profile = request.user.profiles
    form = AddTechForm()

    if request.method == 'POST':
        form = AddTechForm(request.POST, request.FILES)
        if form.is_valid():
            my_tech = form.save(commit=False)
            my_tech.owner = profile
            my_tech.save()
            #messages.success(request, 'my_tech was added successfully!')
            return redirect('newtech')

    context = {'form': form}
    return render(request, 'Coding_Cops/tech_form.html', context)





# class ProfileUpdate(generic.UpdateView):
#     form_class = ProfileUpdateForm
#     template_name_sufix = 'registration/profile_form.html'
#     success_url = reverse_lazy('profile')


#     fields = (
#             ['username'],
#             ['agency'],
#             ['profile_image'],
#             ['private'],
#             ['goals'],
#             ['bio'],
#             ['github'],
#             ['linkedin'],
#             ['website'],
#             ['my_tags'],
#             ['my_courses'],
#     )

    # username = forms.CharField()
    # agency = forms.CharField(max_length=100)
    # profile_image = forms.ImageField()
    # private = forms.BooleanField()
    # goals = forms.Textarea()
    # bio = forms.Textarea()
    # github = forms.URLField()
    # linkedin = forms.URLField()
    # website = forms.URLField()
    # my_tags = forms.CharField()
    # my_courses = forms.CharField()

    # class Meta:
    #     model = Profiles
    #     fields = (
    #         'username',
    #         'agency',
    #         'profile_image',
    #         'private',
    #         'goals',
    #         'bio',
    #         'github',
    #         'linkedin',
    #         'website',
    #         'my_tags',
    #         'my_courses'
    #     )
            


class TechTemplateView(generic.ListView):
    template_name = 'Coding_Cops/info.html'
    model = Technologies
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tech'] = Technologies.objects.all()
        return context


class TechDtl(generic.DetailView):
    template_name = 'Coding_cops/tech_dtl.html'
    model = Technologies
    context_object_name = 'tech'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tech = Technologies.objects.filter(slug=self.kwargs.get('slug'))
        return context




class CoursesView(generic.ListView):
    template_name = 'Coding_Cops/Courses_list.html'
    model = Technologies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['course'] = Courses.objects.all()
        return context


class CourseDetail(generic.DetailView):
    template_name = 'Coding_Cops/Courses_dtl.html'
    model = Courses
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = Courses.objects.filter(slug=self.kwargs.get('slug'))
        return context
