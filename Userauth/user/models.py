from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomerUserManager
from django.template.defaultfilters import slugify 
from .utils import generate_random_id
# Create your models here.

class CustomerUser(AbstractUser):
    # add additional fields in here
    # first_name = models.CharField(max_length=50)
    # last_name = models.CharField(max_length=50)
    # email = models.EmailField(max_length=50)
    # password = models.CharField(max_length=50)
    # is_active = models.BooleanField(default=True)
    # is_staff = models.BooleanField(default=False)
    # is_superuser = models.BooleanField(default=False)
    # last_login = models.DateTimeField(default=timezone.now)
    # date_joined = models.DateTimeField(default=timezone.now)
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['first_name', 'last_name']
    # def __str__(self):
    #     return self.email
    
    username = None
    email = models.EmailField(unique=True)
    slug = models.SlugField(blank=True, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'CustomerUser'
        ordering = ['email']


    def __str__(self):
        return self.email


    objects = CustomerUserManager()

    # create  a default slug /username for user if blank

    def save(self, *args, **kwargs):
        if not self.slug:
            # create a slug

           random_slug=slugify(self.first_name + self.last_name+generate_random_id())
           while CustomerUser.objects.filter(slug=random_slug).exists():
               random_slug=slugify(self.first_name + self.last_name+generate_random_id())
           self.slug = random_slug
        super().save(*args, **kwargs)