# Hackccelerate

An Online education platfrom for schools 
Live at https://learn-live.herokuapp.com/

## Test User Credentials

Login -> http://learn-live.herokuapp.com/accounts/login/

### Student Login
Username : student01
Password : common101

### Teacher Login
Username : teacher01
Password : common101

### Parent Login
Username : parent01
Password : common101

### Django SuperUser
login -> http://learn-live.herokuapp.com/admin
Username : ayush
Password : a

## Installation
```bat
git clone 
cd 
pip install -r 'requirements.txt'
python manage.py makemigrations
python manage.py migrate

```

- Cache db settings
- memached for cache
In settings.py change the "CHANNEL_LAYERS" configuration to your local redis server

```bat
python manage.py runserver
```

Note 01: Once user register on portal, admin should login <here>[https://learn-live.herokuapp.com/admin/accounts/user/] and approve the account of that user. Only approved users can view our course content and participate in discussion forum.

Note 02: All the Test Credentials are approved Users. So you can use them freely!

## Features 

### Students

Note : Once user register's his accounts ,admin needs to approve the account

- login and register
- enroll courses available
- see all courses 
- navigation to course where they can see different modules,
announcments regarding the course and contents of modules also 
chat with other studets in course chat room
- see the dicussion/posts posted by teachers/students



### Teachers
- login and register
- create a course
- edit /moules
- reorder them on course page
- post course content in text/video/file
- create/view public uploads 


### Parentts
-  login and register
- See announcements regarding their children's courses
- Events 
- Holiays
- see report cards of each child(Attendance is manual,so is the grade )
- create/view public uploads 




## Gallery



### home page
<img src="ss/rename.png">
<img src="ss/main_down.png">

### signin
<img src="ss/signup.png">

### approval
<img src="ss/approve.png">

### student
<img src="ss/student_courses.png">
<img src="ss/chat.png">
<img src="ss/all_courses.png">
<img src="ss/discussion.png">


### teacher
<img src="ss/teacher-courses.png">
<img src="ss/add_content.png">
<img src="ss/teacher-courses-manage.png">
<img src="ss/teacher-module-manage.png">
<img src="ss/teacher-edit-course.png">
<img src="ss/teacher-new-announcement.png">










