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
    return render(request, "Inventory/bag.html", {'form': form})


def show_storage(request):
    bags = Storage.objects.all()
    return render(request, "Inventory/showBag.html", {'bags': bags})


def create(request):
    if request.method == "POST":
        form = DonorForm(request.POST)
        form1 = DonorInformationForm(request.POST)
        tstform = PhysicalTestForm(request.POST)
        donationform = BloodDonationHistoryForm(request.POST)
        medicalform = MedicalHistoryForm(request.POST)
        if form.is_valid() & form1.is_valid() & tstform.is_valid() & donationform.is_valid() & medicalform.is_valid():
            try:
                form.save()
                form1.save()
                tstform.save()
                donationform.save()
                medicalform.save()
                return redirect('/show_donor')
            except:
                pass
    else:
        form = DonorForm()
        form1 = DonorInformationForm()
        tstform = PhysicalTestForm()
        donationform = BloodDonationHistoryForm()
        medicalform = MedicalHistoryForm()
    return render(request, "Donor/donor.html", {'form': form, 'form1': form1, 'tstform': tstform, 'donationform': donationform,
                                          'medicalform': medicalform})


def show_donor(request):
    donate = Donor.objects.all()
    data = DonorInformation.objects.all()
    tstdata = PhysicalTest.objects.all()
    donation = BloodDonationHistory.objects.all()
    bags = MedicalHistory.objects.all()
    return render(request, "Donor/showDonor.html", {'donate': donate, 'data': data, 'tstdata': tstdata, 'donation': donation, 'bags': bags})


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
    return render(request, "Donor/donorInfo.html", {'form': form})


def show_info(request):
    data = DonorInformation.objects.all()
    return render(request, "Donor/showDonorInfo.html", {'data': data})


def test(request):
    if request.method == "POST":
        tstform = PhysicalTestForm(request.POST)
        if tstform.is_valid():
            try:
                tstform.save()
                return redirect('/show_test')
            except:
                pass
    else:
        tstform = PhysicalTestForm()
    return render(request, "physicalTest.html", {'tstform': tstform})


def show_test(request):
    tstdata = PhysicalTest.objects.all()
    return render(request, "showTest.html", {'tstdata': tstdata})


def blood_donation_method(request):
    if request.method == "POST":
        donationform = BloodDonationHistoryForm(request.POST)
        if donationform.is_valid():
            try:
                donationform.save()
                return redirect('/blood_donation_info')
            except:
                pass
    else:
        donationform = BloodDonationHistoryForm()
    return render(request, "Donor/blood_donation.html", {'donationform': donationform})


def blood_donation_info(request):
    donation = BloodDonationHistory.objects.all()
    return render(request, "Donor/show_blood_donation.html", {'donation': donation})


def medical_history_method(request):
    if request.method == "POST":
        medicalform = MedicalHistoryForm(request.POST)
        if medicalform.is_valid():
            try:
                medicalform.save()
                return redirect('/medical_history_show')
            except:
                pass
    else:
        medicalform = MedicalHistoryForm()
    return render(request, "medical_history.html", {'medicalform': medicalform})


def medical_history_show(request):
    bags = MedicalHistory.objects.all()
    return render(request, "show_medical_history.html", {'bags': bags})