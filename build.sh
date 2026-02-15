#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Run migrations
python manage.py migrate

# Generate slugs for existing Location data
python manage.py shell -c "
from yourapp.models import Location
from django.utils.text import slugify

for obj in Location.objects.filter(slug__isnull=True):
    base_slug = slugify(obj.location)
    slug = base_slug
    counter = 1

    while Location.objects.filter(slug=slug).exclude(id=obj.id).exists():
        slug = f'{base_slug}-{counter}'
        counter += 1

    obj.slug = slug
    obj.save()

print('Slugs created successfully')
"