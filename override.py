# Copyright (c) 2014 Christian Schwede <info@cschwede.de>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import horizon

keep_panels = ['metering', ]

# Set Swift as the default project panel
projects_dashboard = horizon.get_dashboard("project")
projects_dashboard.default_panel = 'containers'

# Remove all Nova project panels
# have a look at openstack_dashboard/dashboards/project/dashboard.py
compute_panelgroup = projects_dashboard.get_panel_group('compute')
for panelname in compute_panelgroup.panels:
    panel = projects_dashboard.get_panel(panelname)
    projects_dashboard.unregister(panel.__class__)

# Set the user panel as default admin panel
admin_dashboard = horizon.get_dashboard("admin")
admin_dashboard.default_panel = 'users'

# Remove all admin panels (these are mostly Nova panels)
# have a look at openstack_dashboard/dashboards/admin/dashboard.py
admin_panelgroup = admin_dashboard.get_panel_group('admin')
for panelname in admin_panelgroup.panels:
    if panelname not in keep_panels:
        panel = admin_dashboard.get_panel(panelname)
        admin_dashboard.unregister(panel.__class__)
