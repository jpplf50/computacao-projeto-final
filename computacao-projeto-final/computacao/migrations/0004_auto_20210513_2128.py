# Generated by Django 3.2.2 on 2021-05-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computacao', '0003_fita_maquinaturing'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpressaoRegular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('expressao', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Fita',
        ),
    ]
