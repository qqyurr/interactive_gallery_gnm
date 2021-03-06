# Generated by Django 3.1.7 on 2021-04-05 09:20

from django.db import migrations, models
import galleries.models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=50)),
                ('art_image', models.CharField(max_length=50)),
                ('art_description', models.CharField(max_length=50)),
                ('art_voice_description', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionkey', models.CharField(blank=True, max_length=50)),
                ('input_image_1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
                ('input_image_2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
                ('input_image_3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
                ('output_image_1', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
                ('output_image_2', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
                ('output_image_3', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=galleries.models.create_path)),
            ],
        ),
    ]
