# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Doctor, Patient, Appointment
# from django.contrib.auth.decorators import login_required
# from .forms import AppointmentForm
#
# def home(request):
#     return render(request, 'appointments/index.html')
#
# def doctor_list(request):
#     doctors = Doctor.objects.all()
#     return render(request, 'appointments/doctors.html', {'doctors': doctors})
#
# @login_required
# def make_appointment(request, doctor_id):
#     doctor = get_object_or_404(Doctor, id=doctor_id)
#     patient, created = Patient.objects.get_or_create(user=request.user)
#
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             appointment = form.save(commit=False)
#             appointment.doctor = doctor
#             appointment.patient = patient
#             appointment.save()
#             return redirect('doctor_list')
#     else:
#         form = AppointmentForm()
#
#     return render(request, 'appointments/make_appointment.html', {'form': form, 'doctor': doctor})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Doctor, Patient, Appointment
from .forms import AppointmentForm
from django.utils import timezone
from django.contrib import messages
from .models import Doctor, Specialization
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'appointments/index.html')
def doctors_list(request):
    specialization=request.GET.get('specialization')
    if specialization:
        doctors=Doctor.objects.filter(specialization__iexact=specialization)
    else:
        doctors=Doctor.objects.all()
    return render(request, 'doctors_list.html', {'doctors': doctors})


def doctor_detail(request, doctor_id):
    doctor=get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        form=AppointmentForm(request.POST)
        if form.is_valid():
            appointment_time=form.cleaned_data['appointment_time']
            # Проверяем, свободно ли время
            existing_appointment=Appointment.objects.filter(doctor=doctor, appointment_time=appointment_time).exists()
            if existing_appointment:
                messages.error(request, 'Таңдалған уақыт бос емес. Басқа уақытқа қойыңыз.')
            else:
                # Создаем или находим пациента
                patient, created=Patient.objects.get_or_create(
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    phone_number=form.cleaned_data['phone_number'],
                )
                # Создаем запись
                Appointment.objects.create(
                    doctor=doctor,
                    patient=patient,
                    appointment_time=appointment_time,
                    description=form.cleaned_data['description'],
                )
                messages.success(request, 'Жазылым сәтті аяқталды!')
                return redirect('appointment_confirmation')
    else:
        form=AppointmentForm()

    # Список уже занятых времен для отображения
    booked_times=Appointment.objects.filter(doctor=doctor).values_list('appointment_time', flat=True)

    return render(request, 'doctor_detail.html', {
        'doctor': doctor,
        'form': form,
        'booked_times': booked_times,
    })


@login_required
def make_appointment(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)

    if request.method == 'POST':
        appointment_time = request.POST.get('appointment_time')
        description = request.POST.get('description')

        try:
            patient = request.user.patient
        except Patient.DoesNotExist:
            messages.error(request, 'Қате: сіздің аккаунтыңыз пациент ретінде тіркелмеген.')
            return redirect('dashboard')

        Appointment.objects.create(
            doctor=doctor,
            patient=patient,
            appointment_time=appointment_time,
            description=description
        )

        messages.success(request, 'Сіз сәтті түрде жазылдыңыз!')
        return redirect('dashboard')

    return render(request, 'appointments/make_appointment.html', {'doctor': doctor})
def doctors_by_specialization(request, spec_id):
    specialization = Specialization.objects.get(id=spec_id)
    doctors = Doctor.objects.filter(specialization=specialization)
    return render(request, 'appointments/doctors_by_specialization.html', {
        'specialization': specialization,
        'doctors': doctors
    })

