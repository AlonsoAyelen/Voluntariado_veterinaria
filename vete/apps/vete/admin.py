from django.contrib import admin
from vete.apps.vete.models import Propietario
from vete.apps.vete.models import Canino 
from vete.apps.vete.models import Bioquimica
from vete.apps.vete.models import Hemograma
from vete.apps.vete.models import Sintoma
from vete.apps.vete.models import Serovar
from vete.apps.vete.models import Analisis



admin.site.register(Propietario)
admin.site.register(Canino)
admin.site.register(Bioquimica)
admin.site.register(Hemograma)
admin.site.register(Sintoma)
admin.site.register(Serovar)
admin.site.register(Analisis)