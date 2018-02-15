from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers

from planet.models import Planet


class PlanetSerializer(mongoserializers.DocumentSerializer):
	id = serializers.CharField(read_only=False)

	class Meta:
		model = Planet
		fields = '__all__'
