# Generated by Django 5.1.1 on 2024-09-27 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('olcha', '0007_alter_product_users_like'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Attribute',
            new_name='AttributeKey',
        ),
        migrations.RenameField(
            model_name='attributekey',
            old_name='name',
            new_name='key_name',
        ),
        migrations.RenameField(
            model_name='attributevalue',
            old_name='value',
            new_name='value_name',
        ),
    ]
