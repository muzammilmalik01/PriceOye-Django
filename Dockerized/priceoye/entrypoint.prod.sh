#!/bin/sh
if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."
    while ! nc -z "$POSTGRES_DB " "$POSTGRES_PORT"; do
      sleep 0.1
    done
    echo "PostgreSQL started"
fi
# python manage.py collectstatic --no-input
exec "$@"