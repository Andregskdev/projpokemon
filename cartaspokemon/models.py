from django.db import models


class Raridade(models.Model):
    nome = models.CharField(max_length=80, unique=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Raridade'
        verbose_name_plural = 'Raridades'

    def __str__(self):
        return self.nome


class TipoPokemon(models.Model):
    nome = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = 'Tipo de Pokémon'
        verbose_name_plural = 'Tipos de Pokémon'

    def __str__(self):
        return self.nome


class CartaPokemon(models.Model):
    class Estagio(models.TextChoices):
        BASICO = 'BASICO', 'Básico'
        ESTAGIO1 = 'ESTAGIO1', 'Estágio 1'
        ESTAGIO2 = 'ESTAGIO2', 'Estágio 2'

    nome = models.CharField(max_length=120)
    estagioEvolucao = models.CharField(
        max_length=10,
        choices=Estagio.choices,
        default=Estagio.BASICO,
        verbose_name='estágio de evolução',
    )
    pontoVida = models.PositiveIntegerField(verbose_name='pontos de vida')
    imagem = models.ImageField(upload_to='cartas/', blank=True, null=True)
    valorEstimado = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='valor estimado',
    )
    raridade = models.ForeignKey(
        Raridade,
        on_delete=models.PROTECT,
        related_name='cartas',
    )
    tipoPokemon = models.ForeignKey(
        TipoPokemon,
        on_delete=models.PROTECT,
        related_name='cartas',
        verbose_name='tipo de Pokémon',
    )

    class Meta:
        ordering = ['-valorEstimado', 'nome']
        verbose_name = 'Carta Pokémon'
        verbose_name_plural = 'Cartas Pokémon'

    def __str__(self):
        return self.nome
