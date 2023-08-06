from django.contrib import admin
from userQuest.models import User, Question, FavoriteQuestion, ReadQuestion

class UserAdmin(admin.ModelAdmin):
   list_display = ('display_name', 'email', 'phone')

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(FavoriteQuestion)
admin.site.register(ReadQuestion)
