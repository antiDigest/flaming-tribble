from django.contrib import admin
from .models import Words_India, Words_Global, ytstats, tstats, fbstats

# Register your models here.

admin.site.register(Words_India)
admin.site.register(Words_Global)
admin.site.register(ytstats)
admin.site.register(fbstats)
admin.site.register(tstats)
