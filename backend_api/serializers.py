from rest_framework import serializers

class PredictionSerializer(serializers.Serializer):
    age = serializers.FloatField()
    annual_income = serializers.FloatField()
    monthly_inhand_salary = serializers.FloatField()
    interest_rate = serializers.IntegerField()
    num_of_loan = serializers.FloatField()
    delay_from_due_date = serializers.IntegerField()
    changed_credit_limit = serializers.FloatField()
    num_credit_inquiries = serializers.FloatField()
    credit_mix = serializers.CharField()
    outstanding_debt = serializers.FloatField()
    credit_utilization_ratio = serializers.FloatField()
    payment_of_min_amount = serializers.CharField()
    total_emi_per_month = serializers.FloatField()
    payment_behaviour = serializers.CharField()
