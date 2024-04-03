from django import forms
from .models import Vehicle, Maintenance, Claims


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel',
                  'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel', 'steeringAxleNumber',
                  'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress', 'completeSet', 'client',
                  'serviceCompany']


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['maintenanceType', 'maintenanceDate', 'operatingTime', 'workOrderNumber', 'workOrderDate',
                  'maintenanceCompany', 'vehicle', 'serviceCompany', ]


class ClaimsForm(forms.ModelForm):
    class Meta:
        model = Claims
        fields = ['claimDate', 'operatingTime', 'malfunctionNode', 'malfunctionDescription', 'reparingMethod',
                  'usedSpareParts', 'repairingDate', 'vehicleDowntime', 'vehicle', 'serviceCompany', ]
