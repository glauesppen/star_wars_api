# -*- coding: utf-8 -*-
import requests

from mongoengine import Document, EmbeddedDocument, fields


class Planet(Document):
	id = fields.IntField(required=True, primary_key=True)
	nome = fields.StringField(required=True)
	clima = fields.StringField(required=True, null=True)
	terreno = fields.StringField(required=True, null=True)
	movies_counter = fields.IntField(null=True)


	def save(self, *args, **kwargs):
		api_response = requests.get('https://swapi.co/api/planets/?search=%s' % self.nome)
		if api_response.status_code == 200 and api_response.json()['count'] == 1:
			planet = api_response.json()['results'][0] 
			
			self.movies_counter = len(planet['films'])

			if not self.clima:
				self.clima = planet['climate']

			if not self.terreno:
				self.terreno = planet['terrain']

		super(Planet, self).save(*args, **kwargs)