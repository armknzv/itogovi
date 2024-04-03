rom
django.shortcuts
import render, redirect, get_object_or_404

from django.contrib.auth.models import User

from django.core.paginator import Paginator

from Account.models import User_Auth

from .forms import *

from django.contrib.auth.decorators import login_required, permission_required

# для создания сложных условий фильтрации
from django.db.models import Q

# ===== rest_framework =====

from rest_framework import permissions
from rest_framework import viewsets

import django_filters.rest_framework
from App.serializers import *


# create a ReadOnly
class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filterset_fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', ]

    permission_classes = [permissions.IsAuthenticated]
    # XXX: permission_classes = [permissions.IsAdminUser]


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class EngineModelViewSet(viewsets.ModelViewSet):
    queryset = EngineModel.objects.all()
    serializer_class = EngineModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # FIXME: class has to chosen properly!
    permission_classes = [permissions.IsAdminUser]


class TransmissionModelViewSet(viewsets.ModelViewSet):
    queryset = TransmissionModel.objects.all()
    serializer_class = TransmissionModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # NOTE: полный доступ только аутентифицированным пользователям с правами доступа к модели
    permission_classes = [permissions.DjangoModelPermissions]


class DriveAxleModelViewSet(viewsets.ModelViewSet):
    queryset = DriveAxleModel.objects.all()
    serializer_class = DriveAxleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # NOTE: полный доступ аутентифицированным пользователям с правами доступа к модели и только чтение для неаутентифицированных пользователей
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]


class SteeringAxleModelViewSet(viewsets.ModelViewSet):
    queryset = SteeringAxleModel.objects.all()
    serializer_class = SteeringAxleModelSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MaintenanceTypeViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceType.objects.all()
    serializer_class = MaintenanceTypeSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MalfunctionOverviewViewSet(viewsets.ModelViewSet):
    queryset = MalfunctionOverview.objects.all()
    serializer_class = MalfunctionOverviewSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class RepairingMethodViewSet(viewsets.ModelViewSet):
    queryset = RepairingMethod.objects.all()
    serializer_class = RepairingMethodSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MaintenanceCompanyViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceCompany.objects.all()
    serializer_class = MaintenanceCompanySerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ServiceCompanyViewSet(viewsets.ModelViewSet):
    queryset = ServiceCompany.objects.all()
    serializer_class = ServiceCompanySerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    ffilterset_fields = ['id', 'name', 'description', 'role']

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'name', 'description', 'role', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


# Essences
class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['id', 'vehicleNumber', 'vehicleModel', 'engineModel', 'engineNumber', 'transmissionModel',
                        'transmissionNumber', 'driveAxleModel', 'driveAxleNumber', 'steeringAxleModel',
                        'steeringAxleNumber', 'deliveryContract_N_data', 'deliveryDate', 'consignee', 'deliveryAdress',
                        'completeSet', 'client', 'serviceCompany', ]

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


class ClaimsViewSet(viewsets.ModelViewSet):
    queryset = Claims.objects.all()
    serializer_class = ClaimsSerializer

    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'

    # TODO: class has to be chosen properly!
    permission_classes = [permissions.IsAuthenticated | ReadOnly]


# ===== views =====

def html_404(request):
    return render(request, 'App/404.html', {}, status=404)


def indexPage(request):
    return render(request, 'App/index.html', {})


