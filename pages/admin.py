from django.contrib import admin
from pages.models import Host
from pages.models import Checkin
from pages.models import Checkout
from pages.models import Exites
# Register your models here.


admin.site.register(Host)
admin.site.register(Checkin)
admin.site.register(Checkout)
admin.site.register(Exites)