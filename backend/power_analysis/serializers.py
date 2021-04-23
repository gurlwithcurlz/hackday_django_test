from rest_framework import serializers
from .models import PowerAnalysis

class PowerAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerAnalysis
        fields = ('id', 'base_conversion', 'a_grade_proportion', 'uplift', 'days_max', 'calls_per_day')
