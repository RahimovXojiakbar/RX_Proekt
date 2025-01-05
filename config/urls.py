"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Davlat Boshqaruvi Tizimi",
        description="Bu loyiha bir nechta ijtimoiy va siyosiy tuzilmalarni, masalan, davlat, mintaqalar, tumanlar, MFYlar, mahallalar va uylar bilan bog‘liq ma'lumotlarni saqlash uchun mo‘ljallangan. Har bir ob'ekt uchun shaxslar, ularning holati va boshqa parametrlar ham kiritiladi.",
        contact=openapi.Contact(email="rahimovxojiakbar69@gmail.com"),
        default_version='1.0.0',
        license=openapi.License(name='Loyiha Listsenziyasi'),
    ),
    public=True,
)

urlpatterns = [

    path('admin/', admin.site.urls),
    path('state/', include('state.urls')),
    path('region/', include('region.urls')),
    path('district/', include('district.urls')),
    path('MFY/', include('MFY.urls')),
    path('neighborhood/', include('neighborhood.urls')),
    path('house/', include('house.urls')),
    path('human/', include('human.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name='schema-swagger'),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name='schema-redoc'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
