from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('users', 'User')
    User.objects.create_superuser(
        username='admin',  # <-- agrega este campo
        email='admin@example.com',
        password='admin1234'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email'),  # Ajusta si tu última migración es diferente
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]