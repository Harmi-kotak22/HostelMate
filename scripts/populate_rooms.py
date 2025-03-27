import os
import sys
import django

# Add project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hostel_Management.settings")

# Setup Django
django.setup()

from hostel.models import Room, UserRoom, CustomUser, Vacancy

# # Get a default user
# default_user = CustomUser.objects.first()

# if not default_user:
#     print("❌ No users found! Please create a user first.")
#     sys.exit(1)

# # Create 20 rooms
# for i in range(5, 21):  # 20 rooms
#     room_number = f"{i:03}"
#     room, _ = Room.objects.get_or_create(room_number=room_number)

#     for bed in range(1, 4):  # 3 beds per room
#         # Check if an entry already exists
#         existing_user_room = UserRoom.objects.filter(room=room, bed_no=bed).first()

#         if existing_user_room:
#             # Update user if already exists
#             existing_user_room.user = default_user
#             existing_user_room.save()
#             print(f"🔄 Updated: Room {room_number}, Bed {bed}")
#         else:
#             # Create a new entry if not exists
#             UserRoom.objects.create(room=room, bed_no=bed, user=default_user)
#             print(f"✅ Created: Room {room_number}, Bed {bed}")
# import django
# import os

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Hostel_Management.settings")
# django.setup()

# from hostel.models import Room

# existing_rooms = set(Room.objects.values_list('room_number', flat=True))  # Get existing room numbers
# rooms_to_add = 16

# new_rooms = []
# for i in range(1, 21):  # Assuming Room 1 to Room 20
#     room_name = f"Room {i}"
#     if room_name not in existing_rooms:  # Check if room number exists
#         new_rooms.append(Room(room_number=room_name))

# # Bulk create only if there are new rooms to add
# if new_rooms:
#     Room.objects.bulk_create(new_rooms)
#     print(f"✅ Added {len(new_rooms)} new rooms successfully!")
# else:
#     print("⚠️ No new rooms added. All rooms already exist.")
# Create 16 new rooms with integer room numbers
# new_rooms = [Room(room_number=i) for i in range(6, 21)]  # Assuming 1-4 exist

# # Bulk insert new rooms
# Room.objects.bulk_create(new_rooms)

# print("16 new rooms added successfully!")

# Bed options in each room
BED_CHOICES = ['A', 'B', 'C']

# Step 1: Get all room numbers
all_rooms = Room.objects.values_list('room_number', flat=True)

# Step 2: Get all occupied (room, bed) pairs from UserRoom
occupied_beds = UserRoom.objects.values_list('room__room_number', 'bed_no')

# Convert to a set for fast lookup
occupied_beds_set = set(occupied_beds)

# Step 3: Iterate through all rooms and find vacant beds
vacant_entries = []
for room in all_rooms:
    for bed in BED_CHOICES:
        if (room, bed) not in occupied_beds_set:  # If bed is not occupied, it's vacant
            vacant_entries.append(Vacancy(room_number=str(room), bed_number=bed))

# Step 4: Bulk insert the vacancies
Vacancy.objects.bulk_create(vacant_entries)

print(f"✅ {len(vacant_entries)} vacant beds added to Vacancy table!")

def populate_rooms_and_vacancies():
    # First, create rooms if they don't exist
    existing_rooms = set(Room.objects.values_list('room_number', flat=True))
    
    new_rooms = []
    for i in range(101, 121):  # Room numbers: 101-120
        if i not in existing_rooms:
            new_rooms.append(Room(room_number=i))
    
    if new_rooms:
        Room.objects.bulk_create(new_rooms)
        print(f"✅ Added {len(new_rooms)} new rooms successfully!")
    else:
        print("⚠️ No new rooms needed. All rooms already exist.")
    
    # Now, create vacancies for all available beds
    # First, clear existing vacancies
    Vacancy.objects.all().delete()
    
    # Get all rooms
    all_rooms = Room.objects.all()
    
    # Get occupied beds
    occupied_beds = set(UserRoom.objects.values_list('room__room_number', 'bed_no'))
    
    # Create vacancies for unoccupied beds
    vacant_entries = []
    for room in all_rooms:
        for bed in ['A', 'B', 'C']:  # Each room has 3 beds
            if (room.room_number, bed) not in occupied_beds:
                vacant_entries.append(Vacancy(
                    room_number=str(room.room_number),
                    bed_number=bed
                ))
    
    if vacant_entries:
        Vacancy.objects.bulk_create(vacant_entries)
        print(f"✅ Added {len(vacant_entries)} vacant beds successfully!")
    else:
        print("⚠️ No vacant beds to add.")
    
    # Print current state
    print("\nCurrent State:")
    print(f"Total Rooms: {Room.objects.count()}")
    print(f"Total Vacancies: {Vacancy.objects.count()}")
    
    # Print all rooms and their vacancies
    print("\nVacant Beds:")
    for vacancy in Vacancy.objects.all():
        print(f"Room {vacancy.room_number} - Bed {vacancy.bed_number}")

if __name__ == "__main__":
    populate_rooms_and_vacancies()
