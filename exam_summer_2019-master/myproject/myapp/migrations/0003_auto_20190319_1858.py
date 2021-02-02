# Generated by Django 2.1.5 on 2019-03-19 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20190319_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='product',
        ),
        migrations.RenameModel(
            old_name='Product',
            new_name='Item',
        ),
        migrations.AddField(
            model_name='record',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Item'),
        ),
        migrations.AddField(
            model_name='record',
            name='transaction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Transaction'),
        ),
    ]