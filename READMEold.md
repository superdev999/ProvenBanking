[![Build Status](https://magnum.travis-ci.com/Vetted/VPP.svg?token=2UAA2wwqogr2btQ9WbdB&branch=master)](https://magnum.travis-ci.com/Vetted/VPP)
[![Coverage Status](https://coveralls.io/repos/Vetted/VPP/badge.png)](https://coveralls.io/r/Vetted/VPP)


#Vetted

TODO: Change thevetteddb to include extensions schema, grant on permissions and
        hstore extension

************

##Local setup using Docker

* Install dependencies

            sudo apt-get install docker.io


* CD into project root directory & import container images

            bin/import_db.sh PATH_TO_DB_CONTAINER.tar
            bin/import_app.sh PATH_TO_APP_CONTAINER.tar


* Initialize the containers from the images (in separate terminals/tabs/ttys)

            bin/init_db.sh
            bin/init_app.sh

At this point your docker containers should be working and you should be able to excute regular django commands from within the docker containers


WARNING: Do not call initialize the containers again unless you want a clean base. it'll wipe out all data including the databases


* From now on, run the containers like this (in separate ttys)


            bin/run_db.sh
            bin/run_app.sh


###Notes on Tmux

We are using Tmux (terminal multiplexer inside docker containers). Some useful shortcuts


    + Create a new tty


            Control-a c


    + Switch to tty


            Control-a {TTY_NUMBER}


Where 'Control-a c' means press a while holding control and then press c


##Manual/Native setup

##Configuring the machine

###Ubuntu

* Install all the required packages

            wget -O - http://apt.postgresql.org/pub/repos/apt/ACCC4CF8.asc | sudo apt-key add -
            sudo cp /sites/medosocial.com/MedSocial/med_social/deploy/apt/pgdg.list /etc/apt/sources.list.d/
            sudo apt-get install python-software-properties
            sudo add-apt-repository ppa:pitti/postgresql
            sudo apt-get update
            sudo apt-get install build-essential libgeos-c1 python2.7 python-pip python-virtualenv python-dev postgresql-client-common postgresql-client-9.5 pgbouncer libjpeg62 libjpeg-dev zlib1g-dev imagemagick libevent-dev nginx redis-server libfreetype6-dev libxml2 libxslt1-dev libxml2-dev libxslt-dev python-nltk python-numpy node-less libffi-dev libpq-dev

            sudo pip install pip -U
            sudo pip install virtualenv -U
            sudo pip install virtualenvwrapper -U

            # Pgboucer is not used for now. Skip this.
            sudo cp deploy/pgbouncer/userlist.txt /etc/pgbouncer/userlist.txt
            sudo cp deploy/pgbouncer/pgbouncer.ini /etc/pgbouncer/


* If you install PIL in virtualenv, you'll need to symlink some libs for PIL to compile properly

    + For 64bit OS

            sudo ln -s /usr/include/freetype2 /usr/include/freetype
            sudo ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib/
            sudo ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/
            sudo ln -s /usr/lib/x86_64-linux-gnu/libfreetype.so /usr/lib/


    + For 32bit OS

            sudo ln -s /usr/lib/i386-linux-gnu/libjpeg.so /usr/lib/
            sudo ln -s /usr/lib/i386-linux-gnu/libz.so /usr/lib/
            sudo ln -s /usr/lib/i386-linux-gnu/libfreetype.so /usr/lib/


* Configure Postgresql

            sudo passwd postgres
            sudo -u postgres psql
            postgres=# \password postgres
            postgres=# \q
            sudo -u postgres createuser inexec
            sudo -u postgres psql
            postgres=# \password inexec
            postgres=# \q
            sudo vim /etc/postgresql/9.5/main/pg_hba.conf

    Change this

            # "local" is for Unix domain socket connections only
            local   all             all                                     peer

    To

            # "local" is for Unix domain socket connections only
            local   all             all                                     md5


    and restart postgres

            sudo service postgresql restart

    Edit PSQL database template to include the structure and extensions we need

        sudo su postgres
        psql thevetteddb
        thevetteddb=# create schema extensions;
        thevetteddb=# grant all on schema extensions to postgres;
        thevetteddb=# grant all on schema extensions to public;
        thevetteddb=# create extension hstore with schema extensions;
        thevetteddb=# \q;

    Now create the database

            sudo su postgres
            createdb inexecdb
            psql inexecdb
            postgres=# GRANT ALL ON DATABASE inexecdb to inexec;
            postgres=# \q

    also update the userlist.txt in /etc/pgbouncer/ if using pgbouncer with the credentials of the new user


* Install Node.js

        https://launchpad.net/~chris-lea/+archive/node.js/

        OR

        wget nodejs/latest/release.tar.gz
        tar -zvzf release.tar.gz
        cd release
        ./configure
        sudo make
        sudo make install


* Install Node depencies mentioned in packages.json

        npm install --no-bin-links


## Setting up application environment

Deploy the project source to <code>/src/thevetted/VPP/</code>


* Setup MedSocial


    + Run bootstrap script


                ./bootstrap.sh


    + Create <code>med\_social/settings/local.py</code> from <code>med\_social/settings/local.py.def</code>
    + Activate the isolated python environment for medsocial


                source ve/bin/activate


    + Create initial schema


                ./manage.py migrate_schemas --shared


    + create a public tenant (for root domain public site)


                ./manage.py shell
                >>> from customers.models import Customer
                >>> c=Customer.objects.create(domain_url='vetted.dev', schema_name='public', name='Vetted', email='admin@vetted.dev')

                >>> mst =Customer.objects.create(domain_url='microsoft.vetted.dev', schema_name='microsoft', name='Microsoft', email='admin+microsoft@vetted.dev')


    + Create superuser for admin (optional)


                ./manage.py tenant_command createsuperuser


    + Create elastic search indexes for the first time


                ./manage.py rebuild_index


    + Start local server


                ./manage.py runserver


    + Running migrations

        You can run migrate on tenants using the following commands.


                ./manage.py migrate_schemas --tenant


    + [PRODUCTION] Start Circusd

        Copy deploy/hosts/<HOST>/circus_upstart.conf to /etc/init/circus.conf and reboot the system.
        This will start circusd which will manage all services like chaussette and celery


                ./manage.py supervisord -c deploy/supervisord.conf.local -n


    + [LOCAL] Start runserver and celery


                ./manage.py celeryd --loglevel=INFO

                ./manage.py runserver 0.0.0.0:8000


    + or Start django shell


                pip install ipython # (Optional but recommended)
                ./manage.py shell


    + Running on local domain to test tenants

        * Install dnsmasq


                    sudo apt-get install dnsmasq


        * Add the following line to /etc/dnsmasq.conf


                    address=/.vetted.dev/127.0.0.1


        If `dnsmasq` does not work you can add explicit lines to /etc/hosts


                127.0.0.1   vetted.dev
                127.0.0.1   google.vetted.dev
                127.0.0.1   iuiu.vetted.dev
                127.0.0.1   mckinsey.vetted.dev


        Now you can access the site at vetted.dev:PORT and tenants at tenant.vetted.dev:PORT

## Writing Tests
When writing testcases, use `med_social.tests.base.TenantTestCase` as the baseclass instead of `django.test.TestCase`. This class creates and sets the DB's connection to a test schema.

Example:

```
from med_social.tests.base import TenantTestCase

class ExampleTestCase(TenantTestCase):
    def test_something(self):
        response = self.client.get("/something/")
        self.assertEqual(response.status_code, 200)
```        
`self.client` and `self.factory` are substitutes for the django's `Client` and `RequestFactory`provided by the the django-tenant-schemas library, but have the same API.

## Running Tests

We have a special settings file present for tests at <code>med_social/settings/test.py</code>
Command to run tests is


        ./manage.py test --settings=med_social.settings.test


## Upstart

upstart script should be copied from deploy folder like

                sudo cp /src/thevetted/VPP/deploy/hosts/prod/circus_upstart.conf /etc/init/circus.conf

## Patches.

We patch django's built in functions and classes to get get desired behaviour
across the project without overriding functions/classes everywhere in the code.

All patches are store in the patches.py file and are loaded before manage.py
runs any command.

Mostly we just patch form widgets to change default behaviour in form UI.
Subclassing widgets would have been better but that we won't get the desired
behaviour from auto generated forms and forms shipped by 3rd party apps.

We are also patching django's base view `django.views.generic.base.View` to
implement a permissions pattern.
