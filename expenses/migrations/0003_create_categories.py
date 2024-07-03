from django.db import migrations

def create_categories(apps, schema_editor):
    Category = apps.get_model('expenses', 'Category')

    categories_to_create = ["Groceries", "Housing", "Life & Entertainment", "Health & Beauty", "Investments"]

    for category in categories_to_create:
        Category.objects.create(name=category)

class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20200508_1810'),
    ]

    operations = [
        migrations.RunPython(create_categories),
    ]
