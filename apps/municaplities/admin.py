from django.contrib import admin

# Register your models here.
from apps.municaplities.models import Province, District, Municipalities


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'name',
    )


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'name',
        'province'
    )

@admin.register(Municipalities)
class DistrictAdmin(admin.ModelAdmin):
    list_display = (
        # 'id',
        'name',
        'district'
    )