def mainPage(request):
    user = request.user

    # filters block
    # Получение всех доступных моделей автомобилей. distinct() - убирает дубликаты из списка значений
    vehicle_models_names = VehicleModel.objects.values_list('name', flat=True).distinct()
    # Получение всех доступных моделей двигателей.
    engine_models_names = EngineModel.objects.values_list('name', flat=True).distinct()
    # Получение всех доступных Модель трансмиссии.
    transmission_models_names = TransmissionModel.objects.values_list('name', flat=True).distinct()
    # Получение всех доступных Модель трансмиссии.
    transmission_models_names = TransmissionModel.objects.values_list('name', flat=True).distinct()
    # Получение всех доступных Модель ведущего моста.
    driveAxle_models_names = DriveAxleModel.objects.values_list('name', flat=True).distinct()
    # Получение всех доступных Модель управляемого моста.
    steeringAxle_models_names = SteeringAxleModel.objects.values_list('name', flat=True).distinct()

    # Получение значения фильтра из параметров запроса
    filter_vehicle_model = request.GET.get('vehicle_model')
    filter_engine_model = request.GET.get('engine_model')
    filter_transmission_model = request.GET.get('transmission_model')
    filter_driveAxle_model = request.GET.get('driveAxle_model')
    filter_steeringAxle_model = request.GET.get('steeringAxle_model')

    try:
        vehicle_model_id = VehicleModel.objects.get(name=filter_vehicle_model)
    except:
        vehicle_model_id = ''

    try:
        engine_model_id = EngineModel.objects.get(name=filter_engine_model)
    except:
        engine_model_id = ''
    try:
        transmission_model_id = TransmissionModel.objects.get(name=filter_transmission_model)
    except:
        transmission_model_id = ''
    try:
        driveAxle_model_id = DriveAxleModel.objects.get(name=filter_driveAxle_model)
    except:
        driveAxle_model_id = ''
    try:
        steeringAxle_model_id = SteeringAxleModel.objects.get(name=filter_steeringAxle_model)
    except:
        steeringAxle_model_id = ''

        # Roles function
    try:
        role_id = User_Auth.objects.filter(user_auth__username=user).values('role_auth')[0]['role_auth']
        role = Role.objects.get(id=role_id)
    except:
        role = 'Роль не определена'

    try:
        client_id = User_Auth.objects.filter(user_auth__username=user).values('client_auth')[0]['client_auth']
        client_name = Client.objects.get(id=client_id)
    except:
        client_name = ''

    try:
        serviceCompany_id = User_Auth.objects.filter(user_auth__username=user).values('serviceCompany_auth')[0][
            'serviceCompany_auth']
        serviceCompany__name = ServiceCompany.objects.get(id=serviceCompany_id)
    except:
        serviceCompany__name = ''

    manager = False
    client = False
    serviceCompany = False
    role_error = False

    if str(role) == "Manager":
        manager = True
    if str(role) == 'Client':
        client = True
    if str(role) == 'Service Company':
        serviceCompany = True
    if str(role) == 'Роль не определена':
        role_error = True

    # Создаем пустой Q-объект
    q_filter = Q()

    if filter_vehicle_model:
        q_filter &= Q(vehicleModel=vehicle_model_id)

    if filter_engine_model:
        q_filter &= Q(engineModel=engine_model_id)

    if filter_transmission_model:
        q_filter &= Q(transmissionModel=transmission_model_id)

    if filter_driveAxle_model:
        q_filter &= Q(driveAxleModel=driveAxle_model_id)

    if filter_steeringAxle_model:
        q_filter &= Q(steeringAxleModel=steeringAxle_model_id)

    # Применяем фильтры
    if client_name:
        vehicles = Vehicle.objects.filter(client=client_id)
    elif serviceCompany__name:
        vehicles = Vehicle.objects.filter(serviceCompany=serviceCompany_id)
    elif filter_vehicle_model or filter_engine_model or filter_transmission_model or filter_driveAxle_model or filter_steeringAxle_model:
        vehicles = Vehicle.objects.filter(q_filter)
    else:
        vehicles = Vehicle.objects.all().order_by('-deliveryDate')

    # pagination block
    # Получение страницы из параметров запроса
    page_number = request.GET.get('page')

    # Создание объекта Paginator
    paginator = Paginator(vehicles, 5)

    # Получение объекта Page для текущей страницы
    page = paginator.get_page(page_number)

    # if user.is_authenticated-> 1-10 rows will be shown only
    if not user.is_authenticated:
        hideInfo = "display: none;"
    else:
        hideInfo = ''

    return render(request, 'App/main.html',
                  {'vehicles': vehicles, 'page': page, 'vehicle_models_names': vehicle_models_names,
                   'selected_filter': filter_vehicle_model, 'engine_models_names': engine_models_names,
                   'filter_engine_model': filter_engine_model, 'transmission_models_names': transmission_models_names,
                   'filter_transmission_model': filter_transmission_model,
                   'filter_driveAxle_model': filter_driveAxle_model, 'driveAxle_models_names': driveAxle_models_names,
                   'filter_steeringAxle_model': filter_steeringAxle_model,
                   'steeringAxle_models_names': steeringAxle_models_names, 'user': user, 'hideInfo': hideInfo,
                   'role': role, 'manager': manager, 'client': client, 'serviceCompany': serviceCompany,
                   'role_error': role_error, "serviceCompany__name": serviceCompany__name, "client_name": client_name})


