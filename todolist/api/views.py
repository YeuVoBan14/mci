from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import User, Job
from .serializers import JobSerializer, UserSerializer

@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/users/:id',
        'GET /api/jobs',
        'GET /api/jobs/:id'
    ]
    return Response(routes)
@api_view(['GET'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getUser(request, pk):
    users = User.objects.get(id=pk)
    serializer = UserSerializer(users, many=False)
    return Response(serializer.data)
@api_view(['GET'])
def getJobs(request):
    jobs = Job.objects.all()
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getJob(request, pk):
    jobs = Job.objects.get(id=pk)
    serializer = JobSerializer(jobs, many=False)
    return Response(serializer.data)
@api_view(['POST'])
def createJob(request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updateJob(request, pk):
    job = Job.objects.get(pk=pk)
    serializer = JobSerializer(instance=job, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteJob(request, pk):
    job = Job.objects.get(pk=pk)
    job.delete()
    return Response('Deleted Successfully!')
    