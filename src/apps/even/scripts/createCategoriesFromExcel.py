import sys
import pandas
from sentry_sdk import capture_exception

from apps.even.models.EventCategory import EventCategory

categories_file = sys.argv[1]

categories_df = pandas.read_excel(categories_file)

for index, row in categories_df.iterrows():
    # Set category description
    description = row['description']
    additional_text = row['additional text']

    if additional_text != '':
        description = '\n'.join([description, additional_text])

    # Set-up initial data for category
    new_category = {
        'name': row['name'],
        'description': description
    }

    # Get parent category name
    parent_category_name = name = rows['parent']

    # Get parent category
    try:
        parent_category = EventCategory.objects.filter(parent_category=parent_category_name)
    except EventCategory.DoesNotExist:
        capture_exception('Parent category {} for {} subcategory has not been created'.format(
            parent_category_name, new_category.name))
    else:
        new_category['parent_category'] = parent_category

    EventCategory.objects.create(**new_category)
