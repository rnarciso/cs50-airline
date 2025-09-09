from django import forms

from .models import Airport, Flight, Passenger


# ------------------------------ airport ------------------------------ #

class AirportForm(forms.Form):
	code = forms.CharField(
		max_length=3,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Airport Code'
			}
		)
	)
	city = forms.CharField(
		max_length=30,
		widget=forms.TextInput(
			attrs={
			'class': 'form-control',
			'placeholder': 'Airport City'
			}
		)
	)

	def clean_code(self, *args, **kwargs):
		code = self.cleaned_data.get('code')
		if len(code) != 3:
			raise forms.ValidationError('error')
		return code


# class AirportModelForm(forms.ModelForm):
# 	code = forms.CharField(
# 		max_length=3,
# 		widget=forms.TextInput(
# 			attrs={
# 			'class': 'form-control',
# 			'placeholder': 'Airport Code'
# 			}
# 		)
# 	)
# 	city = forms.CharField(
# 		max_length=30,
# 		widget=forms.TextInput(
# 			attrs={
# 			'class': 'form-control',
# 			'placeholder': 'Airport City'
# 			}
# 		)
# 	)

# 	class Meta:
# 		model = Airport
# 		fields = [
# 		'code',
# 		'city'
# 		]

# 	def clean_code(self, *args, **kwargs):
# 		code = self.cleaned_data.get('code')
# 		if len(code) != 3:
# 			raise forms.ValidationError('error')
# 		return code





# ------------------------------ flight ------------------------------ #

class FlightModelForm(forms.ModelForm):
	class Meta:
		model = Flight
		fields = '__all__'





# ------------------------------ passenger ------------------------------ #

class PassengerModelForm(forms.ModelForm):
	class Meta:
		model = Passenger
		fields = '__all__'
