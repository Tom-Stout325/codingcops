from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse



class Profiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    agency = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='images/', default="images/user-default.png")
    private = models.BooleanField(default=False)
    goals = models.TextField(default="Workin on it,  Please check back!", blank=False, null=False)
    bio = models.TextField(default="Workin on it, Please check back!", blank=False, null=False)
    social_github = models.URLField(max_length=300, blank=True, null=True)
    social_linkedin = models.URLField(max_length=300, blank=True, null=True)
    social_website = models.URLField(max_length=300, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default="", blank=True, null=True)

    def __str__(self):
        return str(self.slug)

    class Meta:
        verbose_name_plural = "Profiles"
        ordering = ['slug']

    def get_absolute_url(self):
        return reverse("profile", kwargs={"slug": self.slug})
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.user)
        super().save(*args, **kwargs)



class Courses(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    cost = models.CharField(max_length=20, blank=True, null=True)
    length = models.CharField(max_length=300, blank=True, null=True)
    link = models.URLField(max_length=300, blank=True, null=True)
    website = models.URLField(max_length=300, blank=True, null=True)
    instructor = models.CharField(max_length=300, blank=True, null=True)
    course_image = models.ImageField()
    description = models.TextField()
    slug = models.SlugField(max_length=300,  default="", null=False)

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = "Courses"
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("courses", kwargs={"slug": self.slug})



class Technologies(models.Model):
    title = models.CharField(max_length=300, blank=False, null=False)
    description = models.TextField()
    link = models.URLField(max_length=300, blank=False, null=False)
    tech_image = models.ImageField(null=True, blank=True, upload_to='images/', default="images/user-default.png")
    slug = models.SlugField(unique=True, default="", null=False)

    def get_absolute_urs(self):
        return reverse("tech-dtl", args=self.slug)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Tech"
        ordering = ['title']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Tags(models.Model):
    name = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"
        ordering = ['name']

class Contacts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    
    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Contacts"
        ordering = ['email']
