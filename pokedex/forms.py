from django.forms import ModelForm
from . import models


class PokedexForm(ModelForm):
    class Meta:
        model = models.Pokemon
        fields = '__all__'