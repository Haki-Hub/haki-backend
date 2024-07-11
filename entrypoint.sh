#!/bin/bash

set -e

# Run database migrations
flask db migrate 

echo "Starting gunicorn"

exec gunicorn -w 2 -b 0.0.0.0:5000 app:app