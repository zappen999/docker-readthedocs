#!/bin/bash -x

curl -XPUT 'http://elasticsearch:9200/readthedocs/'

cd /app/readthedocs
ln -s ../manage.py .

PYTHON=/venv/bin/python
$PYTHON manage.py syncdb --noinput
$PYTHON manage.py migrate
echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@localhost', 'admin')" | $PYTHON manage.py shell
$PYTHON manage.py loaddata test_data
$PYTHON manage.py makemessages --all
$PYTHON manage.py compilemessages

export C_FORCE_ROOT="true"
/venv/bin/python manage.py celeryd -l INFO -Q celery,web &
/venv/bin/python manage.py runserver 0.0.0.0:8000

echo "Waiting for DB to get ready..."
sleep 10
psql -h db -U docs -d docs -c "update account_emailaddress set verified=1;"
echo "All users activated!"

chmod 400 /root/.ssh

