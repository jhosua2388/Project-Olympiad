# Generated by Django 4.2.6 on 2023-10-26 22:23

from django.db import migrations, models
import secrets, hashlib

def insert_initial_data(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    Estado = apps.get_model('backoffice', 'estados')
    Grupo = apps.get_model('backoffice', 'group')
    Usuario = apps.get_model('backoffice', 'usuarios')

    # Inserta los datos iniciales en la tabla Estados
    Estado.objects.using(db_alias).bulk_create([
        Estado(nombre='Ingresado', active=True),
        Estado(nombre='Aceptado', active=True),
        Estado(nombre='Rechazado', active=True),
    ])

    Grupo.objects.using(db_alias).bulk_create([
        Grupo(nombre='Administrador', active=True),
        Grupo(nombre='Ejecutivo', active=True),
    ])

    Usuario.objects.using(db_alias).bulk_create([
        Usuario(email='administrador@ong.org', password="123456", hash=secrets.token_hex(20), group_id=1, active=True),
        Usuario(email='ejecutivo@ong.org', password="123456",hash=secrets.token_hex(20), group_id=2, active=True),
    ])

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='beneficiarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('apellido', models.CharField(max_length=15)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('nacionalidad', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=15)),
                ('pais_residencia', models.CharField(max_length=15)),
                ('grado_educacion', models.CharField(max_length=15, null=True)),
                ('actividad_laboral', models.CharField(max_length=15, null=True)),
                ('profesion', models.CharField(max_length=15, null=True)),
                ('estado', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.IntegerField()),
                ('fuente', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='estados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('verificado', models.BooleanField(default=False)),
                ('hash', models.CharField(max_length=40, null=True)),
                ('hash_verificacion', models.CharField(max_length=40, null=True)),
                ('last_login', models.DateTimeField(auto_now_add=True, null=True)),
                ('group_id', models.IntegerField()),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RunSQL("BEGIN;"),
        migrations.RunPython(insert_initial_data),
        migrations.RunSQL("COMMIT;"),
    ]