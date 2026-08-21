"""
Django command to wait for the database to be available.
"""

from django.core.management.base import BaseCommand
import time

from psycopg import OperationalError as PsycopgOpError
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command to wait for the database to be available."""

    def handle(self, *args, **options):
        self.stdout.write("Waiting for database...")
        db_conn = None
        while not db_conn:
            try:
                self.check(databases=["default"])
                db_conn = True
            except (PsycopgOpError, OperationalError):
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS("Database available!"))