from django.dispatch import receiver, Signal

registration_approved = Signal(providing_args=["registration"])


@receiver(registration_approved)
def registration_approved_created_handler(sender, **kwargs):
    registration = kwargs['registration']

    # todo(mudzaffar):
    # user_doer = User()
    # user_doer.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
    # user_doer.username = f'doer{j + 1}'
    # user_doer.email = f'doer{j + 1}@gmail.com'
    # user_doer.first_name = 'Doer'
    # user_doer.last_Name = '{j+1}'
    # user_doer.is_doer = True
    # user_doer.save()
    #
    # doer = Doer()
    # doer.user = User.objects.filter(username=f'doer{j + 1}').first()
    # doer.nric_no = f'8{j + 1}0607-12-4431'
    # doer.name = 'Siti Fariha Ahmad'
    # doer.save()
