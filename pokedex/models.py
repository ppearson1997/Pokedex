from django.db import models
from django.utils.translation import ugettext_lazy as _

def pokemon_upload_dir(instance, filename):
    return "pokemon/%s/%s" % (instance.id, filename)


class Pokemon(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    order = models.IntegerField(verbose_name=_('Order'))
    height = models.IntegerField(verbose_name=_('Height'))
    weight = models.IntegerField(verbose_name=_('Weight'))
    base_experience = models.IntegerField(default=0, verbose_name=_('Base Experience'))
    hp = models.IntegerField(default=0, verbose_name=_('HP'))
    attack = models.IntegerField(default=0, verbose_name=_('Attack'))
    defense = models.IntegerField(default=0, verbose_name=_('Defense'))
    special_attack = models.IntegerField(default=0, verbose_name=_('Special Attack'))
    special_defense = models.IntegerField(default=0, verbose_name=_('Special Defense'))
    speed = models.IntegerField(default=0, verbose_name=_('Speed'))
    image = models.ImageField(upload_to=pokemon_upload_dir, verbose_name=_('Image'), blank=True, null=True)

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemons"
        ordering = ['id']

    def __str__(self):
        return self.name


class PokemonType(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    description = models.CharField(max_length=255, verbose_name=_('Description'))
    
    class Meta:
        verbose_name = "Pokemon Type"
        verbose_name_plural = "Pokemon Types"
        ordering = ['name']

    def __str__(self):
        return self.name


class PokemonTypeSlot(models.Model):
    slot = models.IntegerField(verbose_name=_('Slot'))
    type = models.ForeignKey('pokedex.PokemonType', on_delete=models.CASCADE, verbose_name=_('Pokemon Type'))
    pokemon = models.ForeignKey('pokedex.Pokemon', on_delete=models.CASCADE, verbose_name=_('Pokemon'))
    
    class Meta:
        verbose_name = "Pokemon Type with Slot"
        verbose_name_plural = "Pokemon Types with Slot"
        ordering = ['pokemon', 'slot']

    def __str__(self):
        return self.pokemon.name


class PokemonAbility(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('Name'))
    effect = models.CharField(max_length=255, verbose_name=_('Effect'))
    short_effect = models.CharField(max_length=255, verbose_name=_('Short Effect'))
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Ability"
        verbose_name_plural = "Abilities"
        ordering = ['name']


class PokemonAbilitySlot(models.Model):
    slot = models.IntegerField(verbose_name=_('Slot'))
    ability = models.ForeignKey('pokedex.PokemonAbility', on_delete=models.CASCADE, verbose_name=_('Ability'))
    pokemon = models.ForeignKey('pokedex.Pokemon', on_delete=models.CASCADE, verbose_name=_('Pokemon'))

    def __str__(self):
        return self.pokemon.name
    
    class Meta:
        verbose_name = "Pokemon Ability with Slot"
        verbose_name_plural = "Pokemon Abilities with Slot"
        ordering = ['id']