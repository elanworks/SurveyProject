from django.contrib import admin

# Register your models here.

from .models import Question
from .models import survey
from .models import Option

admin.site.register(Question)
admin.site.register(survey)
admin.site.register(Option)
