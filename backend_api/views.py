import os
import pickle
from tensorflow.keras.models import load_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictionSerializer
import numpy as np

class PredictView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        import os

    model_path = os.path.join(os.path.dirname(__file__), 'lstm_model.h5')
    scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")

    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found: {scaler_path}")
    
        # Adjust the path to where your model and scaler files are located
        # model_path = os.path.join(os.path.dirname(__file__), 'lstm_model.h5')
        # scaler_path = os.path.join(os.path.dirname(__file__), 'scaler.pkl')

        # # Load the model
        # self.model = load_model(model_path)

        # # Load the scaler
        # with open(scaler_path, 'rb') as f:
        #     self.scaler = pickle.load(f)

    def post(self, request):
        serializer = PredictionSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            input_data = [
                data['age'],
                data['annual_income'],
                data['monthly_inhand_salary'],
                data['interest_rate'],
                data['num_of_loan'],
                data['delay_from_due_date'],
                data['changed_credit_limit'],
                data['num_credit_inquiries'],
                data['credit_mix'],
                data['outstanding_debt'],
                data['credit_utilization_ratio'],
                data['payment_of_min_amount'],
                data['total_emi_per_month'],
                data['payment_behaviour']
            ]
            input_data = np.array(input_data).reshape(1, -1)
            scaled_input = self.scaler.transform(input_data)
            prediction = self.model.predict(scaled_input)
            return Response({'prediction': prediction.tolist()}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
