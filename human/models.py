from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField
from django.contrib.auth.models import User
from house.models import House


class MyShortUuid(models.Model):
    uuid = ShortUUIDField(
        primary_key=True,
        editable=False,
        max_length=12,
        alphabet = 'abcdefghijklmnopqrstuvwxz123456789',
    )
    
    class Meta:
        abstract  = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class BaseModel(MyShortUuid):
    created = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class InformationLevel(models.TextChoices):
    HIGH = 'HIGH'
    MIDDLE = 'MIDDLE'
    NO = 'NO'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Status(models.TextChoices):
    KINDERGARTEN = 'Kindergarten'
    SCHOOLBOY = 'Schoolboy'
    STUDENT = 'Student'
    WORKER = 'Worker'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Human(BaseModel):
    name = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    email = models.EmailField(default='example@mail.ru')
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    status = models.CharField(max_length=200, choices=Status.choices)
    information = models.CharField(max_length=200, choices=InformationLevel.choices, default=InformationLevel.NO)
    house = models.ForeignKey(House, on_delete=models.SET_NULL, null=True, related_name='human')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class HumanStatistics(BaseModel):
    human = models.OneToOneField(Human, on_delete=models.CASCADE, related_name="statistics")
    education_level = models.CharField(max_length=100, default="Middle", verbose_name="Ta'lim darajasi")
    working_hours_per_week = models.PositiveIntegerField(default=0, verbose_name="Haftalik ish soatlari")
    gender_distribution = models.CharField(max_length=50, choices={'MALE':'MALE', 'FAMALE':'FAMALE','OTHER':'OTHER'}, verbose_name="Jins")
    living_space_per_person = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Uyda har bir a'zoga to'g'ri keladigan maydon (m²)")

    def __str__(self):
        return f"{self.human.name} statistikasi"
    
    class Meta:
        ordering = ['uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    BIO = models.TextField(default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user
    
    class Meta:
        ordering = ['-uuid']


