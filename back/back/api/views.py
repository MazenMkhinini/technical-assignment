from django.shortcuts import render
from rest_framework import status
from django.views.decorators.http import require_http_methods
from .models import Employee, TimeSlot, TimeSlotOccupation
from .serializers import EmployeeSerializer, TimeSlotSerializer, TimeSlotOccupationSerializer
from django.http import JsonResponse
import json
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

@require_http_methods(['GET'])
def get_employees(request):
  employees = Employee.objects
  serializer = EmployeeSerializer(employees, many=True)
  return JsonResponse({ 'data': serializer.data })

@require_http_methods(['GET'])
def get_timeslots(request):
  timeslots = TimeSlot.objects
  serializer = TimeSlotSerializer(timeslots, many=True)
  return JsonResponse({ 'data': serializer.data })

@require_http_methods(['GET'])
def get_timeslot_occupations(request):
  timeslot_occupations = TimeSlotOccupation.objects
  serializer = TimeSlotOccupationSerializer(timeslot_occupations, many=True)
  return JsonResponse({ 'data': serializer.data })

@require_http_methods(['POST'])
def add_employee(request):
  payload = json.loads(request.body)
  try:
    employee = Employee.objects.create(
      first_name = payload["first_name"],
      last_name = payload["last_name"],
      role = payload["role"]
    )
    serializer = EmployeeSerializer(employee)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@require_http_methods(['POST'])
def add_timeslot(request):
  payload = json.loads(request.body)
  try:
    timeslot = TimeSlot.objects.create(
      start = payload["start"],
      end = payload["end"],
    )
    serializer = TimeSlotSerializer(timeslot)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@require_http_methods(['POST'])
def add_timeslot_occupation(request):
  payload = json.loads(request.body)
  try:
    timeslot = TimeSlotOccupation.objects.create(
      employee = Employee.objects.get(id=payload["employee"]),
      timeslot = TimeSlot.objects.get(id=payload["timeslot"]),
    )
    serializer = TimeSlotOccupationSerializer(timeslot)
    return JsonResponse({'data': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
  except ObjectDoesNotExist as e:
    return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
  except Exception as e:
    print(e)
    return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@require_http_methods(['DELETE'])
def delete_employee(request, id):
  Employee.objects.filter(id=id).delete()
  return JsonResponse({'success': 1})

@require_http_methods(['DELETE'])
def delete_timeslot(request, id):
  TimeSlot.objects.filter(id=id).delete()
  return JsonResponse({'success': 1})

@require_http_methods(['DELETE'])
def delete_timeslot_occupation(request, id):
  TimeSlotOccupation.objects.filter(id=id).delete()
  return JsonResponse({'success': 1})