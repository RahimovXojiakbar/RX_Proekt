from django.db import models
from shortuuid.django_fields import ShortUUIDField
from MFY.models import MFY


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

class Neighborhood(BaseModel):   
    title = models.CharField(max_length=200)
    elder = models.CharField(max_length=250, default='Jhon Doe')
    MFY = models.ForeignKey(MFY, on_delete=models.SET_NULL, null=True)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=15, default=4.65)
    houses = models.PositiveIntegerField(default=85)
    people = models.PositiveIntegerField(default=530)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class NeighborhoodStatistics(BaseModel):
    neighborhood = models.OneToOneField(Neighborhood, on_delete=models.CASCADE, related_name="statistics", verbose_name="Mahalla")
    population_density = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="Aholi zichligi (kishi/km²)")
    unemployment_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.0, verbose_name="Ishsizlik darajasi (%)")
    avg_income = models.DecimalField(max_digits=10, decimal_places=2, default=0.0, verbose_name="O'rtacha daromad (so'm)")
    young_population = models.PositiveIntegerField(default=0, verbose_name="Kichik yoshdagi aholi (0-14)")
    working_population = models.PositiveIntegerField(default=0, verbose_name="Ishchi yoshdagi aholi (15-64)")
    elderly_population = models.PositiveIntegerField(default=0, verbose_name="Keksaygan yoshdagi aholi (65+)")
    education_high = models.PositiveIntegerField(default=0, verbose_name="Oliy ta'lim olganlar")
    education_middle = models.PositiveIntegerField(default=0, verbose_name="O'rta ta'lim olganlar")
    no_education = models.PositiveIntegerField(default=0, verbose_name="Ta'lim olmaganlar")
    good_houses = models.PositiveIntegerField(default=0, verbose_name="Yaxshi sharoitdagi uylar")
    average_houses = models.PositiveIntegerField(default=0, verbose_name="O'rta sharoitdagi uylar")
    poor_houses = models.PositiveIntegerField(default=0, verbose_name="Yomon sharoitdagi uylar")

    def __str__(self):
        return f"{self.neighborhood.title} statistikasi" 

    class Meta:
        ordering = ['uuid']


