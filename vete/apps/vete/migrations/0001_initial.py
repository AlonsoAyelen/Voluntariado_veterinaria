# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-27 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bioquimica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('perfil', models.CharField(max_length=40)),
                ('urea', models.DecimalField(decimal_places=2, max_digits=3)),
                ('crea', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ALT', models.DecimalField(decimal_places=2, max_digits=3)),
                ('AST', models.DecimalField(decimal_places=2, max_digits=3)),
                ('PT', models.DecimalField(decimal_places=2, max_digits=3)),
                ('alb', models.DecimalField(decimal_places=2, max_digits=3)),
                ('FAS', models.DecimalField(decimal_places=2, max_digits=3)),
                ('GGT', models.DecimalField(decimal_places=2, max_digits=3)),
                ('CPK', models.DecimalField(decimal_places=2, max_digits=3)),
                ('col', models.DecimalField(decimal_places=2, max_digits=3)),
                ('bil_t', models.DecimalField(decimal_places=2, max_digits=3)),
                ('bil_d', models.DecimalField(decimal_places=2, max_digits=3)),
                ('trig', models.DecimalField(decimal_places=2, max_digits=3)),
                ('varios', models.CharField(max_length=200)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Canino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80)),
                ('especie', models.CharField(max_length=40)),
                ('sexo', models.CharField(max_length=20)),
                ('raza', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('motivo_de_consulta', models.CharField(max_length=400)),
                ('uso_de_la_mascota', models.CharField(max_length=100)),
                ('habitos', models.CharField(max_length=200)),
                ('contacto_con_basural', models.CharField(max_length=40)),
                ('caza', models.CharField(max_length=40)),
                ('caza_roedores', models.CharField(max_length=40)),
                ('observacion_roedores', models.CharField(max_length=100)),
                ('vacunado_contra_leptospirosis', models.CharField(max_length=40)),
                ('desparasitado', models.CharField(max_length=40)),
                ('eliminacion_de_excretas', models.CharField(max_length=40)),
                ('habitos_alimenticios', models.CharField(max_length=200)),
                ('signos_clinicos', models.CharField(max_length=100)),
                ('piel_Linfonodos', models.CharField(max_length=200)),
                ('digestivo', models.CharField(max_length=200)),
                ('cardio_respiratorio', models.CharField(max_length=200)),
                ('urogenital', models.CharField(max_length=200)),
                ('musculoesqueleticonervioso', models.CharField(max_length=200)),
                ('procedimiento_realizado', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('peso', models.DecimalField(decimal_places=2, max_digits=3)),
                ('actitud', models.CharField(max_length=40)),
                ('mucosas', models.CharField(max_length=40)),
                ('TLC', models.CharField(max_length=40)),
                ('hidratacion', models.CharField(max_length=40)),
                ('FC', models.CharField(max_length=40)),
                ('pulso', models.CharField(max_length=40)),
                ('FR', models.CharField(max_length=40)),
                ('T', models.DecimalField(decimal_places=2, max_digits=3)),
                ('status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hemograma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('HTO', models.IntegerField()),
                ('s_o_l', models.DecimalField(decimal_places=2, max_digits=3)),
                ('GR', models.DecimalField(decimal_places=2, max_digits=3)),
                ('Hb', models.DecimalField(decimal_places=2, max_digits=3)),
                ('plaquetas', models.IntegerField()),
                ('GB', models.DecimalField(decimal_places=2, max_digits=3)),
                ('VCM', models.DecimalField(decimal_places=2, max_digits=3)),
                ('HCM', models.DecimalField(decimal_places=2, max_digits=3)),
                ('ChCM', models.DecimalField(decimal_places=2, max_digits=3)),
                ('FLR_NB', models.IntegerField()),
                ('FLR_NS', models.IntegerField()),
                ('FLR_E', models.IntegerField()),
                ('FLR_B', models.IntegerField()),
                ('FLR_L', models.IntegerField()),
                ('FLR_M', models.IntegerField()),
                ('FLA_REF', models.IntegerField()),
                ('FLA_NB', models.IntegerField()),
                ('FLA_NS', models.IntegerField()),
                ('FLA_E', models.IntegerField()),
                ('FLA_B', models.IntegerField()),
                ('FLA_L', models.IntegerField()),
                ('FLA_M', models.IntegerField()),
                ('observaciones', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('canino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vete.Canino')),
            ],
        ),
        migrations.CreateModel(
            name='Propietario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('barrio', models.CharField(max_length=100)),
                ('procedencia', models.CharField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('edad', models.IntegerField()),
                ('grado_de_instruccion', models.CharField(max_length=100)),
                ('ocupacion', models.CharField(max_length=100)),
                ('numero_convivientes_adultos', models.IntegerField()),
                ('numero_convivientes_ninios', models.IntegerField()),
                ('en_edad_escolar', models.IntegerField()),
                ('mascotas', models.IntegerField()),
                ('tipos', models.CharField(max_length=100)),
                ('vivienda', models.CharField(max_length=100)),
                ('material', models.CharField(max_length=100)),
                ('ambientes', models.IntegerField()),
                ('agujeros', models.CharField(max_length=100)),
                ('agua', models.CharField(max_length=100)),
                ('excretas', models.CharField(max_length=100)),
                ('residuos_domiciliarios', models.CharField(max_length=100)),
                ('recoleccion_de_residuos', models.CharField(max_length=100)),
                ('basural', models.CharField(max_length=100)),
                ('roedores', models.CharField(max_length=100)),
                ('agua_servida', models.CharField(max_length=100)),
                ('inundaciones', models.CharField(max_length=100)),
                ('ultima_inundacion', models.DateField(auto_now=True)),
                ('integrante', models.CharField(max_length=100)),
                ('sintomas', models.CharField(max_length=100)),
                ('aclaracion', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='canino',
            name='propietario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vete.Propietario'),
        ),
        migrations.AddField(
            model_name='bioquimica',
            name='canino',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vete.Canino'),
        ),
    ]
