from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField



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

class President(BaseModel):
    name = models.CharField(max_length=200)
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)
    party = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class State(BaseModel):
    title = models.CharField(max_length=200)
    president = models.OneToOneField(President, on_delete=models.SET_NULL, null=True, related_name='state')
    about = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    flag = models.ImageField(blank=True, upload_to='images')
    anthem = models.TextField(default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    emblem = models.ImageField(upload_to='images', blank=True)
    language = models.CharField(max_length=200)
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=450.54)
    regions = models.PositiveIntegerField(default=13)
    people = models.PositiveIntegerField(default=40000000)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class StateStatistics(BaseModel):
    state = models.OneToOneField(State, on_delete=models.CASCADE, related_name='statistics')
    gdp = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name='Umumiy ichki mahsulot (GDP)')
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name=' Ishsizlik darajasi')
    inflation_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Inflyatsiya darajasi') 
    poverty_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Qashshoqlik darajasi')
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Savodxonlik darajasi')
    life_expectancy = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Hayot davomiyligi')
    population_growth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Aholi o'sish darajasi")
    urban_population_percentage = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name='Shahar aholisi foizi')
    birth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Tug'ilish darajasi")
    death_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="O'lim darajasi")
    changed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Statistics for {self.state.title}"

    class Meta:
        ordering = ['-uuid']

