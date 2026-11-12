from django.db import models

class PantryItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.DecimalField(max_digits=8, decimal_places=2, default=1)
    unit = models.CharField(max_length=24, default='item')
    category = models.CharField(max_length=32, default='Other')
    expires_on = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['expires_on', 'name']

    def as_dict(self):
        return {'id': self.id, 'name': self.name, 'quantity': float(self.quantity), 'unit': self.unit,
                'category': self.category, 'expires_on': self.expires_on.isoformat() if self.expires_on else None}

class SavedRecipe(models.Model):
    title = models.CharField(max_length=140)
    ingredients = models.JSONField(default=list)
    instructions = models.TextField(blank=True)
    servings = models.PositiveSmallIntegerField(default=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def as_dict(self):
        return {'id': self.id, 'title': self.title, 'ingredients': self.ingredients,
                'instructions': self.instructions, 'servings': self.servings}

class ShoppingItem(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=40, blank=True)
    checked = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['checked', 'name']

    def as_dict(self):
        return {'id': self.id, 'name': self.name, 'quantity': self.quantity, 'checked': self.checked}
