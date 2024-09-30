from django.shortcuts import render, get_object_or_404
from programs.models import Programs


def program_detail_view(request, slug):
    # گرفتن برنامه با استفاده از slug یا نمایش 404 در صورت نبود
    program = get_object_or_404(Programs, slug=slug)

    # دسترسی به جزئیات مرتبط با برنامه از طریق ارتباط OneToOne
    program_details = program.details.first()  # اگر ارتباط OneToOne وجود داشته باشد

    context = {
        'program': program,
        'program_detail': program_details
    }

    return render(request, 'prog_detail/program_details.html', context)
