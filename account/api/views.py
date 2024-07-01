from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from account.logic.core import svc_account_register_user
from common.response import get_standard_response


class RegisterView(generics.GenericAPIView):
    def post(self, request):
        try:
            error, user = svc_account_register_user(
                request_data=request.data, serialize=True
            )
            return get_standard_response(error, user)
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)
