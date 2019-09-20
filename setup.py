# ==================================================================================================
# # User
# ==================================================================================================
from random import randint

from account.models import VolunteerWallet
from core.models import Staff, User, Volunteer
from repository.models import Vendor, Project

# user_staff = User()
# user_staff.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
# user_staff.username = 'staff1'
# user_staff.email = 'staff1@gmail.com'
# user_staff.first_name = 'Staff'
# user_staff.last_Name = '1'
# user_staff.is_staff = True
# user_staff.save()
#
# staff = Staff()
# staff.user = User.objects.filter(username='staff1').first()
# staff.nric_no = '760607-12-4431'
# staff.name = 'Rafizi Ramli'
# staff.save()
#
# user_staff = User()
# user_staff.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
# user_staff.username = 'staff2'
# user_staff.email = 'staff2@gmail.com'
# user_staff.first_name = 'Staff'
# user_staff.last_Name = '2'
# user_staff.is_staff = True
# user_staff.save()
#
# staff = Staff()
# staff.user = User.objects.filter(username='staff2').first()
# staff.nric_no = '760607-12-4431'
# staff.name = 'Siti Fariha Ahamd'
# staff.save()

# for j in range(9):
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

vendor = Vendor()
vendor.name = 'Perbandanan Nasional Berhad'
vendor.type = 'GLC'
vendor.save()

# vendor = Vendor()
# vendor.name = 'Rashid Hussin Bank'
# vendor.type = 'GLC'
# vendor.save()
#
# vendor = Vendor()
# vendor.name = 'MAMPU'
# vendor.type = 'GOVERNMENT'
# vendor.save()
#
# vendor = Vendor()
# vendor.name = 'Jabatan Perdana Menteri'
# vendor.type = 'GOVERNMENT'
# vendor.save()

# ==================================================================================================
# Randomize Wallet
# ==================================================================================================

countVolunteer = Volunteer.objects.count()
countProject = Project.objects.count()
for j in range(10000):
    random_volunteer = randint(0, countVolunteer - 1)
    random_project = randint(0, countProject - 1)
    entry = VolunteerWallet()
    entry.volunteer = Volunteer.objects.all()[random_volunteer]
    entry.project = Project.objects.all()[random_project]
    entry.amount = 0.10
    entry.save()

print('Done')


