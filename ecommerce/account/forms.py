from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)

from .models import Customer, Address


class UserAddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["full_name", "phone", "address_line", "address_line2", "town_city", "postcode"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["full_name"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["phone"].widget.attrs.update({"class": "form-control mb-2 account-form", "placeholder": "Phone"})
        self.fields["address_line"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["address_line2"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["town_city"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )
        self.fields["postcode"].widget.attrs.update(
            {"class": "form-control mb-2 account-form", "placeholder": "Full Name"}
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    name = forms.CharField(
        label='Username', min_length=4, max_length=50, help_text='bắt buộc')
    email = forms.EmailField(max_length=100, help_text='bắt buộc', error_messages={
        'required': 'Bạn cần nhập email để đăng ký'})
    password = forms.CharField(label='Mật khẩu', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Xác nhận mật khẩu', widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ('name', 'email',)

    def clean_name(self):
        name = self.cleaned_data['name'].lower()
        r = Customer.objects.filter(name=name)
        if r.count():
            raise forms.ValidationError("Username đã tồn tại")
        return name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Mật khẩu không khớp')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Customer.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Vui lòng sử dụng email khác, email đã được sử dụng')
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Name'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Mật khẩu'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu'})


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=254, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}))

    def clean_email(self):
        email = self.cleaned_data['email']
        u = Customer.objects.filter(email=email)
        if not u:
            raise forms.ValidationError(
                'Rất tiếc, chúng tôi không thể tìm thấy địa chỉ email đó')
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-newpass'}))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New Password', 'id': 'form-new-pass2'}))


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    name = forms.CharField(
        label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Name', 'id': 'form-firstname',
                   'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-lastname'}))

    class Meta:
        model = Customer
        fields = ('email', 'name', 'first_name',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = True
        self.fields['email'].required = True
