source bin/activate
cd do_it
git pull origin master
python manage.py collectstatic
python manage.py migrate
sudo supervisorctl restart do_it