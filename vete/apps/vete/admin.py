from django.contrib import admin
from vete.apps.vete.models import Propietario
from vete.apps.vete.models import Canino 
from vete.apps.vete.models import Bioquimica
from vete.apps.vete.models import Hemograma


admin.site.register(Propietario)
admin.site.register(Canino)
admin.site.register(Bioquimica)
admin.site.register(Hemograma)
