from django.contrib import admin
from .models import Blog
from .models import About
from .models import Work
# from .models import Month
# Register your models here.
admin.site.register(Blog)
admin.site.register(About)
admin.site.register(Work)
# admin.site.register(Month)