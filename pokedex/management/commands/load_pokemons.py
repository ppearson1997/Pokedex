import json
from logging import NullHandler
from django.db.models import base
import requests

from django.core.management.base import BaseCommand
from pokedex.constants import logger
from pokedex import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Now importing Pokemon ...")

        for x in range(1, 152):
            response = requests.get("https://pokeapi.co/api/v2/pokemon/%s" % x)
            pokemons = json.loads(response.text)
            hp = 0
            attack = 0
            defense = 0
            special_attack = 0
            special_defense = 0
            speed = 0
            
            for index, dtl in enumerate(pokemons['stats']):
                if dtl['stat']['name'] == 'hp':
                    hp = pokemons['stats'][index]['base_stat']
                if dtl['stat']['name'] == 'attack':
                    attack = pokemons['stats'][index]['base_stat']
                if dtl['stat']['name'] == 'defense':
                    defense = pokemons['stats'][index]['base_stat']
                if dtl['stat']['name'] == 'special-attack':
                    special_attack = pokemons['stats'][index]['base_stat']
                if dtl['stat']['name'] == 'special-defense':
                    special_defense = pokemons['stats'][index]['base_stat']
                if dtl['stat']['name'] == 'speed':
                    speed = pokemons['stats'][index]['base_stat']

            pokemon,created = models.Pokemon.objects.get_or_create(
                name=pokemons["name"],
                order=pokemons["order"],
                height=pokemons["height"],
                weight=pokemons["weight"],
                base_experience = pokemons["base_experience"],
                hp = hp,
                attack = attack,
                defense = defense,
                special_attack = special_attack,
                special_defense = special_defense,
                speed = speed
            )

            for type in pokemons["types"]:
                pokemontype,created = models.PokemonType.objects.get_or_create(
                    name=type['type']['name'],
                )
                pokemontypeslot,created = models.PokemonTypeSlot.objects.get_or_create(
                    slot=type['slot'],
                    type=pokemontype,
                    pokemon=pokemon
                )
            
            for ability in pokemons["abilities"]:
                ability_url = requests.get(ability['ability']['url'])
                ability_dtl = json.loads(ability_url.text)
                effect = ""
                short_effect = ""

                for index, dtl in enumerate(ability_dtl['effect_entries']):
                    if dtl['language']['name'] == 'en':
                        effect = ability_dtl['effect_entries'][index]['effect']
                        short_effect = ability_dtl['effect_entries'][index]['short_effect']
                    
                pokemonability,created = models.PokemonAbility.objects.get_or_create(
                    name=ability['ability']['name'],
                    effect = effect,
                    short_effect = short_effect
                )
                pokemontypeslot,created = models.PokemonAbilitySlot.objects.get_or_create(
                    slot=ability['slot'],
                    ability=pokemonability,
                    pokemon=pokemon
                )

                logger.info(pokemon)