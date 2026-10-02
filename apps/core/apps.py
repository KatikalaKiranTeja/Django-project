from django.apps import AppConfig

from .db_bootstrap import ensure_sqlite_schema


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.core'

    def ready(self) -> None:
        ensure_sqlite_schema()
