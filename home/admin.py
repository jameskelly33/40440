from django.contrib import admin
from .models import Goal, Objective

# Register your models here.
class GoalAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'categories',
        'completed',
    )

class ObjectiveAdmin(admin.ModelAdmin):
    list_display = (
        'goal',
        'description',
        'completed',
    )


admin.site.register(Objective, ObjectiveAdmin)

admin.site.register(Goal, GoalAdmin)