def maintenancePage(request):
    user = request.user

    # filters block
    # Получение моделей вид ТО. distinct() - убирает дубликаты из списка значений
    maintenance_type = MaintenanceType.objects.values_list('name', flat=True).distinct()
    # Получение моделей зав.номер машины.
    vehicle_number = Vehicle.objects.values_list('vehicleNumber', flat=True).distinct()
    # Получение моделей сервисная компания.
    service_company = ServiceCompany.objects.values_list('name', flat=True).distinct()

    # Получение значения фильтра из параметров запроса
    filter_maintenance_type = request.GET.get('maintenance_type')
    filter_vehicle_number = request.GET.get('vehicle_number')
    filter_service_company = request.GET.get('service_company')

    try:
        maintenance_type_id = MaintenanceType.objects.get(name=filter_maintenance_type)
    except:
        maintenance_type_id = ''
    try:
        vehicle_number_id = Vehicle.objects.get(vehicleNumber=filter_vehicle_number)
    except:
        vehicle_number_id = ''
    try:
        service_company_id = ServiceCompany.objects.get(name=filter_service_company)
    except:
        service_company_id = ''

    try:
        role_id = User_Auth.objects.filter(user_auth__username=user).values('role_auth')[0]['role_auth']
        role = Role.objects.get(id=role_id)
    except:
        role = 'Роль не определена'

    try:
        client_id = User_Auth.objects.filter(user_auth__username=user).values('client_auth')[0]['client_auth']
        client_name = Client.objects.get(id=client_id)
    except:
        client_name = ''

    try:
        serviceCompany_id = User_Auth.objects.filter(user_auth__username=user).values('serviceCompany_auth')[0][
            'serviceCompany_auth']
        serviceCompany__name = ServiceCompany.objects.get(id=serviceCompany_id)
    except:
        serviceCompany__name = ''

    manager = False
    client = False
    serviceCompany = False
    role_error = False

    if str(role) == "Manager":
        manager = True
    if str(role) == 'Client':
        client = True
    if str(role) == 'Service Company':
        serviceCompany = True
    if role == 'Роль не определена':
        role_error = True

    # Создаем пустой Q-объект
    q_filter = Q()

    if filter_maintenance_type:
        q_filter &= Q(maintenanceType=maintenance_type_id)

    if filter_vehicle_number:
        q_filter &= Q(vehicle=vehicle_number_id)

    if filter_service_company:
        q_filter &= Q(serviceCompany=service_company_id)

    # Применяем фильтры
    if client_name:
        maintenance = Maintenance.objects.filter(vehicle=client_id)
    elif serviceCompany__name:
        maintenance = Maintenance.objects.filter(serviceCompany=serviceCompany_id)
    elif filter_maintenance_type or filter_vehicle_number or filter_service_company:
        maintenance = Maintenance.objects.filter(q_filter)
    else:
        maintenance = Maintenance.objects.all().order_by('-maintenanceDate')

    # pagination block
    # Получение страницы из параметров запроса
    page_number = request.GET.get('page')

    # Создание объекта Paginator
    paginator = Paginator(maintenance, 10)

    # Получение объекта Page для текущей страницы
    page = paginator.get_page(page_number)

    return render(request, 'App/maintenance.html',
                  {'user': user, 'maintenance_type': maintenance_type, 'vehicle_number': vehicle_number,
                   'service_company': service_company, 'filter_maintenance_type': filter_maintenance_type,
                   'filter_vehicle_number': filter_vehicle_number, 'filter_service_company': filter_service_company,
                   'maintenance': maintenance, 'page': page, 'role': role, 'manager': manager, 'client': client,
                   'serviceCompany': serviceCompany, 'role_error': role_error, 'client_name': client_name,
                   'serviceCompany__name': serviceCompany__name})


