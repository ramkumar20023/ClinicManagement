from django.db import models

# Create your models here.

# Admin models

class Role(models.Model):
    RoleId= models.AutoField(primary_key=True)
    RoleName=models.CharField(max_length=50)

    def __str__(self):
        return self.RoleName

class Signup(models.Model):
    SignupID=models.AutoField(primary_key=True)
    Role=models.ForeignKey(Role, on_delete=models.CASCADE)
    UserName=models.CharField(max_length=50)
    EmailId=models.EmailField()
    Password=models.CharField(max_length=15)

    def __str__(self):
        return self.UserName

class Login(models.Model):
    UserId=models.AutoField(primary_key=True)
    Signup=models.ForeignKey(Signup, on_delete=models.CASCADE)
    Role=models.ForeignKey(Role, on_delete=models.CASCADE)
    EmailId=models.EmailField()
    Password=models.CharField(max_length=15)

    def __str__(self):
        return f"Login for {self.Signup.UserName}"

class Department(models.Model):
    DepartmentId=models.AutoField(primary_key=True)
    DepartmentName=models.CharField(max_length=50)

    def __str__(self):
        return self.DepartmentName

class Doctor(models.Model):
    class GenderChoices(models.TextChoices):
        MALE='male','Male'
        FEMALE='female','Female'
        OTHER='other','Other'

    DoctorId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20, choices=GenderChoices.choices, default=GenderChoices.MALE)
    Date_of_Birth=models.DateField()
    Date_of_Joining=models.DateField()
    EmailId=models.EmailField()
    phone_Number=models.CharField(max_length=15)
    Address=models.TextField()
    Specialization=models.CharField(max_length=100)
    Consultant_fees=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    IsActive=models.BooleanField(default=True)
    Department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    UserId=models.ForeignKey(Login, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Dr. {self.FirstName} {self.LastName}"
    
    def full_name(self):
        return f"{self.FirstName} {self.LastName}"

class StaffManage(models.Model):
    class GenderChoices(models.TextChoices):
        MALE='male','Male'
        FEMALE='female','Female'
        OTHER='other','Other'

    class BloodChoices(models.TextChoices):
        Ap='A+','A+'
        An='A-','A-'
        Bp='B+','B+'
        Bn='B-','B-'
        AB='AB+','AB+'
        ABn='AB-','AB-'
        Op='O+','O+'
        On='O-','O-'

    StaffId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Age=models.IntegerField()
    Gender=models.CharField(max_length=20, choices=GenderChoices.choices, default=GenderChoices.MALE)
    Date_of_Birth=models.DateField()
    BloodGroup=models.CharField(max_length=20, choices=BloodChoices.choices, default=BloodChoices.Op)
    EmailId=models.EmailField()
    phone_Number=models.CharField(max_length=15)
    Address=models.TextField()
    Role=models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, blank=True)
    Login=models.ForeignKey(Login, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"
    
class Pharm(models.Model):
    MedicineId=models.AutoField(primary_key=True)
    MedicineName=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    Expiry_Date=models.DateField()
    PricePerUnit=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    lowStock=models.IntegerField()
    supplier=models.CharField(max_length=100)

    def __str__(self):
        return self.MedicineName
    
    @property
    def total_value(self):
        return self.Quantity * self.PricePerUnit
    
    def is_low_stock(self):
        return self.Quantity <= self.lowStock

class Batch(models.Model):
    BatchId=models.AutoField(primary_key=True)
    ManufacturingDate = models.DateField()
    Pharm=models.ForeignKey(Pharm, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Pharm.MedicineName

class LabDepartment(models.Model):
    LabId=models.AutoField(primary_key=True)
    EquipmentName=models.CharField(max_length=250)
    Department=models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.EquipmentName
        
class LabDevice(models.Model):
    class StatusChoices(models.TextChoices):
        WORKING='working','Working'
        UNDERMAINTENANCE='undermaintenance','Under Maintenance'
        STANDBY='standby','Standby'
        OUTOFORDER='outoforder','Out of Order'

    ModuleId=models.AutoField(primary_key=True)
    EquipmentName=models.CharField(max_length=250)
    Quantity=models.IntegerField()
    Last_Service_Date=models.DateField()
    Next_Service_Date = models.DateField(null=True, blank=True)
    Status=models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.WORKING)

    def __str__(self):
        return self.EquipmentName
    
# LabTechnician Models
class LabTest(models.Model):
    LaboratoryId=models.AutoField(primary_key=True)
    LabDepartment=models.ForeignKey(LabDepartment, on_delete=models.SET_NULL, null=True, blank=True)
    TestName=models.CharField(max_length=255)
    TestResult=models.TextField()
    ResultDate = models.DateTimeField(null=True, blank=True)
    DeviceCharge=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ServiceCharge=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    TestingCharge=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Technician = models.ForeignKey(StaffManage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.TestName
    
    @property
    def total_charges(self):
        return self.DeviceCharge + self.ServiceCharge + self.TestingCharge

class LabBill(models.Model):
    LabBillId=models.AutoField(primary_key=True)
    TotalPrice=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    LabTest=models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.TotalPrice = self.LabTest.total_charges
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.LabBillId} for {self.LabTest.TestName}"

# Pharmacist Models
class Pharmacist(models.Model):
    PharmId=models.AutoField(primary_key=True)
    Pharm=models.ForeignKey(Pharm, on_delete=models.SET_NULL, null=True, blank=True)
    MedicineName=models.CharField(max_length=100)
    Quantity=models.IntegerField()
    PricePerUnit=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # TotalPrice=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    @property
    def total_price(self):
        return self.Quantity * self.PricePerUnit

    def __str__(self):
        return f"{self.MedicineName} x{self.Quantity}"
    
class PharmBill(models.Model):
    BillId=models.AutoField(primary_key=True)
    Pharmacist=models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    TotalPrice=models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.TotalPrice = self.Pharmacist.total_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.BillId}"
    
