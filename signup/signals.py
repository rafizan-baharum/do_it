from django.dispatch import receiver, Signal

registration_approved = Signal(providing_args=["registration"])


@receiver(registration_approved)
def registration_approved_created_handler(sender, **kwargs):
    registration = kwargs['registration']

    # todo(mudzaffar):
    # user_volunteer = User()
    # user_volunteer.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
    # user_volunteer.username = f'volunteer{j + 1}'
    # user_volunteer.email = f'volunteer{j + 1}@gmail.com'
    # user_volunteer.first_name = 'Volunteer'
    # user_volunteer.last_Name = '{j+1}'
    # user_volunteer.is_volunteer = True
    # user_volunteer.save()
    #
    # volunteer = Volunteer()
    # volunteer.user = User.objects.filter(username=f'volunteer{j + 1}').first()
    # volunteer.nric_no = f'8{j + 1}0607-12-4431'
    # volunteer.name = 'Siti Fariha Ahmad'
    # volunteer.save()
