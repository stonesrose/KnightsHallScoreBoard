from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(teamInfo)
admin.site.register(matchInfo)
admin.site.register(matchType)
admin.site.register(matchRounds)