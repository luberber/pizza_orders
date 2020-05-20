# Generated by Django 2.0.3 on 2020-05-19 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prize', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='sub',
            name='toppings',
        ),
        migrations.AddField(
            model_name='add',
            name='sub',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='orders.Sub'),
        ),
        migrations.AddField(
            model_name='add',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toppping', to='orders.Topping'),
        ),
    ]