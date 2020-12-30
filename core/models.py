from django.db import models

"""core models"""


class TimeStampedModel (models.Model):
    """Time Stamped model"""
    created = models.DateTimeField(auto_now_add=True)  # model이 생성된 날짜 자동저장
    updated = models.DateTimeField(auto_now=True)  # model이 업데이트된 날짜 자동저장

    class Meta:
        abstract = True
        # abstract model은 DB로 가지 않음. 다른 model이 이걸 끌어와서 쓸수만 있지, DB admin으로 만들어지지 않음.
