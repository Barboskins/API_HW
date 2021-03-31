# TODO: опишите сериализаторы
from rest_framework import serializers

from measurements.models import Project, Measurement


class ProjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    project = serializers.StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = [
           'id',
           'name',
           'latitude',
           'longitude',
           'created_at',
           'updated_at',
           'project'
        ]


class MeasurementSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = [
            'id',
            'value',
            'project',
        ]