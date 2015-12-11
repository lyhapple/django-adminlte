# -*- coding: utf-8 -*-
import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class LoginForm(AuthenticationForm):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                classes = self.fields[f_name].widget.attrs.get('class', '')
                classes += ' has-error'
                self.fields[f_name].widget.attrs['class'] = classes


class RegistrationForm(forms.Form):

    username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Username")}))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'maxlength': 60, 'class': 'form-control', 'placeholder': _("Email Address")}))
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Password")}))
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'maxlength': 30, 'class': 'form-control', 'placeholder': _("Confirm your password")}))

    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        if self.errors:
            for f_name in self.fields:
                if f_name in self.errors:
                    classes = self.fields[f_name].widget.attrs.get('class', '')
                    classes += ' has-error'
                    self.fields[f_name].widget.attrs['class'] = classes

    def clean_username(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        #_("Account already exists.")
        raise forms.ValidationError("用户名已经存在,请更换!")

    def clean_password2(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                #_("Passwords don't match.")
                raise forms.ValidationError("两次输入的密码不一致!")
        return self.cleaned_data['password2']

    def clean(self):
        return self.cleaned_data
