from rest_framework import serializers
from reports.models import Report

class ReportSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Report
        fields = ('transcript', 'gps_lat', 'gps_long', 'moving', 'pub_date')
