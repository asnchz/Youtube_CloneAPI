from .models import Comment
from .models import Reply
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer
from .serializers import ReplySerializer

# Create your views here.
class ReplyList(APIView):
    def 