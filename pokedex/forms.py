from django import forms
from . import models
from django.utils.translation import ugettext_lazy as _


class PokedexForm(forms.ModelForm):
    type =forms.ModelMultipleChoiceField(required=True,
                                        widget=forms.CheckboxSelectMultiple,
                                        queryset=models.PokemonType.objects.all())
    type_slot = forms.CharField(required=True, help_text = _('Add slot as many as the checked type and separate using comma.eg.(2,3,5)'))
    ability = forms.ModelMultipleChoiceField(required=True,
                                            widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check-inline'}),
                                            queryset=models.PokemonAbility.objects.all())
    ability_slot = forms.CharField(required=True, help_text = _('Add slot as many as the checked ability and separate using comma.eg.(2,3,5)'))

    class Meta:
        model = models.Pokemon
        fields = '__all__'