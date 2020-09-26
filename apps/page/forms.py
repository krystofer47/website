from django import forms
from django.core.mail import EmailMessage

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        sender = self.cleaned_data['sender']
        cc_self = self.cleaned_data['cc_myself']

        if cc_self:
            email = EmailMessage(
                subject,
                message,
                sender,
                cc = [sender]
            )

        else:
            email = EmailMessage(
                subject,
                message,
                sender
            )
            
        email.send()        