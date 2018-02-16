# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet

from planet.serializers import PlanetSerializer
from planet.models import Planet


class PlanetViewSet(MongoModelViewSet):
    lookup_field = 'id'
    serializer_class = PlanetSerializer

    def get_queryset(self):
        planetas = Planet.objects.all()

        nome = self.request.query_params.get('nome', None)

        if nome:
            planetas = planetas.filter(nome__icontains=nome)

        return planetas