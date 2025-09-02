from django.db import migrations

def create_superuser(apps, schema_editor):
    from django.contrib.auth.models import User
    # Change username/email/password as you like
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(
            username="Ashraf",
            email="mohammedashrafma759932@gmail.com",
            password="Ashru@9947"
        )

class Migration(migrations.Migration):

    dependencies = [
        ('my-portfolio', '0001_initial'),  # change "portfolio" to your app name
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
