# Generated by Django 2.1.7 on 2019-06-11 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rest1Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tafel_nr', models.IntegerField(blank=True, null=True)),
                ('wijk', models.IntegerField(blank=True, null=True)),
                ('begin_tijd', models.TextField(blank=True, null=True)),
                ('volg_nr', models.IntegerField(blank=True, null=True)),
                ('eind_tijd', models.TextField(blank=True, null=True)),
                ('servicetype', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rest1_data',
                'managed': False,
            },
        ),
    ]
