from django.contrib import admin
from .models import CartaPokemon, Raridade, TipoPokemon


@admin.register(Raridade)
class RaridadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(TipoPokemon)
class TipoPokemonAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)


@admin.register(CartaPokemon)
class CartaPokemonAdmin(admin.ModelAdmin):
    list_display = ('nome', 'raridade', 'tipoPokemon', 'estagioEvolucao', 'pontoVida', 'valorEstimado')
    list_filter = ('raridade', 'tipoPokemon', 'estagioEvolucao')
    search_fields = ('nome',)
