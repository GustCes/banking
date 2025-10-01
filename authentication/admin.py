from django.contrib import admin
from .models import Country, Department, City, User
# Register your models here.
#admin.site.register(Country)
#admin.site.register(Department)
#admin.site.register(City)
#admin.site.register(User)

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    display_data = ('name', 'abrev', 'get_status')
    list_filter = ('status',)
    search_fields = ('name', 'abrev')
    ordering = ('id',)

    def get_status(self, obj):
        return 'active' if obj.status==True else 'inactive'
    #table label
    get_status.short_description = 'Status'