# @login_required(login_url=html_404)
def claimPage(request):
    user = request.user

    # filters block
    # Получение моделей узел отказа. distinct() - убирает дубликаты из списка значений
    malfunction_node = MalfunctionOverview.objects.values_list('name', flat=True).distinct()
    # Получение моделей способ восстановления;
    reparing_method = RepairingMethod.objects.values_list('name', flat=True).distinct()
    # Получение моделей сервисная компания.
    service_company = ServiceCompany.objects.values_list('name', flat=True).distinct()

    # Получение значения фильтра из параметров запроса
    filter_malfunction_node = request.GET.get('malfunction_node')
    filter_reparing_method = request.GET.get('reparing_method')
    filter_service_company = request.GET.get('service_company')

    try:
        malfunction_node_id = MalfunctionOverview.objects.get(name=filter_malfunction_node)
    except:
        malfunction_node_id = ''
    try:
        reparing_method_id = RepairingMethod.objects.get(name=filter_reparing_method)
    except:
        reparing_method_id = ''
    try:
        service_company_id = ServiceCompany.objects.get(name=filter_service_company)
    except:
        service_company_id = ''

    try:
        role_id = User_Auth.objects.filter(user_auth__username=user).values('role_auth')[0]['role_auth']
        role = Role.objects.get(id=role_id)
    except:
        role = 'Роль не определена'

    try:
        client_id = User_Auth.objects.filter(user_auth__username=user).values('client_auth')[0]['client_auth']
        client_name = Client.objects.get(id=client_id)
    except:
        client_name = ''

    try:
        serviceCompany_id = User_Auth.objects.filter(user_auth__username=user).values('serviceCompany_auth')[0][
            'serviceCompany_auth']
        serviceCompany__name = ServiceCompany.objects.get(id=serviceCompany_id)
    except:
        serviceCompany__name = ''

    manager = False
    client = False
    serviceCompany = False
    role_error = False

    if str(role) == "Manager":
        manager = True
    if str(role) == 'Client':
        client = True
    if str(role) == 'Service Company':
        serviceCompany = True
    if role == 'Роль не определена':
        role_error = True

    # Создаем пустой Q-объект
    q_filter = Q()

    if filter_malfunction_node:
        q_filter &= Q(malfunctionNode=malfunction_node_id)

    if filter_reparing_method:
        q_filter &= Q(reparingMethod=reparing_method_id)

    if filter_service_company:
        q_filter &= Q(serviceCompany=service_company_id)

    # Применяем фильтры
    if client_name:
        claim = Claims.objects.filter(vehicle=client_id)
    elif serviceCompany__name:
        claim = Claims.objects.filter(serviceCompany=serviceCompany_id)
    elif filter_malfunction_node or filter_reparing_method or filter_service_company:
        claim = Claims.objects.filter(q_filter)
    else:
        claim = Claims.objects.all().order_by('-claimDate')

    # pagination block
    # Получение страницы из параметров запроса
    page_number = request.GET.get('page')

    # Создание объекта Paginator
    paginator = Paginator(claim, 10)

    # Получение объекта Page для текущей страницы
    page = paginator.get_page(page_number)

    clients = Client.objects.all()
    # print('clients:', clients)

    return render(request, 'App/claimPage.html',
                  {'user': user, 'malfunction_node': malfunction_node, 'reparing_method': reparing_method,
                   'service_company': service_company, 'filter_malfunction_node': filter_malfunction_node,
                   'filter_reparing_method': filter_reparing_method, 'filter_service_company': filter_service_company,
                   'claim': claim, 'page': page, 'clients': clients, 'role': role, 'manager': manager, 'client': client,
                   'serviceCompany': serviceCompany, 'role_error': role_error, 'client_name': client_name,
                   'serviceCompany__name': serviceCompany__name})


def vehicle_create(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = VehicleForm()

    return render(request, 'App/vehicle_create.html', {'form': form})


def maintenance_create(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('maintenancePage')
    else:
        form = MaintenanceForm()

    return render(request, 'App/maintenance_create.html', {'form': form})


def claim_create(request):
    if request.method == 'POST':
        form = ClaimsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('claimPage')
    else:
        form = ClaimsForm()

    return render(request, 'App/claim_create.html', {'form': form})


def vehicle_edit(request, pk):
    # vehicle = get_object_or_404(Vehicle, id=pk)
    try:
        vehicle = Vehicle.objects.get(id=pk)
    except Vehicle.DoesNotExist:
        return redirect('html_404')

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'App/vehicle_create.html', {'form': form})


def maintenance_edit(request, pk):
    try:
        maintenance = Maintenance.objects.get(id=pk)
    except Maintenance.DoesNotExist:
        return redirect('html_404')

    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = MaintenanceForm(instance=maintenance)

    return render(request, 'App/maintenance_create.html', {'form': form})


def claim_edit(request, pk):
    try:
        claim = Claims.objects.get(id=pk)
    except Claims.DoesNotExist:
        return redirect('html_404')

    if request.method == 'POST':
        form = ClaimsForm(request.POST, instance=claim)
        if form.is_valid():
            form.save()
            return redirect('mainPage')
    else:
        form = ClaimsForm(instance=claim)

    return render(request, 'App/claim_create.html', {'form': form})