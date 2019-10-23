import os
import sys
import pandas
import django
import numpy as np

from sentry_sdk import capture_exception

BASE_PATH = os.path.dirname('/src/')
sys.path.append(BASE_PATH)

os.environ["DJANGO_SETTINGS_MODULE"] = 'eventuality.settings'
django.setup()

from apps.even.models.EventCategory import EventCategory

categories_file = sys.argv[1]

categories_df = pandas.read_excel(categories_file)

categories_df.fillna('', inplace=True)

updated = 0
created = 0
for index, row in categories_df.iterrows():
    category_name = row['name']

    # Set category description
    description = row['description']
    additional_text = row['additional text']

    if additional_text != '':
        description = '\n'.join([description, additional_text])

    # Get parent category name
    parent_category_name = row['parent']

    parent_category = None
    if parent_category_name != '':
        # Get parent category
        try:
            parent_category = EventCategory.objects.get(name=parent_category_name)
        except EventCategory.DoesNotExist:
            capture_exception('Parent category {} for {} subcategory has not been created'.format(
                parent_category_name, new_category.name))

    # Check if a category already exists with that name
    try:
        existing_category = EventCategory.objects.get(name = category_name)
    except EventCategory.DoesNotExist as e:
        # Set-up initial data for category
        new_category = {
            'name': category_name,
            'description': description,
            'parent_category': parent_category
        }

        EventCategory.objects.create(**new_category)

        created = created + 1
    else:
        is_updated = False
        # Update existing category
        if existing_category.description != description:
            existing_category.description = description
            is_updated = True

        if existing_category.parent_category != parent_category:
            existing_category.parent_category = parent_category
            is_updated = True

        if is_updated:
            existing_category.save()
            updated = updated + 1

print('{} categories were created'.format(created))

print('{} categories were updated'.format(updated))
