from django.db import models
from django_countries.fields import CountryField  # third party 패키지
from core import models as core_models  # 코어에서 model을 가져오는데 core_models로 명명해서.
from users import models as user_models  # user_models만들어놓은걸 host에 적용하기위해 가져옴


class abstractItem(core_models.TimeStampedModel):

    """Abstract Item"""
    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(abstractItem):
    class Meta:
        verbose_name = "Room Type"  # 대신보여줄이름
        ordering = ["created"]  # 오더순서


class Amenity(abstractItem):
    class Meta:
        verbose_name_plural = "Amenities"
        ordering = ["name"]


class Facility(abstractItem):
    class Meta:
        verbose_name_plural = "Facilities"
        ordering = ["name"]


class HouseRule(abstractItem):
    class Meta:
        verbose_name = "House Rule"


class Photo(core_models.TimeStampedModel):

    caption = models.CharField(max_length=150)
    file = models.ImageField()
    room = models.ForeignKey("Room", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption  # 자기캡션이름을 사진이름대신보여줘라


class Room(core_models.TimeStampedModel):
    class Meta:
        verbose_name = "Room"

    """Room Model Definition"""

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    guests = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey("users.User", on_delete=models.CASCADE)
    # 1대다, 1:Many일때는 ForeignKey를 사용해 연결. 여기서는 host를 미리만들어 둔 user model이랑 연결.1명의 호스트에 여러 유저가 연결 가능.
    room_type = models.ForeignKey(
        RoomType, on_delete=models.SET_NULL, null=True, blank=True)
    amenities = models.ManyToManyField("Amenity", blank=True)
    # 다대다, Many to Many인 relationship에는 ManytoManyField를 사용해 연결. 여기서는 amenities를 여러개 룸에 연결 가능.
    facilities = models.ManyToManyField("Facility", blank=True)
    house_rules = models.ManyToManyField("HouseRule", blank=True)

    # country경우 장고에서 제공하는 country 패키지 깔아서 사용 https://pypi.org/project/django-countries/
    # installation부분참고하여 인스톨

    def __str__(self):
        return self.name
    # 어드민에 룸의이름이 리스트에 보이게 해줌.
