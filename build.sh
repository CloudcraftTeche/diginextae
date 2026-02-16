#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# ✅ Fix duplicate slugs before migration
echo "Fixing duplicate slugs..."

python manage.py shell << END
from django.utils.text import slugify
from dashboard.models import OurWorks  # change app name if different

for obj in OurWorks.objects.all():
    if not obj.slug:
        base_slug = slugify(obj.title)
    else:
        base_slug = obj.slug

    slug = base_slug
    counter = 1

    while OurWorks.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    if obj.slug != slug:
        obj.slug = slug
        obj.save(update_fields=["slug"])

print("Slug cleanup completed")
END

# Run migrations
python manage.py migrate
