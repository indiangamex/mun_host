from django.contrib import admin
from contact.models import Contact
from contact.models import Idelegate
from contact.models import Sdelegate

admin.site.register(Contact)
admin.site.register(Idelegate)
admin.site.register(Sdelegate)