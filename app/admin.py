from django.contrib import admin

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration

admin.site.register(Program)
admin.site.register(Adult)
admin.site.register(Child)
admin.site.register(Registration)

admin.AdminSite.login_template = 'admin/login.html'
admin.AdminSite.logout_template = 'admin/logout.html'
admin.AdminSite.site_header = 'Summer Reading Signup Administration'
admin.AdminSite.site_title = 'Summer Reading Signup'
admin.AdminSite.index_title = 'Administration'
