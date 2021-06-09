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
    
    def __init__(self, *args, **kwargs):
        super(PokedexForm, self).__init__(*args, **kwargs)
        self.initial['type']= models.PokemonTypeSlot.objects.filter(pokemon__id=self.instance.id).values_list('type_id', flat=True)
        self.initial['ability']= models.PokemonAbilitySlot.objects.filter(pokemon__id=self.instance.id).values_list('ability_id', flat=True)
        ts, init_val = [], []
        for i in models.PokemonTypeSlot.objects.filter(pokemon__id=self.instance.id):
            ts.append(str(i.slot))
        self.initial['type_slot'] = ','.join(ts)
        for i in models.PokemonAbilitySlot.objects.filter(pokemon__id=self.instance.id):
            init_val.append(str(i.slot))
        self.initial['ability_slot']= ','.join(init_val)
        