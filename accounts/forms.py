from django import forms
from django.contrib.auth.models import User
from accounts.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(forms.ModelForm):
    class Meta:

        fields = ("username", 'email', 'password')
        model = User

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
            }
    # On the UserCreationForm the fileds 'password1' and 'password2' were declared in the form itself.
    # Adjust their apperance like this:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control'})
        self.fields["username"].label = "* Username"
        self.fields["email"].label = "* Email"
        self.fields["password"].label = "* Password"

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("first_name", "last_name", "birth_date", "location", "website_link", "bio", "profile_pic")

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control'}),
            'profile_pic' : forms.FileInput(attrs={'class': 'custom-file-input', 'id':'customFile', 'type': 'file', 'onchange': 'fileLabel(this.value)'}),
            'location': forms.Textarea(attrs={'class': 'form-control'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rename the form fields
        self.fields["profile_pic"].label = "Name"
        self.fields["profile_pic"].label = "Profile picture"
        self.fields["location"].label = "Address"
        self.fields["birth_date"].label = "Birthday"


# Update profile
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username", "email", "password")

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'New Password'})


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ("first_name", "last_name", "birth_date", "location", "website_link", "bio", "profile_pic")

        widgets = {
            'first_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            'last_name' : forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            'profile_pic' : forms.FileInput(attrs={'class': 'custom-file-input', 'id':'customFile', 'type': 'file', 'onchange': 'fileLabel(this.value)'}),
            'location': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            'website_link': forms.URLInput(attrs={'class': 'form-control', 'placeholder':'Edit'}),
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date',}),
            'bio': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Edit'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Rename the form fields
        self.fields["profile_pic"].label = "Profile picture"
        self.fields["location"].label = "Address"
        self.fields["birth_date"].label = "Birthday"
