from rest_framework import serializers
from .models import Employee, TimeSlot, TimeSlotOccupation

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'role']

class TimeSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlot
        fields = ['id', 'start', 'end']

class TimeSlotOccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeSlotOccupation
        fields = ['id', 'employee', 'timeslot']
