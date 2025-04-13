from django.db import models,migrations
from django.contrib.auth.models import User,Group


# def create_groups(apps, schema_editor):
#     Group: models.Model= apps.get_model('auth', 'Group')
#     Group.objects.get_or_create(name='Admin')
#     Group.objects.get_or_create(name='Doctor')
#     Group.objects.get_or_create(name='Receptionist')
#     Group.objects.get_or_create(name='Pharmacist')
#     Group.objects.get_or_create(name='Lab Technician')

# class Migration(migrations.Migration):
#     dependencies = [
#         ('auth', '0001_initial'), 
#     ]
    
#     operations = [  
#         migrations.RunPython(create_groups),
#     ]

class Role(models.Model):
    RoleId = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.RoleName

class Userdetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Signup(models.Model):
    SignupID = models.AutoField(primary_key=True)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='signups')
    UserName = models.CharField(max_length=50)
    EmailId = models.EmailField(unique=True)
    Password = models.CharField(max_length=128)

    def __str__(self):
        return self.UserName
    
    @property
    def id(self):
        return self.SignupID

class Login(models.Model):
    UserId = models.AutoField(primary_key=True)
    Signup = models.OneToOneField(Signup, on_delete=models.CASCADE, related_name='login')
    LastLogin = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Login for {self.Signup.UserName}"


class Department(models.Model):
    DepartmentId = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=50)

    def __str__(self):
        return self.DepartmentName

class Doctor(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    DoctorId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20, choices=GenderChoices.choices, default=GenderChoices.MALE)
    Date_of_Birth = models.DateField()
    Date_of_Joining = models.DateField()
    EmailId = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    Address = models.TextField()
    Specialization = models.CharField(max_length=100)
    Consultant_fees = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    IsActive = models.BooleanField(default=True)
    Date=models.DateTimeField(auto_now_add=True, null=True)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True, related_name='department_doctors')
    Role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='role_doctors')

    def __str__(self):
        return f"Dr. {self.FirstName} {self.LastName}"
    
    def full_name(self):
        return f"{self.FirstName} {self.LastName}"


class StaffManage(models.Model):
    class GenderChoices(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'
        OTHER = 'other', 'Other'

    class BloodChoices(models.TextChoices):
        Ap = 'A+', 'A+'
        An = 'A-', 'A-'
        Bp = 'B+', 'B+'
        Bn = 'B-', 'B-'
        AB = 'AB+', 'AB+'
        ABn = 'AB-', 'AB-'
        Op = 'O+', 'O+'
        On = 'O-', 'O-'

    StaffId = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=20, choices=GenderChoices.choices, default=GenderChoices.MALE)
    Date_of_Birth = models.DateField()
    Date_of_Joining = models.DateField(auto_now_add=False)
    BloodGroup = models.CharField(max_length=20, choices=BloodChoices.choices, default=BloodChoices.Op)
    EmailId = models.EmailField()
    phone_Number = models.CharField(max_length=15)
    Address = models.TextField()
    date=models.DateTimeField(auto_now_add=True, null=True)
    Role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True, related_name='role_staff')

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"


class Pharm(models.Model):
    MedicineId = models.AutoField(primary_key=True)
    MedicineName = models.CharField(max_length=100)
    Quantity = models.IntegerField()
    Expiry_Date = models.DateField()
    PricePerUnit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lowStock = models.IntegerField()
    supplier = models.CharField(max_length=100)
    Date=models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.MedicineName
    
    @property
    def total_value(self):
        return self.Quantity * self.PricePerUnit
    
    def is_low_stock(self):
        return self.Quantity <= self.lowStock

class Batch(models.Model):
    BatchId = models.AutoField(primary_key=True)
    ManufacturingDate = models.DateField()
    Pharm = models.ForeignKey(Pharm, on_delete=models.SET_NULL, null=True, blank=True, related_name='medicine_batches')

    def __str__(self):
        return self.Pharm.MedicineName if self.Pharm else "Unknown Medicine"


class LabDevice(models.Model):
    class StatusChoices(models.TextChoices):
        WORKING = 'working', 'working'
        UNDERMAINTENANCE = 'undermaintenance', 'undermaintenance'
        STANDBY = 'standby', 'standby'
        OUTOFORDER = 'outoforder', 'outoforder'

    ModuleId = models.AutoField(primary_key=True)
    EquipmentName = models.CharField(max_length=250)
    Quantity = models.IntegerField()
    Date=models.DateTimeField(auto_now_add=True, null=True)
    Last_Service_Date = models.DateField()
    Next_Service_Date = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.WORKING)

    def __str__(self):
        return self.EquipmentName