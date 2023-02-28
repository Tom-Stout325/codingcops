from django.urls import path
from .views import * 
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', HomePage, name='home'),
    path('contact/', ContactPage, name="contact"),
    path('contact/thanks/', Thanks, name='thanks'),
    path('info/', TechTemplateView.as_view(), name='info'),

    path('tech/', TechTemplateView.as_view(), name='tech'),
    path('tech-add/', AddTech, name='newtech'),
    path('tech-dtl/<slug:slug>/', TechDtl.as_view(), name='techdtl'),

    path('courses', CoursesView.as_view(), name="courses"),
    path('courses/<slug:slug>/', CourseDetail.as_view(), name='courseDtl'),

    path('profiles/', AllProfiles.as_view(), name='profiles'), 
    path('profiles/<slug:slug>', ProfileDtl.as_view(), name='profilesDtl'), 
    path('profile/', MyProfile, name='profile'),
    #path('profile_update', ProfileUpdate.as_view(),'profile_update'),
    
    
    path('register/', UserRegisterView.as_view(), name='register'),
    path('password/', PasswordsChangeView.as_view(template_name="registration/change-password.html")),
    path('edit-user/', UserChangeForm.as_view(template_name='registration/user_edit_form.html')),
   # path('edit-profile/', ProfileChangeForm.as_view(template_name='registration/profile_form.html'), name='edit-profile')

]