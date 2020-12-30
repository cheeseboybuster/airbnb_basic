# application에 대한 작업을 시작하기전에 settings.py의 project_apps에 'apps.py' application의 config를 추가해줘야함.
# model에 대한 설명:https://docs.djangoproject.com/en/3.1/search/?q=no+such+table%3A+users_user
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    """ Custom User Model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
        (GENDER_OTHER, "Other"),
    )

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_KOREAN = "ko"

    LANGUAGE_CHOICES = (
        (LANGUAGE_ENGLISH, "english"),
        (LANGUAGE_KOREAN, "korean"),
    )

    CURRENCY_US = "USD"
    CURRENCY_KR = "KRW"

    CURRENCY_CHOICES = (
        (CURRENCY_US, "USD"),
        (CURRENCY_KR, "KRW"),
    )

    avatar = models.ImageField(blank=True)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    # null=True 는 아무정보가 없어도 괜찮다는 뜻 DB상
    # blank=True UI상 아무정보 입력안해도 괜찮다는 뜻.
    bio = models.TextField(blank=True)
    birthdate = models.DateField(blank=True, null=True)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=3, blank=True)
    currency = models.CharField(
        choices=CURRENCY_CHOICES, max_length=3, blank=True)
    superhost = models.BooleanField(default=False)
