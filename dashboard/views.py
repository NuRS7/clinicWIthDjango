from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from appointments.models import Doctor, Appointment, Specialization

@login_required
def dashboard_view(request):
    user = request.user

    if user.is_patient:
        doctors = Doctor.objects.all()
        specializations = Specialization.objects.all()
        return render(request, 'dashboard/index.html', {
            'user': user,
            'doctors': doctors,
            'specializations': specializations
        })

    elif user.is_doctor:
        try:
            doctor = Doctor.objects.get(user=user)
            appointments = Appointment.objects.filter(doctor=doctor)

        except Doctor.DoesNotExist:
            appointments = []
        return render(request, 'dashboard/doctor_dashboard.html', {
            'user': user,
            'appointments': appointments,
        })

    else:
        messages.error(request, "Сізде кіруге рұқсат жоқ. ")
        return redirect('login')

@require_POST
@login_required
def complete_appointment(request, appointment_id):
    user = request.user

    if user.is_doctor:
        appointment = get_object_or_404(Appointment, id=appointment_id)
        if appointment.doctor.user == user:
            appointment.delete()
            messages.success(request, 'Сеанс сәтті аяқталды және жазылым бітті')
        else:
            messages.error(request, 'Сіз біреудің сеансын өшіре алмайсыз')
    else:
        messages.error(request, 'Доктор ғана сеансты өшіре алады')

    return redirect('dashboard')

def list(request):
    return render(request, 'dashboard/index.html')

