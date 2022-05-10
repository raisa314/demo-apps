from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Meetup, Account
# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_filter = ('title',)
    prepopulated_fields = {'slug': ('title',)}

class AccountAdmin(UserAdmin):
	list_display = ('email','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','username',)
	readonly_fields=('date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Meetup, MeetupAdmin)
admin.site.register(Account, AccountAdmin)
