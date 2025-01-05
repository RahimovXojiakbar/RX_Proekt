from django.db import models
from shortuuid.django_fields import ShortUUIDField
from neighborhood.models import Neighborhood


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

class House(BaseModel):
    house_boss = models.CharField(max_length=200)
    house_number= models.PositiveIntegerField()
    a_b = models.CharField(max_length=200, choices={ 'A':'A', 'B':'B'})
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.SET_NULL, null=True, related_name='house')
    status = models.CharField(max_length=200, choices={'POORER':'POORER', 'MIDDLE':'MIDDLE','RICH':'RICH'})
    people = models.PositiveIntegerField(blank=True, default=5)
    area_kv_m = models.DecimalField(decimal_places=2, max_digits=15, default=415.5)

    def __str__(self) -> str:
        return f"{self.house_number} {self.a_b}"

    class Meta:
        ordering = ['house_number', 'a_b']
  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class HouseStatistics(BaseModel):
    house = models.OneToOneField(House, on_delete=models.CASCADE, related_name="statistics", verbose_name="Uy")
    education_high = models.PositiveIntegerField(default=0, verbose_name="Oliy ta'lim olganlar")
    education_middle = models.PositiveIntegerField(default=0, verbose_name="O'rta ta'lim olganlar")
    no_education = models.PositiveIntegerField(default=0, verbose_name="Ta'lim olmaganlar")
    electricity_available = models.BooleanField(default=False, verbose_name="Elektr energiyasi mavjudligi")
    water_available = models.BooleanField(default=False, verbose_name="Suv ta'minoti mavjudligi")
    gas_available = models.BooleanField(default=False, verbose_name="Gaz ta'minoti mavjudligi")

    def __str__(self):
        return f"{self.house.house_number} {self.house.a_b} statistikasi"

    class Meta:
        ordering = ['uuid']


