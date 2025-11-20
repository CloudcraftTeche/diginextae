from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    User = get_user_model()

    username = 'admin'
    email = 'admin@example.com'
    password = 'Admin@123'

    if not User.objects.filter(is_superuser=True).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"Superuser created -> username: {username}, password: {password}")
    else:
        existing_superuser = User.objects.filter(is_superuser=True).first()
        print(
            f"Superuser already exists -> username: {existing_superuser.username}, "
            f"password (configured): {password}"
        )
