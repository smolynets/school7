from django.contrib import admin
from .models import Podii
from .models import Biblioteka
from .models import Istoria
from .models import Kolek
from .models import Muzey
from .models import Psuholoh
from .models import Rozklad
from .models import Vyhovna
from .models import Zno


# Register your models here.



admin.site.register(Podii)
admin.site.register(Biblioteka)
admin.site.register(Istoria)
admin.site.register(Kolek)
admin.site.register(Muzey)
admin.site.register(Psuholoh)
admin.site.register(Rozklad)
admin.site.register(Vyhovna)
admin.site.register(Zno)

