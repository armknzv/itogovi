from django.contrib import admin

from .models import *


# Catalogs
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class EngineModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    # list_display = [field.name for field in EngineModel._meta.get_fields()]


class TransmissionModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class DriveAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class SteeringAxleModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class MaintenanceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class MalfunctionOverviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class RepairingMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class MaintenanceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


# Roles for users
class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ServiceCompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


# Essences
class VehicleAdmin(admin.ModelAdmin):
    list_display = (
    'id', 'vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel', 'transmissionNumber',
    'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber', 'deliveryContract_N_data',
    'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client', 'serviceCompany',)


class MaintenanceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Maintenance._meta.get_fields()]


class ClaimsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Claims._meta.get_fields()]


# Catalogs
admin.site.register(VehicleModel, VehicleModelAdmin)
admin.site.register(EngineModel, EngineModelAdmin)
admin.site.register(TransmissionModel, TransmissionModelAdmin)
admin.site.register(DriveAxleModel, DriveAxleModelAdmin)
admin.site.register(SteeringAxleModel, SteeringAxleModelAdmin)
admin.site.register(MaintenanceType, MaintenanceTypeAdmin)
admin.site.register(MalfunctionOverview, MalfunctionOverviewAdmin)
admin.site.register(RepairingMethod, RepairingMethodAdmin)
admin.site.register(MaintenanceCompany, MaintenanceCompanyAdmin)
