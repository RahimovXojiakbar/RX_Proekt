from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField
from state.models import State


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

class Governor(BaseModel):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Region(BaseModel):
    title = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, related_name='region')
    governor = models.OneToOneField(Governor, on_delete=models.SET_NULL, null=True, related_name='region')
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    districts = models.PositiveIntegerField(default=8)
    people = models.PositiveIntegerField(default=2500000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class RegionStatistics(BaseModel):
    region = models.OneToOneField(Region, on_delete=models.CASCADE, related_name='statistics')
    total_area_km2 = models.DecimalField(decimal_places=2, max_digits=10, default=0.0)
    population_density = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, verbose_name='aholi zichligi')  
    gdp = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name='yalpi ichki mahsulot')  
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='ishga joylashish darajasi') 
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='savodxonlik darajasi')
    median_income = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name="o'rtacha daromad")
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Statistics for {self.region.title}"
 
    class Meta:
        ordering = ['uuid']

