from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption', 'created_at']  # Include description for visibility

    # Define a custom action
    def some_action(self, request, queryset):
        # Example action: add a message to notify the admin user
        self.message_user(request, "Custom action executed on selected posts.")
    some_action.short_description = "Perform some action on selected posts"

    # Add custom action to the admin
    actions = ['some_action']
