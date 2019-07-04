from django import forms
from crudApplication.models import Consent, Recipient, Charge, BloodTest, Storage, Donor, DonorInformation, PhysicalTest, BloodDonationHistory


class ConsentForm(forms.ModelForm):
    class Meta:
        model = Consent
        fields = "__all__"


class RecipientForm(forms.ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"


class ChargeForm(forms.ModelForm):
    class Meta:
        model = Charge
        fields = "__all__"


class BloodTestForm(forms.ModelForm):
    class Meta:
        model = BloodTest
        fields = "__all__"


class StorageForm(forms.ModelForm):
    class Meta:
        model = Storage
        fields = "__all__"


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = "__all__"


class DonorInformationForm(forms.ModelForm):
    class Meta:
        model = DonorInformation
        fields = "__all__"


class PhysicalTestForm(forms.ModelForm):
    class Meta:
        model= PhysicalTest
        fields = "__all__"


class BloodDonationHistoryForm(forms.ModelForm):
    class Meta:
        model = BloodDonationHistory
        fields = "__all__"
