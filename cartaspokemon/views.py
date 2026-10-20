from django.shortcuts import render

from django.db.models import Count
from django.shortcuts import get_object_or_404, render

from .models import CartaPokemon, Raridade


def inicio(request):
    raridades = Raridade.objects.annotate(total_cartas=Count('cartas')).filter(total_cartas__gt=0)
    return render(request, 'cartaspokemon/inicio.html', {'raridades': raridades})


def cartas_por_raridade(request, raridade_id):
    raridade = get_object_or_404(Raridade, pk=raridade_id)
    busca = request.GET.get('busca', '').strip()
    cartas = CartaPokemon.objects.filter(raridade=raridade)
    if busca:
        cartas = cartas.filter(nome__icontains=busca)
    return render(
        request,
        'cartaspokemon/cartas_por_raridade.html',
        {'raridade': raridade, 'cartas': cartas, 'busca': busca},
    )
