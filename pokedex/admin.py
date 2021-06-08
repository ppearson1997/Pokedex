from django.contrib import admin
from pokedex import models

@admin.register(models.Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order', 'height', 'weight',
                    'hp', 'attack', 'defense', 'special_attack',
                    'special_defense', 'speed')


@admin.register(models.PokemonType)
class PokemonTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','description')


@admin.register(models.PokemonTypeSlot)
class PokemonTypeSlotAdmin(admin.ModelAdmin):
    list_display = ('id',  'slot', 'type','pokemon')


@admin.register(models.PokemonAbility)
class PokemonAbilityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'effect', 'short_effect')


@admin.register(models.PokemonAbilitySlot)
class PokemonAbilitySlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'slot', 'ability','pokemon')