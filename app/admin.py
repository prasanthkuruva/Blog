from django.contrib import admin
from .models import BlogModel,UserModel

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','date_added')
    
class UserModelAdmin(admin.ModelAdmin):
   list_display = ('username','email')

admin.site.register(BlogModel,BlogAdmin)
admin.site.register(UserModel,UserModelAdmin)
