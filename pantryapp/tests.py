import json
from django.test import TestCase
from .models import PantryItem
from .views import pantry_match, DEMO_RECIPES

class PantryApiTests(TestCase):
    def test_inventory_create_and_metrics(self):
        response=self.client.post('/api/pantry', data=json.dumps({'name':'Tomato','quantity':3,'unit':'piece'}), content_type='application/json')
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.json()['name'],'Tomato')
        self.assertEqual(self.client.get('/api/metrics').json()['pantry_items'],1)

    def test_invalid_inventory_is_rejected(self):
        response=self.client.post('/api/pantry', data=json.dumps({'name':' '}), content_type='application/json')
        self.assertEqual(response.status_code,400)

    def test_recipe_matcher_ranks_ingredient_overlap(self):
        result=pantry_match(DEMO_RECIPES,['tomato','chickpea','onion','rice'])
        self.assertEqual(result[0]['title'],'Smoky chickpea tomato bowls')
        self.assertEqual(result[0]['match'],100)
