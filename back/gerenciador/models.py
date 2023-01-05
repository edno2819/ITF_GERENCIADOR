from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class EmailRequiredMixin(object):
    def __init__(self, *args, **kwargs):
        super(EmailRequiredMixin, self).__init__(*args, **kwargs)
        # self.fields['email'].required = True
        # self.fields['first_name'].required = True
        # self.fields['groups'].required = True


class MyUserCreationForm(EmailRequiredMixin, UserCreationForm):
    pass

class MyUserChangeForm(EmailRequiredMixin, UserChangeForm):
    pass


class EmailRequiredUserAdmin(UserAdmin):
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    add_fieldsets = ((None, {
        'fields': ('username', 'email', 'first_name', 'password1', 'password2', 'groups', 'is_staff'), 
        'classes': ('wide',)
    }),)

