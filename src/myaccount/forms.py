from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from allauth.socialaccount.forms import SignupForm
from .models import UserProfile

from django.core.exceptions import ValidationError

def nickname_unique_validator(value):
	if UserProfile.objects.filter(nickname=value).count() > 0:
		raise ValidationError('Nickname already taken.')
	return value

class SignupForm(forms.Form):
	nickname = forms.CharField(max_length=30, label='nickname', validators=[nickname_unique_validator])

	def signup(self, request, user):
		# user.username = self.cleaned_data['email']
		user.username = user.email
		user.save()

		up = UserProfile()
		up.user = user
		up.nickname = self.cleaned_data['nickname']
		up.save()


# class SocialCustomSignupForm(SignupForm):
# 	nickname = forms.CharField(max_length=30, label='nickname')

# 	def signup(self, request, user):
# 		user.username = self.cleaned_data['email']
# 		user.save()

# 		userprofile =  UserProfile()
# 		userprofile.user = user
# 		userprofile.nickname = self.cleaned_data['nickname']
# 		print(userprofile)
# 		userprofile.save()