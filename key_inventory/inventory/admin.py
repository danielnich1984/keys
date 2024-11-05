from django.contrib import admin
from django.utils import timezone
from .models import Key, Users, KeyAssignment

# Register Users
admin.site.register(Users)

@admin.register(Key)
class KeyAdmin(admin.ModelAdmin):
    list_display = ('name', 'total_quantity', 'checked_out_quantity', 'available_quantity')

# Action to mark selected keys as lost
@admin.action(description="Mark selected keys as lost")
def mark_keys_as_lost(modeladmin, request, queryset):
    queryset.update(status='LOST', return_date=timezone.now())

# Register KeyAssignment with additional actions
@admin.register(KeyAssignment)
class KeyAssignmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'key', 'checkout_date', 'return_date', 'is_returned', 'status')
    list_filter = ('key', 'user', 'return_date', 'status')
    search_fields = ('user__fname', 'user__lname', 'key__name')
    actions = [mark_keys_as_lost]  # Add the action to the admin

    def is_returned(self, obj):
        return obj.return_date is not None  # Check if the key assignment has been returned
    is_returned.short_description = 'Returned'  # Display name in admin
