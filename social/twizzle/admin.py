from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile


# Unregister Group.
admin.site.unregister(Group)

#Join User and Profile Info
class ProfileInline(admin.StackedInline):
    model = Profile
    
#Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    fields= ["username"]
    inlines = [ProfileInline]

# Unregister Initial User.
admin.site.unregister(User)
    
# Register User and Profile.
admin.site.register(User, UserAdmin)
# admin.site.register(Profile)

    
