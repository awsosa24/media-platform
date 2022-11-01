import csv
from django.core.management.base import BaseCommand
from base.models import Channel


class Command(BaseCommand):
    """
    calculate the ratings of every channel and export them in a csv.
    python3 manage.py channels_ratings
    """
    def handle(self, *args, **options):
        meta = {
            'file': './base/tmp/ratings.csv',
            'query': Channel.ratings(),
            'fields': ('title', 'average_rating') # models fields you want to include
        }
        self._write_csv(meta)

    def _write_csv(self, meta):
        f = open(meta['file'], 'w+')
        writer = csv.writer(f)
        writer.writerow(meta['fields'])
        for obj in meta['query']:
            row = [getattr(obj, field) for field in meta['fields']]
            writer.writerow(row)
        f.close()
        print('Data written to %s' % meta['file'])
