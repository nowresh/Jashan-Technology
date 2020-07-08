from crispy_forms.helper import FormHelper
from django import forms

class EmailForm(forms.Form):
    # email = forms.EmailField()
    name = forms.CharField(max_length=100,label="Name")
    company= forms.CharField(max_length=100,label="Company name")
    email = forms.EmailField(max_length=50,label="Email")
    phone = forms.IntegerField(label="Contact number")
    # subject = forms.CharField(max_length=100,label="hello")
    attach = forms.FileField(label="Upload file",widget=forms.ClearableFileInput(attrs={'multiple': True}))
    message = forms.CharField(widget = forms.Textarea,label="Project Description")

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True 