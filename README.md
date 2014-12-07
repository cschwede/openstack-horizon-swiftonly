Openstack Horizon - Swift, Keystone and Ceilometer only
=======================================================

This simple python module overrides default settings in OpenStack Horizon and
makes it possible to use Horizon with OpenStack Swift and Keystone only (and
Ceilometer, if you want).

1. Install this package:
    
    python setup.py install

2. Add customization module to /etc/openstack-dashboard/local_settings:

 HORIZON_CONFIG = {
     # ...
     'customization_module': 'dashboard_override.override',
 }

3. Restart Apache

 apachectl restart

Have a look at the override.py file and customize it to meet your needs.
