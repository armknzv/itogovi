from .models import *
from django.contrib.auth.models import User

from django.conf import settings

from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', ]


# Catalogs
class VehicleModelSerializer(serializers.HyperlinkedModelSerializer):
    # class VehicleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModel
        fields = ['id', 'name', 'description', ]


class EngineModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EngineModel
        fields = ['id', 'name', 'description', ]


class TransmissionModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TransmissionModel
        fields = ['id', 'name', 'description', ]


class DriveAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DriveAxleModel
        fields = ['id', 'name', 'description', ]


class SteeringAxleModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SteeringAxleModel
        fields = ['id', 'name', 'description', ]


class MaintenanceTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceType
        fields = ['id', 'name', 'description', ]


class MalfunctionOverviewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MalfunctionOverview
        fields = ['id', 'name', 'description', ]


class RepairingMethodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RepairingMethod
        fields = ['id', 'name', 'description', ]


class MaintenanceCompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MaintenanceCompany
        fields = ['id', 'name', 'description', ]


# Roles for users
class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = ['id', 'name', ]


class ServiceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCompany
        fields = ['id', 'name', 'description', 'role']

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['role'] = f'{settings.SITE_URL}/api/roles/{data["role"]}'
        return data


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'description', 'role', ]

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['role'] = f'{settings.SITE_URL}/api/roles/{data["role"]}'
        return data


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'name', 'description', 'role', ]

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['role'] = f'{settings.SITE_URL}/api/roles/{data["role"]}'
        return data


# Essences
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ['id', 'vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber',
                  'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client',
                  'serviceCompany', ]

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['vehicleModel'] = f'{settings.SITE_URL}/api/catalog/vehicle_model/{data["vehicleModel"]}'
        data['engineModel'] = f'{settings.SITE_URL}/api/catalog/engine_model/{data["engineModel"]}'
        data['transmissionModel'] = f'{settings.SITE_URL}/api/catalog/transmission_model/{data["transmissionModel"]}'
        data['driveAxleModel'] = f'{settings.SITE_URL}/api/catalog/drive_axle_model/{data["driveAxleModel"]}'
        data['steeringAxleModel'] = f'{settings.SITE_URL}/api/catalog/steering_axle_model/{data["steeringAxleModel"]}'
        data['client'] = f'{settings.SITE_URL}/api/catalog/client/{data["client"]}'
        data['serviceCompany'] = f'{settings.SITE_URL}/api/catalog/service_company/{data["serviceCompany"]}'
        return data


class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['maintenanceType'] = f'{settings.SITE_URL}/api/catalog/maintenance_type/{data["maintenanceType"]}'
        data['maintenanceCompany'] = f'{settings.SITE_URL}/api/catalog/maintenance_company/{data["maintenanceCompany"]}'
        data['vehicle'] = f'{settings.SITE_URL}/api/vehicle/{data["vehicle"]}'
        data['serviceCompany'] = f'{settings.SITE_URL}/api/catalog/service_company/{data["serviceCompany"]}'
        return data


class ClaimsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claims
        fields = '__all__'

    # NOTE: to get link for "roles" instead of just an ID for
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['malfunctionNode'] = f'{settings.SITE_URL}/api/catalog/malfunction_overview/{data["malfunctionNode"]}'
        data['reparingMethod'] = f'{settings.SITE_URL}/api/catalog/repairing_method/{data["reparingMethod"]}'
        data['vehicle'] = f'{settings.SITE_URL}/api/vehicle/{data["vehicle"]}'
        data['serviceCompany'] = f'{settings.SITE_URL}/api/catalog/service_company/{data["serviceCompany"]}'
        return data