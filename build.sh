#!/usr/bin/env bash
# exit on error
set -o errexit

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Collect static files
python manage.py collectstatic --no-input

# Fix duplicate slugs before migration
python manage.py shell << EOF
from dashboard.models import SubService
from django.utils.text import slugify
import uuid

# Find and fix empty/duplicate slugs
subservices = SubService.objects.all()
for obj in subservices:
    if not obj.slug or obj.slug == '':
        # Generate a unique slug
        base_slug = slugify(obj.name) if hasattr(obj, 'name') else 'subservice'
        obj.slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"
        obj.save()
        print(f"Fixed slug for {obj.id}: {obj.slug}")
EOF

# Run migrations
python manage.py migrate