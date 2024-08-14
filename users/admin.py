from django.contrib import admin

from users.models import User, Position


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'position')
