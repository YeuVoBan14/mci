from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import User, Job
from .serializers import JobSerializer, UserSerializer, ChangePasswordSerializer
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login

@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/users',
        'GET /api/users/:id',
        'POST /api/users-create',
        'PUT /api/users/:id',
        'DELETE /api/users/:id',
        'POST /api/change-password/:id',
        'POST /api/login',

        'GET /api/jobs',
        'GET /api/jobs/:id',
        'POST /api/jobs-create',
        'PUT /api/jobs/:id',
        'DELETE /api/jobs/:id',
        'GET /api/jobs-filter',
        'GET /api/jobs-datefilter',
        'GET /api/jobs-applicants'
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
    if isinstance(request.data, list):
        serializer = JobSerializer(data=request.data, many=True)
    else:
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
@api_view(['GET'])
def filterJobs(request):
  keyword = request.GET.get('keyword')
  if keyword:
    filtered_jobs = Job.objects.filter(title__icontains=keyword)
  else:
    filtered_jobs = Job.objects.all()

  serializer = JobSerializer(filtered_jobs, many=True)
  return Response(serializer.data)
@api_view(['GET'])
def filterDateJobs(request):
  startdate  = request.GET.get('startdate')
  if startdate:
    try:
      startdate_utc = datetime.strptime(startdate, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    except ValueError:
      return Response('Invalid start date format')
  if startdate:
    filtered_jobs = Job.objects.filter(date_posted__gte=startdate)
  else:
    filtered_jobs = Job.objects.all()

  serializer = JobSerializer(filtered_jobs, many=True)
  return Response(serializer.data)

@api_view(['POST'])
def createUser(request):
    if isinstance(request.data, list):
        serializer = UserSerializer(data=request.data, many=True)
    else:
        serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updateUser(request, pk):
    user = User.objects.get(pk=pk)
    serializer = UserSerializer(instance=user, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deleteUser(request, pk):
    user = User.objects.get(pk=pk)
    user.delete()
    return Response('Deleted Successfully!')
@api_view(['POST'])
def changePassword(request, pk):
    serializer = ChangePasswordSerializer(data=request.data, context={'user_id': pk})
    if serializer.is_valid():
        user = User.objects.get(id=pk)
        user.set_password(serializer.data['new_password'])
        user.save()
        return Response('Password changed successfully')
    else:
        errors = serializer.errors
        return Response(errors)
@api_view(['POST'])
def loginPage(request):
    data = request.data
    username = data.get('username')
    password = data.get('password')

    if username is None or password is None:
        return Response('Missing username or password')
    user = authenticate(request, username=username, password=password)
    if user is None:
        return Response('Invalid username or password')
    else:
       login(request, user)
       return Response('Login successfully')
#     {
#   "username": "your_username",
#   "password": "your_password"
# }
@api_view(['GET'])
def getJobswithApplicants(request):
    jobs_with_applicants = Job.objects.filter(applicants__isnull=False).prefetch_related('applicants')
    serializer = JobSerializer(jobs_with_applicants, many=True)
    if not serializer.data:
        return Response('No jobs found with applicants')
    for job in serializer.data:
        job['applicants'] = [User.objects.get(pk=applicant).username for applicant in job['applicants']]
    return Response(serializer.data)

    