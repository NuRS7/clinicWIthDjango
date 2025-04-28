from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor, Patient, Appointment
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm

def home(request):
    return render(request, 'appointments/index.html')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'appointments/doctors.html', {'doctors': doctors})

@login_required
def make_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    patient, created = Patient.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.patient = patient
            appointment.save()
            return redirect('doctor_list')
    else:
        form = AppointmentForm()

    return render(request, 'appointments/make_appointment.html', {'form': form, 'doctor': doctor})
