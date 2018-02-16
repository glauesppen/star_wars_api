# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.test import APITestCase

BASE_PLANET = {
	'id': '1',
	'nome': 'Alderaan',
	'clima': 'temperate',
	'terreno': 'grasslands, mountains',
}

class PlanetsTests(APITestCase):

	def test_get_planets_list(self):
		response = self.client.get('/api/planets/')
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	def test_create_planets_list(self):
		response_data = {
			'id': '1',
			'nome': 'Alderaan',
			'clima': 'temperate',
			'terreno': 'grasslands, mountains',''
			'movies_counter': 2,
		}

		response = self.client.post('/api/planets/', BASE_PLANET, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(response.data, response_data)

	def test_delete_planet(self):
		planet = self.client.post('/api/planets/', BASE_PLANET, format='json').data
		response = self.client.delete('/api/planets/1/')
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT	)
