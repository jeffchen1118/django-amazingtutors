# Amazing Tutors

Amazing Tutors is a digital-powered learning platform that benefits both tutors and students by providing a flexible, engaging, resourceful, personalized, and responsive web space as a collaborative learning environment, uplifting the learner's motivation and learning experiences.

Growing from the Blog App as its foundation, Amazing Tutors implements several features to accommodate its user groups and enhance their learning experiences with this e-learning platform. A tutor, he/she can list a series of lesson materials in the use of a WYSIWYG editor (summernote) which can attach video or file links easily to create vivid and resourceful lessons for study. The implementation of a Question/Answer board namely class activities is the major plus which offers great flexibility for tutors and students to interact. Tutors can use it to list/edit tests to produce assignments,  quizzes or discussions while students can also submit discussion questions. Students can get grades and feedback quickly from tutors too, all these features form a simple yet robust collaborative learning environment.

Here's my deployed site :
[Amazing Tutors](https://amazingtutors-3f0b6cb3b188.herokuapp.com/)



![image](assets/mockuppage.jpg)


## UX 

For this e-learning platform, the tutor and students are looking for a simple, neat and intuitive layout. The Tutor can claim the lesson's ownership by creating one from the front page, and he/she can edit it anytime by the WYSIWYG editor via the 'Edit Lesson' button found in the hero image area when the lesson page is loaded.  On the lesson page, all the details of the lesson are presented in front of the tutor and students, following an 'Add Note' button for them to create or update their notes. Then 'Raise Question' button is also presented next to the 'Edit lesson' for the tutor, or only 'Raise Question' is available for the student.   


The Class Activity area following the lesson and note is where collaborations and interaction activities happen. The tutor can raise three types of questions: Type 1 is the question for a test with a due date, namely an assignment question; type2 is the question for a test without a due date namely a quiz; then type 3 is the question for discussion only, and student can raise the same type 3 discussion question. Among those questions and answers, they are all colour-coded separately based on the question or answer owner's role, and the reference of each colour is presented on the tin on the page and easily distinguishable.   

 
 ### Color Scheme



![image](assets/colorpallete.jpg)
![image](assets/colorpallete-1.jpg)



### Typography

- Caveat font was used for the site lego. The font was imported from google fonts. Serif sans is the fall back font in the case of an import error

[Google Fonts](https://fonts.google.com/?query=caveat)

- The icons  used where imported from Font Awesome 

[Font Awesome](https://fontawesome.com/icons)

- The favicon used is from the following link

[Favicon.io](https://favicon.io/favicon-generator/)


### User Stories 

### Site Users

- As a user I can register an account so that I can perform authenticated activities 
- As a user I can login to my account  so that I can see lessons 
- As a user I can logout of my account  so that I keep my account secure
- As a user I can create an lesson and post videos, file links or rich format text so that I can teach students 
- As a user I can browse lessons so that I can choose which lesson to teach or learn
- As a user I can edit and or delete my lessons so that I can manage my own content on the site
- As a user I can edit and or update my notes so that I can manage my own content on the site
- As a user I can edit and or delete my questions so that I can manage my own content on the site 
- As a user I can edit and or delete my Answers so that I can manage my own content on the site
- As a user I can edit and or update the grade and feedback for the students' assignment or quiz submission 
  so that they can get the feedback  


### Site Admin
-As site admin I can access all the lessons, questions, answers, gradefeedback, about,  so that I can manage the site effectively
 



## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used Balsamiq to design my site wireframes

[Balsamiq](https://balsamiq.com/wireframes) 
  


### Devices Wireframes

<details>

<summary>
Click here to see the Devices Wireframes
</summary>
 
![image](assets/wireframe-1.jpg) 
     -   
![image](assets/wireframe-2.jpg) 
     -
 

</details>


## Features


### Existing Features


### **Navigation Bar**

-The navigation bar is available on index and lesson_detail pages. It is fully responsive and provides links to all the areas of the website, lesson links are only presented based on whether the user is authenticated and logged in or not. Users are able to navigate on any size device with a burger menu with dropdown for small devices. users can easily click on the site logo to returnm back to the landing page.

  Desktop

  ![image](assets/navbar-1.jpg)


  Mobile

  ![image](assets/navbar-2.jpg)


### **Landing Page**
- The user can choose to create a lesson, or browse lessons (5 lessons max per page)

![image](assets/w3c/desktoptest.jpg)



### **The Footer**

- The copyright declamation and links to facebook, linkedin, instagram and youtube

  ![image](assets/footer.jpg)



### **Lesson details**

- from this simplied example 1-1, we can see the lesson author chienc currently signed in, he has put some content in lesson and his note sections.  
  ![image](assets/example-1.jpg)


Example-1-2 Then move down to class activities section, as chienc the lesson author has submitted a test question with a due date, platform will automatically identify and label its a 'assignemnt' and display the matching background color:cyclamen to make aware by other students. He answered a question from another user jeffchen. The lesson author can see everyone's answer to provide gradefeedback. Here jeffchen and julie have submitted their answers and chienc have graded and left both feedbacks.
  ![image](assets/example-2.jpg)


- chienc also submitted an discussion question, answers of such type question will always be instantly shared and available to all students, chienc can edit his own question as he is the owner, also chienc's question and answer color is distinquished from the students' color and his answer will always be promoted to the top spot because of his role as the lesson author.
  ![image](assets/example-3.jpg)   
- Below chienc's discussion question, student jeffchen raised another question, the color is light blue compared to chienc's ocean blue color.
  ![image](assets/example-4.jpg)


- Here in the same lesson, we switch over to the student jeffchen's scope from the tutor chienc's. jeffchen can only raise question as he is not the lesson author aka the tutor.  
![image](assets/jeffchenonexample-1.jpg)

- An interesting example picture, here jeffchen has answered both chienc's test assignment questions, one has been submitted but not graded, one has been graded. now jeffchen can edit the answer has not been graded yet. the other answer has been graded so he can no longer edit that answer. 
![image](assets/jeffchenonexample-2.jpg)

- In this picture, jeffchen has answered the discussion question from the tutor and he received a grade and feedback. jeffchen also raised a discussion question and he is the question owner so he can edit both the question and answer if its provided by himself. The other student will read or write a answer to the question only but can't edit them. 
  ![image](assets/jeffchenonexample-3.jpg)



### **Signup**

- Signup page allows the users to register and join the AmazingTutors site. 
- This allows the user to be able to create his/her lessons or become a student only. 
- User's get a message pop up letting them know they are signedup. 

  ![image](assets/signup.jpg)

 



### **LogIn** 

- This page allows already authenticated users to log into the site and access lessons.  
- Users get message to let then know they are login
- The logIn will then change to logout once the user is successfully loggedin.
- The user gets a prompt message if they are sure they want to log out , before getting a message they have successfully logged out if they complete the process.
- user won't be allowed to perform any activity if not login 

  ![image](assets/login.jpg)

  ![image](assets/logout.jpg)

  ![image](assets/notlogin.jpg)

### **User roles**
-User roles are generated automatically by resource - lesson. when user created a lesson, he claims the ownership of the lesson and so he is prioritized user, whereas all other users will become students. Tutors and students would have different permits inside the lesson. 
-The superuser can CRUD every data fields avaialbe via the admin panel  
  
### **Create, Edit and Delete Lesson**

- This page is a form to create a lesson, it is only accessible to authenticated logged in users. 
- Here the user's can edit lesson in rich format text by summernote editor and publish for visibility to all users or keep it as a draft showing as faded from the index and not visible to others  
- Once saved, the user get a message to show the lesson has been created successfully 

  ![image](assets/createlesson.jpg)
  ![image](assets/editdeletelesson.jpg)

- **Create Note**

- This page is a modal form to create a note which is situated below the lesson body, it is only accessible to authenticated logged in users. 
- Here the user's can edit note in rich format text by summernote editor, the note is only visible by individual and only can update after creation.   
- Once saved, the user will see it displayed immediately. 

  ![image](assets/createnote.jpg)

- **Create, Edit and Delete Question**

- This page is a form to create a question, and once question is created, the user can edit or delete it.  
- Questions and answer are edited via textarea form to avoid unwanted html tag display issues.   
- Once saved, the user will see question on the acreen immediately and a message for update successfully. 

  ![image](assets/createquestion.jpg) 
  ![image](assets/editdeletequestion.jpg)   

- **Create, Edit and Delete answer**

- This page is a form to create a answer, and once answer is created, the user can edit or delete it.  
- Questions and answer are edited via textarea form to avoid unwanted html tag display issues.   
- Once saved, the user will see answer on the acreen immediately and a message for update successfully. 
- in ansser create form, question and due date will display 

  ![image](assets/createanswer.jpg) 
 
  **Create, Update grade_feedback**

- This page is a form to create a grade_feedback, and once grade_feedback is created, the user can update it.    
- The grade and feedback will be displayed with the answer on the acreen immediately and a message for update successfully. 
- once answer is graded, the answer owner won't be able to edit answer again. 

  ![image](assets/gradefeedback.jpg) 



### Future Features

- **User Profiles**

- Users to have custom user profiles where they can list there accomplishments in completed lessons with their grades
- Users will have CRUD functionality and autonomy on their profiles
- Users to be able to add profile images for a more personal feel.

- **courses schedule board**

- Tutors and students have schedule board to follow the course timetable 
- also task board can highlight assignments' due date, events or class activities. 

- **AI agent assistant or tutor**

- deploy AI agent that trained up to share the tutor's loading on testing students or give students personalized feedbacks to improve learning experiences. 
- gamified challenges to motivate the students 



## Tools and Technologies used 


- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![Git](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![Cloudinary](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) used for online static file storage.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Balsamiq](https://img.shields.io/badge/Balsamiq-grey?logo=barmenia&logoColor=CE0908)](https://balsamiq.com/wireframes) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) currently power codepilot by chatgpt4o version, used to help debug, troubleshoot, and explain things in VScode.



## Database Design 

Here is my Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.


Site used for ERD

- [Smartdraw.com](https://app.smartdraw.com/editor.aspx?credID=-72573565&depoId=63080189&flags=128)

  ![image](assets/AmazingTutorsERD.jpg)

## Use of AI along the coding process  

### Use AI tools to assist in code creation
AI helps me with dissolving a complex idea into executable codes, I asked Codepilot to provide me options to resolve complex relationships between user roles, their able action and moves and which data to present to them. Codepilot is able to customize various filters to help with this requirement. 
-AI suggest code options for me to verify and integrate into the final product.
-There was a time when AI was struggling to see rendered html and I could provide AI further info, by looking at the correct id of a html tag for example, so AI could provide me with more accurate and effective js code to form the action I want.
-AI provides me with some very smart and neat code to iterate through an ordered queryset of the question and answer by question type or user role, which is very impressive.

### Use of AI tools to assist in debugging code
-There is a vast number of codebases I debugged with AI's help. Like say When the DTL tags were not closed correctly or simply the page not loading and a debug error was thrown out by the Django server, I would ask AI to provide me detailed options so I can walk them through and determine which is the minimum impact and traceable route to sort the bug.  I have designed my backend model well, however, there were a few times model errors that happened AI helped me to track and suggest the correct Field definition so the code would work.   

### Use AI tools to optimize code for performance and user experience
-The AI always recognize the desired patterns and makes adequate suggestion in producing ghost scripts. In this case, it helps me to use neat and tidied-up code so my performance as a developer and my user experience is boosted by coding with the AI.

### Use AI tools to create automated unit tests
-I followed course material to use Codepilot to generate a test skeleton, however AI only suggested on first test then it stucked and preventing itself to generate more ghost scripts, so I would need to test more on this part to get clear verdict. 

### Reflect on AI's role in the development process and its impact on workflow
-AI is a great companion and assistant to help a human coder in my experience through this project. AI can't be God if human feeds it junk information. I learned questions would need to be very specific and try to narrow stuff down and guide AI to slice it into smaller problems to help get good results. All in all, the more I code with the AI, the more confident I would become and can create very interesting projects down the road. 


## Agile Development Process


### GitHub Projects

[GitHub Projects](https://github.com/users/jeffchen1118/projects/8) 

- GitHub Projects is the Agile tool used for this project.


![image](assets/projectkaban.jpg)

 

### MoSCoW Prioritization approaches 

As I am the product owner, project manager and developer at the same time, I am actively prioritizing the product/project scope to justify time, resource and manpower to meet its MVP goal. The user stories and acceptance criterias were reshaped along the way on a daily basis, representing the communications between roles during the project to make a very realistic approach to meet the final MVP goal while maintaining quality, productivity and performance.



## Testing


### Feature-by-Feature Testing:

- Navigation:
Testested for smooth transitions between pages, links directing to the correct destinations.
- Responsive Design: 
Checked for compatibility across various devices and screen sizes.

- Lessons Display: 
lessons are properly showcased with accurate descriptions, images, and links.

- All Forms: 
Tested the form submission process, ensuring the user receives a confirmation.

### User Experience Testing:

- Usability Testing: 
The current implementation has meet the goal setup, all forms are functioning as expected, the logic meet design scope and user stories' requirements.  

- Accessibility Testing: 
All images and links have well labeled alt text for screen reader compatibility compliance.

### Compatibility Testing:

- Browser Compatibility: 
Testing applied on different browsers (Chrome, Firefox, Microsoft Edge,) to ensure consistent performance.

- Device Compatibility:

Functionality tested across various devices (desktops, laptops, tablets, and mobile phones).


 
## Code Validation


### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| index | index.html |![image](assets/w3c/w3cindex.jpg) | |
| lesson details | lesson_detail.html | ![image](assets/w3c/w3clessondetail.jpg) | | 
| create lesson | lesson_create.html |![image](assets/w3c/w3ccreatelesson.jpg) | |
| lesson edit | lesson_edit.html |![image](assets/w3c/w3clessonedit.jpg) | |
| create question | question_create.html |![image](assets/w3c/w3ccreatequestion.jpg) | |
| question edit | question_edit.html |![image](assets/w3c/w3ceditquestion.jpg) | |
| answer edit | answer_edit.html |![image](hassets/w3c/w3ceditanswer.jpg) | |
| gradefeedback | grade_feedback.html |![image](assets/w3c/w3cgradefeedback.jpg) | |
| about | about.html |![image](assets/w3c/w3cabout.jpg) | |

### highlights of HTML test result
   - summernote is embedded as editor in lesson_details, create lesson, edit lesson, they contains 10+ summernote related errors which is beyond scope of this project. 
   - django can generate placeholder of YY:MM:DD in DateTimeField to trigger error in html check, also beyond scope of this project 
   - in lesson, question or answer edit.html, the lesson_slug or question_id or answer_id is the attribute passed to the js code for provoke delete method, so has to keep it as it is. 

### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | Screenshot | Notes |
| --- | --- | --- | --- |
| static | custom.css |![image](assets/w3c/w3ccss.jpg) | |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files. 
A Note for CI examiner, as the 80 characters length restraint was set in old days I'll choose to leave them as they are now, as most editor can display > 80 characters correctly in modern displays so the code won't look too hideous to read.     

| APP | File | CI URL |
| --- | --- | --- |
| lesson | admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jeffchen1118/django-amazingtutors/refs/heads/main/lesson/admin.py) | 
| lesson | forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jeffchen1118/django-amazingtutors/refs/heads/main/lesson/forms.py) | 
| lesson | models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jeffchen1118/django-amazingtutors/refs/heads/main/lesson/models.py) | 
| lesson | urls.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jeffchen1118/django-amazingtutors/refs/heads/main/lesson/urls.py)  | 
| lesson | views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jeffchen1118/django-amazingtutors/refs/heads/main/lesson/views.py) | 

 

### Javascript
I have validated all my js files on [javascript validator](jshint.com) give some warnings about ES6 version syntax on them. 
![image](assets/w3c/jstest.jpg)

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser |  |  |  |  | Notes |
| --- | --- | --- | --- | --- | --- |
| Chrome |   Works as expected |
| Firefox |   Works as expected |
| Microsoft Edge|   Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

|  |  |  | Notes |
| --- | --- | --- | --- |
| Mobile (DevTools) | ![image](assets/w3c/mobiletest.jpg) | Works as expected |
| Tablet (DevTools) | ![image](assets/w3c/tablettest.jpg) | Works as expected |
| Desktop | ![image](assets/w3c/desktoptest.jpg) | Works as expected |

## Lighthouse Audit


I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| | ![image](assets/w3c/lighthousemobile.jpg) | ![image](assets/w3c/lighthousedesktop.jpg) ||

## Defensive Programming

| Page | User Action | Expected Result | Pass/Fail | Comments |
| --- | --- | --- | --- | --- |
| Home | | | | |
| | Click on Logo | Redirection to Home page | Pass | |
| | Click on Home link in navbar | Redirection to Home page | Pass | |
| | Click on create lesson card in landingpage | Redirection to create lesson form | Pass | |
| About | | | | |
| | Click on About link in navbar | Redirection to About page | Pass | |
| Lesson Details | | | | |
| | Load lesson details | All content on lesson details loaded as expected | Pass | |
| | Click on edit lesson button | Redirection to edit/delete lesson form | Pass | |
| | Click on add note button | Pop up modal for add/update note | Pass | |
| | Click on Raise Question button | Redirection to create question form | Pass | |
| | Click on Edit Question button | Redirection to edit/delete question form | Pass | |
| | Click on Write Answer button | Redirection to create answer form | Pass | | 
| | Click on Edit Answer button | Redirection to edit/delete answer form | Pass | | 
| | Click on Grade&Feedback button | Redirection to gradefeedback form | Pass | |
| Sign Up | | | | |
| | Click on Sign Up button | Redirection to Sign Up page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password (twice) | Field will only accept password format | Pass | |
| | Click on Sign Up button | Asks user to confirm email page | Pass | Email sent to user |
| | Confirm email | Redirects user to blank Sign In page | Pass | |
| Log In | | | | |
| | Click on the Login link | Redirection to Login page | Pass | |
| | Enter valid email address | Field will only accept email address format | Pass | |
| | Enter valid password | Field will only accept password format | Pass | |
| | Click Login button | Redirects user to home page | Pass | |
| Log Out | | | | |
| | Click Logout button | Redirects user to logout page | Pass | Confirms logout first |
| | Click Confirm Logout button | Redirects user to home page | Pass | |
| repeat for all remaining pages | x | x | x | x |

## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a user I can register an account so that I can perform authenticated activities. | ![image](assets/signup.jpg) |
| As a user I can login to my account so that I can see lessons
. | ![image](assets/login.jpg) |
| As a user I can logout of my account so that I keep my account secure
. | ![image](assets/logout.jpg) |
| As a user I can create an lesson and post videos, file links or rich format text so that I can teach students. | ![image](assets/createlesson.jpg) |
| As a user I can browse lessons so that I can choose which lesson to teach or learn. | ![image](assets/w3c/desktoptest.jpg) |
| As a user I can edit and or delete my lessons so that I can manage my own content on the site. | ![image](assets/editdeletelesson.jpg) |
| As a user I can edit and or update my notes so that I can manage my own content on the site
. | ![image](assets/createnote.jpg) |
| As a user I can edit and or delete my questions so that I can manage my own content on the site. | ![image](assets/editdeletequestion.jpg) |
| As a user I can edit and or delete my Answers so that I can manage my own content on the site. | ![image](assets/createanswer.jpg) |
| As a user I can edit and or update the grade and feedback for the students' assignment or quiz submission so that they can get the feedback. | ![image](assets/gradefeedback.jpg) |


## Deployment

The live deployed application can be found deployed on :

[Heroku](https://amazingtutors-3f0b6cb3b188.herokuapp.com/).

### PostgreSQL Database
The project's database is obtained and hosted via [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net/)

Then add below to the end of your env.py which would not be found in Github repository. 
os.environ["DATABASE_URL"] = (
    "Your DATABASE_URL" 
)

> [!Important]
> - PostgreSQL Databases by Code Institute are only available to CI students.
> - If you plan to clone/fork this repository, you must acquire your own database instance. 
> - PostgreSQL Databasees by Post Insittute allow maximum of 8 instances per each student.
> - Created databases are subject to delection after 18 months.   
> The DATABASE_URL value would be stored into **Config Vars** on Heroku. 

### Cloudinary API KEY

This project support the use of the [Cloudinary API](https://cloudinary.com) to store lesson images online if you would like to make a unique image to present the lesson in the lessons list.

To obtain a Cloudinary API key, create an account and log in.
- For *Primary interest*, you can choose *Programmable Media for image and video API*.
- click on setting icon to get to the contrrol dashboard, you would find your **API Keys**.
- Be sure to remove the `CLOUDINARY_URL=` as part of the API **value**; this is the **key**. 
> [!Attention] This **key** would be stored into **config Vars** on Heroku. 

Then add below to the end of your env.py which would not be found in Github repository. 
os.environ["CLOUDINARY_URL"] = (
    "Your Cloudinary API key")

- Then you can upload lesson's header images to cloudinary which would be found from assets - media library there. When up to use the image to modify a lesson header image on the AmazingTutors website, you would copy the **delivery URL** from the souce image on the Cloudinary, then you would need to signin as the admin on AmazingTutors then go to [site admin](https://amazingtutors-3f0b6cb3b188.herokuapp.com/admin/) where you can update the lesson header image by choose file, put the copied **delivery URL** to replace the placeholder image.      


### Heroku Deployment

[Heroku](https://www.heroku.com) is used to host the website, 

Deployment steps are as follows, after account setup:

- Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select **Create App**.
- From the new app **Settings**, click **Reveal Config Vars**, and set your environment variables.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

| Key | Value |
| --- | --- |
| `CLOUDINARY_URL` | user's own value |
| `DATABASE_URL` | user's own value |
| `SECRET_KEY` | user's own value |

Heroku needs three additional files in order to deploy properly.

- requirements.txt
- Procfile
- runtime.txt

You can install this project's **requirements** (where applicable) using:

- `pip3 install -r requirements.txt`

If you have your own packages that have been installed, then the requirements file needs updated using:

- `pip3 freeze --local > requirements.txt`

The **Procfile** can be created with the following command:

- `echo web: gunicorn app_name.wsgi > Procfile`
- *replace **app_name** with the name of your primary Django app name; the folder where settings.py is located*

The **runtime.txt** file needs to know which Python version you're using:
1. type: `python3 --version` in the terminal.
2. in the **runtime.txt** file, add your Python version:
	- `python-3.10.12`

[!important] 
> - When creating your heroku app environment you sould associate it with your GitHub project which can be cloned or forked from this repository before starting the app deployment to Heroku. Once the prodject has been associated and **Config Vars** settings are correct, you can click **deploy branch** to deploy it and run the website from your heroku app environment.   

### Local Deployment

This project can be cloned or forked in order to make a local copy on your own system and run tests on the local server. 

For either method, you will need to install any applicable packages found within the *requirements.txt* file.

- `pip3 install -r requirements.txt`.

You will need to create a new file called `env.py` at the root-level,
and include the same environment variables listed above from the Heroku deployment steps.

> [!IMPORTANT]  
> This is a sample only; you would replace the values with your own if cloning/forking my repository.

Sample `env.py` file:

```python
import os

os.environ("CLOUDINARY_URL", "user's own value")
os.environ("DATABASE_URL", "user's own value")
os.environ("SECRET_KEY", "user's own value")

# local environment only (do not include these in production/deployment!)
os.environ.setdefault("DEBUG", "True")
```

Once the project is cloned or forked, in order to run it locally, you'll need to follow these steps:

- Start the Django app: `python3 manage.py runserver`
- Stop the app once it's loaded: `CTRL+C` or `⌘+C` (Mac)
- Make any necessary migrations: `python3 manage.py makemigrations`
- Migrate the data to the database: `python3 manage.py migrate`
- Create a superuser: `python3 manage.py createsuperuser`
- Everything should be ready now, so run the Django app again: `python3 manage.py runserver`


## Credits

- [Code Institute: Blog project as foundation of this project] 
- [CI Blog](https://github.com/Code-Institute-Solutions/blog.git)

### Content

 - [Codepilot](https://copilot.microsoft.com/)
 - [Microsoft Designer](https://designer.microsoft.com/)

| Source | Location | Notes | 
| --- | --- | --- |
| [Shar-nm](https://github.com/shar-nm/lens-whisperer?tab=readme-ov-file) | README and Testing | a wonderful robust template to help me complete this readme.MD file |
| [Very Academy](https://www.youtube.com/watch?v=qJUgC4T5e_E) | Youtube channel | The channel offers vast of Django projects model orm videos |
| [W3Schools](https://www.w3schools.com/howto/howto_js_topnav_responsive.asp) | entire site | responsive HTML/CSS/JS navbar |
| [WhiteNoise](http://whitenoise.evans.io) | entire site | hosting static files on Heroku temporarily |
| [Bootstrap 5.3](https://getbootstrap.com/docs/5.3/getting-started/) | entire site | responsivenes and CSS |

### Media


| Source | Location | Type | Notes |
| --- | --- | --- | --- |
[Horilla](https://www.horilla.com/blogs/how-to-integrate-summernote-with-django/) | website | blog | how to integrate summernote with django in html |
 



### Acknowledgements

- I would like to thank the facilitator Amy [Amy Richardson](https://github.com/amylour) for her resourceful, caring, encouraging approach to everyone and Yari also doing well taking over Amy's left at the final project stage.
- I would like to thank John, Spencer and Roo for their patient and witty guiding session with us. 
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank myself who is always wanting to know and learn more and never give up to try pushing himself to climb over the boundary.














