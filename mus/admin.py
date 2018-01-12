from django.contrib import admin

# Register your models here.

from mus.models.db import *

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Team)
admin.site.register(Round)
admin.site.register(Score)
