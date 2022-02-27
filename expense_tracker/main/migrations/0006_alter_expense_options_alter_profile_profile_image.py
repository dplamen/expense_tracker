# Generated by Django 4.0.2 on 2022-02-27 00:15

from django.db import migrations, models
import expense_tracker.validators


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_expense_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ('title', 'price')},
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images', validators=[expense_tracker.validators.ValidateMaxSizeImage(5)]),
        ),
    ]