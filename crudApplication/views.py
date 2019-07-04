from django.shortcuts import render, redirect
from crudApplication.forms import ConsentForm, RecipientForm, ChargeForm, BloodTestForm, StorageForm, DonorForm, DonorInformationForm, PhysicalTestForm, BloodDonationHistoryForm, MedicalHistoryForm
from crudApplication.models import Consent, Recipient, Charge, BloodTest, Storage, Donor, DonorInformation, PhysicalTest, BloodDonationHistory, MedicalHistory


def consent_method(request):
    if request.method == "POST":
        form = ConsentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_consent')
            except:
                pass
    else:
        form = ConsentForm()
    return render(request, "consent.html", {'form': form})


def show_consent(request):
    consent = Consent.objects.all()
    return render(request, "showConsent.html", {'consent': consent})


def receive(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_recipient')
            except:
                pass
    else:
        form = RecipientForm()
    return render(request, "recipient.html", {'form': form})


def show_recipient(request):
    recipients = Recipient.objects.all()
    return render(request, "showRecipient.html", {'recipients': recipients})


def cost(request):
    if request.method == "POST":
        form = ChargeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_charge')
            except:
                pass
    else:
        form = ChargeForm()
    return render(request, "charge.html", {'form': form})


def show_charge(request):
    charges = Charge.objects.all()
    return render(request, "showCharge.html", {'charges': charges})


def blood_test_method(request):
    if request.method == "POST":
        form = BloodTestForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_blood_test')
            except :
                pass
    else:
        form = BloodTestForm()
    return render(request, "blood_test.html", {'form': form})


def show_blood_test(request):
    blood_test_1 = BloodTest.objects.all()
    return render(request, "show_blood_test.html", {'blood_test_1': blood_test_1})


def store(request):
    if request.method == "POST":
        form = StorageForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_storage')
            except:
                pass
    else:
        form = StorageForm()
    return render(request, "bag.html", {'form': form})


def show_storage(request):
    bags = Storage.objects.all()
    return render(request, "showBag.html", {'bags': bags})


def create(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_donor')
            except:
                pass
    else:
        form = DonorForm()
    return render(request, "donor.html", {'form': form})


def show_donor(request):
    donate = Donor.objects.all()
    return render(request, "showDonor.html", {'donate': donate})


def info(request):
    if request.method == "POST":
        form = DonorInformationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_info')
            except:
                pass
    else:
        form = DonorInformationForm()
    return render(request, "donorInfo.html", {'form': form})


def show_info(request):
    data = DonorInformation.objects.all()
    return render(request, "showDonorInfo.html", {'data': data})


def test(request):
    if request.method == "POST":
        form = PhysicalTestForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_test')
            except:
                pass
    else:
        form = PhysicalTestForm()
    return render(request, "physicalTest.html", {'form': form})


def show_test(request):
    data = PhysicalTest.objects.all()
    return render(request, "showTest.html", {'data': data})


def blood_donation_method(request):
    if request.method == "POST":
        form = BloodDonationHistoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/blood_donation_info')
            except:
                pass
    else:
        form = BloodDonationHistoryForm()
    return render(request, "blood_donation.html", {'form': form})


def blood_donation_info(request):
    bags = BloodDonationHistory.objects.all()
    return render(request, "show_blood_donation.html", {'bags': bags})


def medical_history_method(request):
    if request.method == "POST":
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/medical_history_show')
            except:
                pass
    else:
        form = MedicalHistoryForm()
    return render(request, "medical_history.html", {'form': form})


def medical_history_show(request):
    bags = MedicalHistory.objects.all()
    return render(request, "show_medical_history.html", {'bags': bags})