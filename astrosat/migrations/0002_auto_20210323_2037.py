# Generated by Django 3.1.7 on 2021-03-23 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrosat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Astrosat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cosmic_source', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='alternative_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='b_v_color_index',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='equatorial_dec',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='equatorial_ra',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='galactic_latitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='galactic_longitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='optical_counterpart_name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='orbital_period',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='positional_accuracy',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='pulse_period',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='spectral_type',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='type_of_observation',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='u_b_color_index',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='v_magnitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='cosmicsource',
            name='x_ray_flux',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='keyword',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='paper_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cosmicsource',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='abstract',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='author',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='title',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
