# IITB-ASSIGNMENT-2023

I. Web app development
  1. Authentication
    a) User login, logout
    b) User registration
    c) Standard password validation
    d) Forgot password validation
  2. API calls, JSON handling, Dashboard
    a) Fetch and display News image, title in home page (after logging-in)
    b) Redirect user to detailed user article on clicking news clip image
    c) User creates blog-blog title, content, date created(automatic)
    d) User delete his/her own blogs from dashboard
  3. Serializers - Django REST Framework
    a) Site-administrator can view existing blogs list in json format through api
    endpoint only
    b) Site-admin can delete, update, create blogs through api endpoints only
  4. Bootstrap designing (Optional)
    a) Usage of font-awsome based delete icon in dashboard
    b) Bootstrap form-controls for blogs creation form


  The project consist of two major apps
    |
    allApps
      |
      ---> userAccounts
      ---> blogs
      
      A -> userAccounts consist all of our logic for user authentication
      B ->  1. blog consists of all of api fetching, creating new blog post, deleting on the website 
            2. CRUD operation only admin can perform created using django-rest-framework
            |
            -> endpoint http://127.0.0.1:8000/blogs/blog_api/     
