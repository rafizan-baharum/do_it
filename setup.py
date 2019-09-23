# ==================================================================================================
# # User
# ==================================================================================================
import datetime
from random import randint

from account.models import DoerWallet
from core.models import Staff, User, Doer, Level, State, City
from repository.models import Vendor, Project
from signup.models import INCOME_CHOICES, RACE_CHOICES, GENDER_CHOICES

level = Level()
level.code = 'EMAS'
level.name = 'TAHAP EMAS'
level.daily_task_count = 100
level.save()

level = Level()
level.code = 'PERAK'
level.name = 'TAHAP PERAK'
level.daily_task_count = 50
level.save()

level = Level()
level.code = 'GANGSA'
level.name = 'TAHAP GANGSA'
level.daily_task_count = 20
level.save()

state = State()
state.code = 'WP'
state.name = 'WILAYAH PERSEKUTUAN'
state.save()

state = State()
state.code = 'SL'
state.name = 'SELANGOR'
state.save()

state = State()
state.code = 'PK'
state.name = 'PERAK'
state.save()

state = State()
state.code = 'NS'
state.name = 'NEGERI SEMBILAN'
state.save()

state = State()
state.code = 'MK'
state.name = 'MELAKA'
state.save()

selangorCities = ['KLANG', 'HULU LANGAT', 'KUALA LANGAT', 'SEPANG', 'HULU SELANGOR', 'SABAK BERNAM', 'GOMBAK']

for i in range(len(selangorCities)):
    city = City()
    city.code = f'S{i}'
    city.name = selangorCities[i]
    city.state = State.objects.filter(code='SL').first()
    city.save()


user_staff = User()
user_staff.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
user_staff.username = 'staff1'
user_staff.email = 'staff1@gmail.com'
user_staff.first_name = 'Staff'
user_staff.last_Name = '1'
user_staff.is_staff = True
user_staff.save()

staff = Staff()
staff.user = User.objects.filter(username='staff1').first()
staff.nric_no = '760607-12-4431'
staff.name = 'Rafizi Ramli'
staff.save()

user_staff = User()
user_staff.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
user_staff.username = 'staff2'
user_staff.email = 'staff2@gmail.com'
user_staff.first_name = 'Staff'
user_staff.last_Name = '2'
user_staff.is_staff = True
user_staff.save()

staff = Staff()
staff.user = User.objects.filter(username='staff2').first()
staff.nric_no = '760607-12-4431'
staff.name = 'Siti Fariha Ahmad'
staff.save()

names = ['Azlan Ahmad', 'Jazlan Kasiran', 'Siti Salwa Rahman', 'Sabtu Difrata', 'Junaidi Jun',
         'Jamal Abdallah', 'Ruhaini Suratman', 'Hafiz Selamat', 'Samiul Samiun']
for j in range(9):
    user_doer = User()
    user_doer.password = 'pbkdf2_sha256$150000$kxgoZc1nqo7D$yQUXU5W2GN05Osmwy+PA1yB66W/IJkcsEzB2rdz2B3Y='
    user_doer.username = f'doer{j + 1}'
    user_doer.email = f'doer{j + 1}@gmail.com'
    user_doer.first_name = names[j]
    user_doer.last_Name = names[j]
    user_doer.is_doer = True
    user_doer.save()
    doer = Doer()
    doer.user = User.objects.filter(username=f'doer{j + 1}').first()
    doer.nric_no = f'8{j + 1}0607-12-4431'
    doer.email = f'doer{j + 1}@gmail.com'
    doer.name = names[j]
    doer.birth_date = datetime.date(2019, 9, j + 1)
    doer.level = Level.objects.filter(code='GANGSA').first()
    doer.gender = GENDER_CHOICES[0][0]
    doer.race = RACE_CHOICES[0][0]
    doer.income = INCOME_CHOICES[0][0]
    doer.city = City.objects.first()
    doer.state = State.objects.first()
    doer.save()

vendor = Vendor()
vendor.name = 'Perbandanan Nasional Berhad'
vendor.type = 'GLC'
vendor.save()

vendor = Vendor()
vendor.name = 'Rashid Hussin Bank'
vendor.type = 'GLC'
vendor.save()

vendor = Vendor()
vendor.name = 'MAMPU'
vendor.type = 'GOVERNMENT'
vendor.save()

vendor = Vendor()
vendor.name = 'Jabatan Perdana Menteri'
vendor.type = 'GOVERNMENT'
vendor.save()


# ==================================================================================================
# Randomize Wallet
# ==================================================================================================

# countDoer = Doer.objects.count()
# countProject = Project.objects.count()
# for j in range(10000):
#     random_doer = randint(0, countDoer - 1)
#     random_project = randint(0, countProject - 1)
#     entry = DoerWallet()
#     entry.doer = Doer.objects.all()[random_doer]
#     entry.project = Project.objects.all()[random_project]
#     entry.amount = 0.10
#     entry.save()

print('Done')
