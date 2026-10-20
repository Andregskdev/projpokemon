import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Raridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, unique=True)),
                ('descricao', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Raridade',
                'verbose_name_plural': 'Raridades',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='TipoPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'verbose_name': 'Tipo de Pokémon',
                'verbose_name_plural': 'Tipos de Pokémon',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='CartaPokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=120)),
                ('estagioEvolucao', models.CharField(choices=[('BASICO', 'Básico'), ('ESTAGIO1', 'Estágio 1'), ('ESTAGIO2', 'Estágio 2')], default='BASICO', max_length=10, verbose_name='estágio de evolução')),
                ('pontoVida', models.PositiveIntegerField(verbose_name='pontos de vida')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='cartas/')),
                ('valorEstimado', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='valor estimado')),
                ('raridade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cartas', to='cartaspokemon.raridade')),
                ('tipoPokemon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='cartas', to='cartaspokemon.tipopokemon', verbose_name='tipo de Pokémon')),
            ],
            options={
                'verbose_name': 'Carta Pokémon',
                'verbose_name_plural': 'Cartas Pokémon',
                'ordering': ['-valorEstimado', 'nome'],
            },
        ),
    ]
