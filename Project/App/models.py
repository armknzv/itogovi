from django.db import models
from django.contrib.auth.models import User


# Catalogs
class VehicleModel(models.Model):
    '''Vehicle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class EngineModel(models.Model):
    '''Engine model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class TransmissionModel(models.Model):
    '''Transmission model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class DriveAxleModel(models.Model):
    '''Drive axle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class SteeringAxleModel(models.Model):
    '''Steering axle model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class MaintenanceType(models.Model):
    '''maintenance Type model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class MalfunctionOverview(models.Model):
    '''Malfunction Overview model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class RepairingMethod(models.Model):
    '''Repairing Method model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class MaintenanceCompany(models.Model):
    '''Maintenance Company model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


# Roles for users
class Role(models.Model):
    '''Roles Company model'''
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class ServiceCompany(models.Model):
    '''Service Company model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class Client(models.Model):
    '''Client model'''
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


class Manager(models.Model):
    '''Manager model'''
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.name}'


# Essences
class Vehicle(models.Model):
    '''Vehicle model'''
    vehicleNumber = models.TextField()  # Зав. № машины
    vehicleModel = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)  # Модель техники
    engineModel = models.ForeignKey(EngineModel, on_delete=models.CASCADE)  # Модель двигателя
    engineNumber = models.TextField()  # Зав. № двигателя
    transmissionModel = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE)  # Модель трансмиссии
    transmissionNumber = models.TextField()  # Зав. № трансмиссии
    driveAxleModel = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE)  # Модель ведущего моста
    driveAxleNumber = models.TextField()  # Зав. № ведущего моста
    steeringAxleModel = models.ForeignKey(SteeringAxleModel, on_delete=models.CASCADE)  # Модель управляемого моста
    steeringAxleNumber = models.TextField()  # Зав. № управляемого моста
    deliveryContract_N_data = models.TextField()  # Договор поставки №, дата
    deliveryDate = models.DateField()  # Дата отгрузки с завода
    consignee = models.TextField()  # Грузополучатель (конечный потребитель)
    deliveryAdress = models.TextField()  # Адрес поставки (эксплуатации)
    completeSet = models.TextField()  # Комплектация (доп. опции)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Клиент
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)  # Сервисная компания

    def __str__(self):
        """ return a propper view for the admin panel """
        return f'{self.vehicleNumber}'


class Maintenance(models.Model):
    '''Maintenance model'''
    maintenanceType = models.ForeignKey(MaintenanceType, on_delete=models.CASCADE)  # Вид ТО
    maintenanceDate = models.DateField()  # Дата проведения ТО
    operatingTime = models.IntegerField()  # Наработка, м/час
    workOrderNumber = models.TextField()  # № заказ-наряда
    workOrderDate = models.DateField()  # Дата заказ-наряда
    maintenanceCompany = models.ForeignKey(MaintenanceCompany, on_delete=models.CASCADE)  # Организация, проводившая ТО
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Машина
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)  # Сервисная компания


class Claims(models.Model):
    '''Claims model'''
    claimDate = models.DateField()  # Дата отказа
    operatingTime = models.IntegerField()  # Наработка, м/час
    malfunctionNode = models.ForeignKey(MalfunctionOverview, on_delete=models.CASCADE)  # Узел отказа
    malfunctionDescription = models.TextField()  # Описание отказа
    reparingMethod = models.ForeignKey(RepairingMethod, on_delete=models.CASCADE)  # Способ восстановления
    usedSpareParts = models.TextField()  # Используемые запасные части
    repairingDate = models.DateField()  # Дата восстановления
    vehicleDowntime = models.IntegerField()  # Время простоя техники -> calculated = repairingDate - claimDate
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)  # Mашина
    serviceCompany = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE)  # Cервисная компания