from django import forms
from .models import Publisher, Book
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit



ROLE = (('Title', 'title'), ('Contributor', 'contributor'))


class SearchForm(forms.Form):
    search = forms.CharField(required=False, min_length=3)
    search_in = forms.ChoiceField(choices=ROLE, required=False)
    
    def __init_(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method= "get"
        self.helper.add_input(Submit("","search"))


class PublisherForm(forms.Form):
    class Meta:
        model = Publisher
        fields = '_all_'

class OrderForm(forms.Form):
    def validate_email_domain(value):
        if value.split('@')(-1).lower != 'example.com':
            raise ValidationError('The email address must be on the domain example.com')

    magazine_count = forms.IntegerField(min_value=0, max_value=80, widget=forms.NumberInput(attrs={'placeholder':"number of magazines"}))
    book_count = forms.IntegerField(min_value=0, max_value=50, widget=forms.NumberInput(attrs={"placeholder":"number of books"}))
    send_confirmation = forms.BooleanField(required=False)
    email = forms.EmailField(required=False, widget=forms.EmailInput, validators=[validate_email_domain])

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["send_confirmation"] and not cleaned_data.get["email"]:
            self.add_error("email", "Please entre a valid email address to receive confirmation message")
        elif cleaned_data.get["email"] and not cleaned_data["send_confirmation"]:
            self.add_error("send_confirmation", "PLease check this if you want to receive email confirmation")

        item_total = cleaned_data.get("magazine_count", 0) + cleaned_data.get("book_count", 0)
        if item_total > 100:
            self.add_error(None, "The total number of items must be less than 100")


class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ('name','website','email')


class BookMediaForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ("image_field", "file_field")