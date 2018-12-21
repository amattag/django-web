from django.contrib import admin

# Register your models here.


from .models import Robot, New


admin.site.register(Robot)
admin.site.register(New)