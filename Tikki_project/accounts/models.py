from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager


COUNTRIES = (
    ('', 'Select Country'),
    ('US', 'United States of America'),
    ('NG', 'Nigeria'),
    ('GB', 'Great Britain'),
    ('CN', 'China'),
    ('GH', 'Ghana'),
    ('KE', 'Kenya'),
    ('NL', 'The Netherlands'),
    ('IS', 'Israel')
)

BUSINESS_CATEGORIES = (
    ('', 'Select a category'),
    ('general', 'General'),
    ('contract', 'Contracting/Consultancy'),
    ('agriculture', 'Agriculture'),
    ('ecommerce', 'Ecommerce'),
    ('tech', 'Technology and IT'),
    ('consultancy', 'Consultancy'),
    ('ngo', 'Not-for-profit/NGO'),
    ('publishing', 'Writing and Publishing'),
    ('blogging', 'Blogging'),
    ('trading', 'Trading - Buying and Selling'),
    ('education', 'Education and EduTech'),
    ('adventure', 'Adventure'),
    ('travels', 'Travels and Tourism'),
    ('sports', 'Sports'),
    ('music', 'Music and Entertainment'),
    ('foodspitality', 'Food and Hospitality'),
    ('delivery', 'Delivery and Logistics'),
    ('freelancing', 'Freelancing'),
    ('adventure', 'Adventure'),
    ('aerospace', 'Aerospace and Aviation'),
    ('security', 'Security'),
    ('others', 'Others'),

)

COMPANY_SIZE = (
    ('', 'Select an option'),
    ('justme', 'Just Me'),
    ('lessthan10', '1-10'),
    ('less50', '11-50'),
    ('50less200', '51-200'),
    ('200less500', '201-500'),
    ('500less1000', '501-1000'),
    ('1kless5k', '1001-5,000'),
    ('5kless10k', '5001-10,000'),
    ('greaterthan10k', '10,000+'),

)


class CustomUser(AbstractUser):
    firstname = models.CharField(_('First Name'), max_length=255)
    lastname = models.CharField(_('First Name'), max_length=255)
    business_name = models.CharField(_('Business/Company Name'), max_length=255)
    phone_number = models.CharField(_('Phone Number'), max_length=13)
    email = models.CharField(_('Email'), max_length=255, unique=True)
    country = models.CharField(_('Country'), choices=COUNTRIES, max_length=100)
    state = models.CharField(_('State/Province'), max_length=255)
    city = models.CharField(_('City'), max_length=150)
    zipcode = models.CharField(_('Zip Code'), max_length=10)
    business_category = models.CharField(_('Business Category'), choices=BUSINESS_CATEGORIES, max_length=150)
    company_size = models.CharField(_('Company Size'), choices=COMPANY_SIZE, max_length=150)
    datejoined = models.DateField(auto_now_add=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
