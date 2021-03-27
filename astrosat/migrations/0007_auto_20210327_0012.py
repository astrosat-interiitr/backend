# Generated by Django 3.1.7 on 2021-03-27 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrosat', '0006_auto_20210324_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='astrosat',
            old_name='cosmic_source',
            new_name='cycle',
        ),
        migrations.AddField(
            model_name='astrosat',
            name='date',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='astrosat',
            name='equatorial_dec',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='astrosat',
            name='equatorial_ra',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='astrosat',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='astrosat',
            name='telescope',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='astrosat',
            name='time',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
