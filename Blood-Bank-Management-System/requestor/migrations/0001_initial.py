# Generated by Django 2.1.4 on 2019-02-02 08:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='New_requestor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rig', models.CharField(max_length=30)),
                ('date_of_registration', models.DateTimeField(auto_now_add=True)),
                ('locality', models.CharField(max_length=400)),
                ('landmark', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator(code='invalid_cell', message='Enter a valid phone no', regex='^[1-9]{1}[0-9]{9}$')])),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.State')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]