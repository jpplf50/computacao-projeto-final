from django.contrib import admin

# Register your models here.
from .models import Automato
admin.site.register(Automato)

from .models import MaquinaTuring
admin.site.register(MaquinaTuring)

from .models import ExpressaoRegular
admin.site.register(ExpressaoRegular)