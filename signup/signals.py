from django.dispatch import receiver, Signal

from core.models import User, Doer, Level

registration_approved = Signal(providing_args=["registration"])

@receiver(registration_approved)
def registration_approved_created_handler(sender, **kwargs):
    registration = kwargs['registration']

    user_doer = User()
    user_doer.password = registration.password
    user_doer.username = registration.email
    user_doer.email = registration.email
    user_doer.first_name = registration.name
    user_doer.last_Name = ''
    user_doer.is_doer = True
    user_doer.save()

    doer = Doer()
    doer.user = User.objects.filter(username=registration.email).first()
    doer.email = registration.email
    doer.nric_no = registration.nric_no
    doer.name = registration.name
    doer.birth_date = registration.birth_date
    doer.state = registration.state
    doer.city = registration.city
    doer.gender = registration.gender
    doer.race = registration.race
    doer.level = Level.objects.filter(code='GANGSA').first()
    doer.save()
