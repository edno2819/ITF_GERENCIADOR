from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response


class SnippetList(APIView):
    permission_classes = (IsAuthenticated)
    # obriga a equisição vir com Authentication : Bearer  token
