from django.contrib import admin
from .models import post , Catagory , Coment 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User , Group
# Register your models here.


admin.site.unregister(User)

admin.site.register(Coment)
admin.site.register(post)
admin.site.register(Catagory)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    def get_form(self, request, obj = None , **kwargs):
        form = super().get_form(request , obj , **kwargs)
        is_superuser = request.user.is_superuser
    
        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            
        if obj and obj.is_staff and obj.is_active and request.user.is_staff:
            form.base_fields['is_staff'].disabled = True
            form.base_fields['is_active'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True

        return form
