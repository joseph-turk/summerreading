from django.contrib import admin

from .models import Program
from .models import Adult
from .models import Child
from .models import Registration

admin.site.register(Program)
admin.site.register(Adult)
admin.site.register(Child)
admin.site.register(Registration)
