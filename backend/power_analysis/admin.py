from django.contrib import admin
from .models import PowerAnalysis


class PowerAnalysisAdmin(admin.ModelAdmin):
    list_display = ('base_conversion', 'a_grade_proportion', 'uplift', 'days_max', 'calls_per_day')


# Register your models here.
admin.site.register(PowerAnalysis, PowerAnalysisAdmin)