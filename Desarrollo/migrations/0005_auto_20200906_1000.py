# Generated by Django 3.0.3 on 2020-09-06 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Desarrollo', '0004_auto_20200829_2332'),
    ]

    operations = [
        migrations.CreateModel(
            name='LineaBase',
            fields=[
                ('Codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=255)),
                ('Estado', models.CharField(blank=True, choices=[('i', 'Iniciado'), ('p', 'Pendiente'), ('f', 'Finalizado')], default='p', help_text='Estados de la Tarea', max_length=1)),
            ],
        ),
        migrations.AlterField(
            model_name='tarea',
            name='descripcion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='observacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='tarea',
            name='linea_base',
            field=models.ForeignKey(blank=True, help_text='Linea Base a la que pertence', null=True, on_delete=django.db.models.deletion.SET_NULL, to='Desarrollo.LineaBase'),
        ),
    ]