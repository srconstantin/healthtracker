from django.contrib import admin
from tracker.models import Daily
admin.site.register(Daily)
from tracker.models import Food
admin.site.register(Food)
from tracker.models import Activity
admin.site.register(Activity)
from tracker.models import Medication
admin.site.register(Medication)
from tracker.models import Supplement
admin.site.register(Supplement)


