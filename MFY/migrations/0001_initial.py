# Generated by Django 5.1.4 on 2025-01-05 07:23

import django.db.models.deletion
import django_ckeditor_5.fields
import shortuuid.django_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz123456789', editable=False, length=22, max_length=12, prefix='', primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('BIO', django_ckeditor_5.fields.CKEditor5Field(default='<p> Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque at ligula purus. Praesent aliquet ipsum risus, nec interdum nunc tempus quis. Proin ultricies mauris urna, vel sagittis libero fermentum in. Sed eleifend varius nisl eu ullamcorper. Vestibulum condimentum cursus pretium. Aenean sed nibh ac dui pulvinar porttitor ut id neque. Sed consequat sapien sed magna venenatis lacinia. Praesent ullamcorper dignissim viverra. Curabitur ac odio et ante volutpat condimentum. Pellentesque eu faucibus ipsum. Sed est ante, accumsan id tortor vitae, vestibulum auctor magna. Vivamus in neque neque. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Aliquam non leo sit amet nunc maximus bibendum vitae fringilla ex. </p>')),
                ('information', models.CharField(choices=[('HIGH', 'High'), ('MIDDLE', 'Middle'), ('NO', 'No')], max_length=200)),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='MFY',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz123456789', editable=False, length=22, max_length=12, prefix='', primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('title', models.CharField(max_length=200)),
                ('area_km_kv', models.DecimalField(decimal_places=2, default=15.75, max_digits=10)),
                ('neighborhoods', models.PositiveIntegerField(default=8)),
                ('people', models.PositiveIntegerField(default=8500)),
                ('chairman', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='c_MFY', to='MFY.chairman')),
                ('district', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='d_MFY', to='district.district')),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
        migrations.CreateModel(
            name='MFYStatistics',
            fields=[
                ('uuid', shortuuid.django_fields.ShortUUIDField(alphabet='abcdefghijklmnopqrstuvwxz123456789', editable=False, length=22, max_length=12, prefix='', primary_key=True, serialize=False)),
                ('created', models.DateField(auto_now_add=True)),
                ('total_budget', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, verbose_name='MFY byudjeti')),
                ('poverty_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Qashshoqlik darajasi (%)')),
                ('literacy_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Savodxonlik darajasi (%)')),
                ('unemployment_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Ishsizlik darajasi (%)')),
                ('healthcare_facilities', models.PositiveIntegerField(default=0, verbose_name='Tibbiyot muassasalari soni')),
                ('educational_institutions', models.PositiveIntegerField(default=0, verbose_name="Ta'lim muassasalari soni")),
                ('industrial_units', models.PositiveIntegerField(default=0, verbose_name='Sanoat korxonalari soni')),
                ('average_income_per_person', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name="Aholi boshiga o'rtacha daromad")),
                ('birth_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name="Tug'ilish ko'rsatkichi")),
                ('death_rate', models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name="O'lim ko'rsatkichi")),
                ('change_at', models.DateTimeField(auto_now_add=True)),
                ('MFY', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='statistics', to='MFY.mfy', verbose_name="Mahalla fuqarolar yig'ini")),
            ],
            options={
                'ordering': ['-uuid'],
            },
        ),
    ]