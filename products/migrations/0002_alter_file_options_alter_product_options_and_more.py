# Generated by Django 4.2 on 2024-09-14 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='file',
            options={'ordering': ('-created_time',), 'verbose_name': 'file', 'verbose_name_plural': 'files'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-created_time',), 'verbose_name': 'product', 'verbose_name_plural': 'products'},
        ),
        migrations.AddField(
            model_name='file',
            name='file_type',
            field=models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('audio', 'Audio'), ('text', 'Text'), ('other', 'Other')], default='text', max_length=5, verbose_name='file type'),
        ),
    ]
