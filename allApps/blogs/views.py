from django.shortcuts import render
from .forms import *
from .models import *
from ..userAccounts.views import * 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
import json

# Creating API for performing CRUD only for the admin
class blogsApi(APIView):
    # get method
    def get(self, request):
        user = request.user
        if user.is_superuser:
            data = blogs.objects.all()
            serializer = blogSerializers(data, many=True)
            return Response({
                'status': 200,
                'message': 'Data fetched',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 200,
                'message': 'Only admin Have the access to this data',
            })

    # post method
    def post(self, request):
        user = request.user
        serializer = blogSerializers(data = request.data)
        if user.is_superuser:
            if serializer.is_valid():
                serializer.save(author = user)
                return Response({
                    'status': 200,
                    'message': 'Data Submited',
                    'data': serializer.data
                })
            print(serializer.errors)
            return Response({
                'status': 403,
                'message': 'Data cannot be submited',
            })
        else:
            return Response({
                'status': 200,
                'message': 'Only admin Have the access to this data',
            })

    # update method
    def put(self, request):
        user = request.user
        print(user.is_superuser)
        if user.is_superuser:
            id = request.data['id']
            blogObj = blogs.objects.get(pk = id)
            if blogObj:
                serializer = blogSerializers(blogObj, data = request.data)
                if serializer.is_valid():
                    serializer.save(author = user)
                    return Response({
                        'status': 200,
                        'message': 'Data updated',
                        'data': serializer.data
                    })
                else:
                    return Response({
                        'status': 403,
                        'error': serializer.errors
                    })

            else:
                return Response({
                    'status': 403,
                    'messages': f"Invalid Id - {id}"
                })
        else:
            return Response({
                'status': 200,
                'message': 'Only admin Have the access to this data',
            })
   
    # patch method
    def patch(self, request):
        user = request.user
        if user.is_superuser:
            id = request.data['id']
            blogObj = blogs.objects.get(pk = id)
            if blogObj:
                serializer = blogSerializers(blogObj, data = request.data)
                if serializer.is_valid():
                    serializer.save(author = user)
                    return Response({
                        'status': 200,
                        'message': 'Data updated',
                        'data': serializer.data
                    })
                else:
                    return Response({
                        'status': 403,
                        'error': serializer.errors
                    })

            else:
                return Response({
                    'status': 403,
                    'messages': f"Invalid Id - {id}"
                })
        else:
            return Response({
                'status': 200,
                'message': 'Only admin Have the access to this data',
            })

    # delete method
    def delete(self, request):
        user = request.user
        if user.is_superuser:
            try:
                id = request.data['id']
                blogObj = blogs.objects.get(pk = id)
                blogObj.delete()
                return Response({
                    'status': 200,
                    'message': 'Data Deleted',
                })
            except:
                return Response({
                    'status': 403,
                    'messages': "Invalid Id"
                })
        else:
            return Response({
                'status': 200,
                'message': 'Only admin Have the access to this data',
            })


# create blog -for users
@login_required(login_url='user-login')
def createBlog(request):
    form = blogsForm()
    if request.method == 'POST':
        form = blogsForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            messages.info(request, "Post successfully saved ")
            return redirect('home')
    context = {
        'form' : form
    }
    return render(request, "blogs/postBlog.html", context)

# delete blog for -user
@login_required(login_url='user-login')
def deleteBlog(request, id):
    user = request.user
    obj = blogs.objects.get(pk = id)
    if obj.author == user:
        obj.delete()
        messages.info(request, "Post Deleted Successfully")
        return redirect('user_profile')
    else:
        messages.info(request, "You are not authorised to delete this post")
        return redirect('user_profile')

# list post for users
@login_required(login_url='user-login')
def listPost(request):
    data = blogs.objects.all()
    context = {
        'data': data
    }
    return render(request, 'blogs/allBlogs.html', context)

# view particular post -user
@login_required(login_url='user-login')
def particularPost(request, id):
    data = blogs.objects.get(pk = id)
    context = {
        'post': data
    }
    return render(request, 'particularBlog.html', context)