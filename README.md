askbot-openshift
================

[Askbot](https://askbot.com/) running on [OpenShift](http://openshift.com/).

How-to
------

 1. Create Python 2.7 app
 2. Add PostgreSQL cartridge
 3. Add Cron cartridge
 4. Add [Redis cartridge](smarterclayton/openshift-redis-cart)
 5. Push --force this repo to the app
 5. Create user account on your site (first account is the admin account)
 6. Via Django admin, create a new site
 7. (Optionally, for security) Disable Django admin in `wsgi/openshift/settings.py`
 8. Profit
