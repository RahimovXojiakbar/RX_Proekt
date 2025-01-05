from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from shortuuid.django_fields import ShortUUIDField
from district.models import District


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

class Chairman(BaseModel):
    name = models.CharField(max_length=200)
    BIO = CKEditor5Field(config_name='extends', default = '<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')
    information =  models.CharField(max_length=200, choices=InformationLevel.choices)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFY(BaseModel):
    title = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True, related_name='d_MFY')
    chairman = models.OneToOneField(Chairman, on_delete=models.SET_NULL, null=True, related_name='c_MFY')
    area_km_kv = models.DecimalField(decimal_places=2, max_digits=10, default=15.75)
    neighborhoods = models.PositiveIntegerField(default=8)
    people = models.PositiveIntegerField(default=8500)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-uuid']

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class MFYStatistics(BaseModel):
    MFY = models.OneToOneField(MFY, on_delete=models.CASCADE, related_name='statistics', verbose_name="Mahalla fuqarolar yig'ini")
    total_budget = models.DecimalField(decimal_places=2, max_digits=15, default=0.0, verbose_name="MFY byudjeti")
    poverty_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Qashshoqlik darajasi (%)")
    literacy_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Savodxonlik darajasi (%)")
    unemployment_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Ishsizlik darajasi (%)")
    healthcare_facilities = models.PositiveIntegerField(default=0, verbose_name="Tibbiyot muassasalari soni")
    educational_institutions = models.PositiveIntegerField(default=0, verbose_name="Ta'lim muassasalari soni")
    industrial_units = models.PositiveIntegerField(default=0, verbose_name="Sanoat korxonalari soni")
    average_income_per_person = models.DecimalField(decimal_places=2, max_digits=10, default=0.0, verbose_name="Aholi boshiga o'rtacha daromad")
    birth_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="Tug'ilish ko'rsatkichi")
    death_rate = models.DecimalField(decimal_places=2, max_digits=5, default=0.0, verbose_name="O'lim ko'rsatkichi")
    change_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Statistics for {self.MFY.title}"

    class Meta:
        ordering = ['-uuid']