# Receptionist Models
class PatientDetails(models.Model):
    class GenderChoices(models.TextChoices):
        MALE='male','Male'
        FEMALE='female','Female'
        OTHER='other','Other'

    class BloodChoices(models.TextChoices):
        Ap='A+','A+'
        An='A-','A-'
        Bp='B+','B+'
        Bn='B-','B-'
        AB='AB+','AB+'
        ABn='AB-','AB-'
        Op='O+','O+'
        On='O-','O-'

    PatientId=models.AutoField(primary_key=True)
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    age=models.IntegerField()
    DOb=models.DateField()
    Gender=models.CharField(max_length=20, choices=GenderChoices.choices)
    BloodGroup=models.CharField(max_length=20, choices=BloodChoices.choices, default=BloodChoices.Op)
    Address=models.TextField()
    phonenumber=models.CharField(max_length=15)
    EmergencyContact=models.CharField(max_length=15)
    alergy=models.TextField(blank=True, null=True)
    RegisterationDate=models.DateTimeField(auto_now_add=True)
    LastVisitDate = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

    @property
    def full_name(self):
        return f"{self.FirstName} {self.LastName}"

class Appointment(models.Model):
    class statuschoices(models.TextChoices):
        SCHEDULED='scheduled','Scheduled'
        COMPLETED='completed','Completed'
        CANCELLED='cancelled','Cancelled'

    AppointmentId=models.AutoField(primary_key=True)
    PatientDetails=models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    Doctor=models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    # Doctor_FirstName=models.CharField(max_length=100, null=True, blank=True)
    # Doctor_LastName=models.CharField(max_length=100, null=True, blank=True)
    AppointmentDate=models.DateTimeField()
    Status=models.CharField(max_length=50, choices=statuschoices.choices, default=statuschoices.SCHEDULED)
    Remarks=models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment #{self.AppointmentId} - {self.PatientDetails.full_name}"

class AppointmentBill(models.Model):
    BillId=models.AutoField(primary_key=True)
    Appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Consultant_fees=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    ServiceCharge=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Total_cost=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    Created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.Total_cost = self.Consultant_fees + self.ServiceCharge
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bill #{self.BillId} for Appointment #{self.Appointment.AppointmentId}"
    

# Doctor Management

class Prescription(models.Model):
    PrescriptionId=models.AutoField(primary_key=True)
    Frequency=models.CharField(max_length=100)
    Dosage=models.CharField(max_length=100)
    No_of_Days=models.IntegerField()
    Appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Medicine = models.ForeignKey(Pharm, on_delete=models.SET_NULL, null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Prescription #{self.PrescriptionId}"


class LabTesting(models.Model):
    TestingId=models.AutoField(primary_key=True)
    TestName=models.CharField(max_length=255)
    Notes=models.TextField(blank=True, null=True)
    Appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Test = models.ForeignKey(LabTest, on_delete=models.SET_NULL, null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TestName

class Consultation(models.Model):
    ConsultantId=models.AutoField(primary_key=True)
    Notes=models.TextField()
    Prescription=models.ForeignKey(Prescription, on_delete=models.SET_NULL, null=True, blank=True)
    LabTesting=models.ForeignKey(LabTesting, on_delete=models.SET_NULL, blank=True, null=True)
    Appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation #{self.ConsultantId}"
    
class LabTestReport(models.Model):
    ReportID=models.AutoField(primary_key=True)
    LabTesting=models.ForeignKey(LabTesting, on_delete=models.CASCADE)
    LabTechnician=models.ForeignKey(StaffManage, on_delete=models.PROTECT)
    Appointment=models.ForeignKey(Appointment, on_delete=models.CASCADE)
    Findings = models.TextField()
    # ReportDeliveryDate = models.DateField(null=True, blank=True)
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report #{self.ReportID} for {self.LabTesting.TestName}"


class PatientHistory(models.Model):
    RecordId=models.AutoField(primary_key=True)
    Consultation=models.ForeignKey(Consultation, on_delete=models.CASCADE)
    Diagnosis = models.TextField()
    Treatment = models.TextField()
    Created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History Record #{self.RecordId}"