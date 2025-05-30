This repository contains submission for the 2nd task to create a simple backend using Flask. Instead of using Postman, a simple HTML webpage is used to show the app.

Please create a folder called templates and move the index.html file into it. Open all the files and the folder on VSCode and run the app (python app.py).
Copy paste the the Url shown in the terminal in any web browser. A simple HTML website will open showing the course contents. Add and delete operations can be done on the same page. And the result is shown in the same webpage.

Testing using Postman
to add a new resource : http://127.0.0.1:5000/add 
use POST
enter the data using the form data option in body the keys are :
week:Week 1
title:a video
type:video
url: https://www.youtube.com/watch?v=0HXg9_r_7MM

to delete an existing resource : http://127.0.0.1:5000/delete
use POST
enter the data using form data option in body. the keys are :
week:Week 1
title:a video


A screen shot of postman testing add and delete is also included in repo.
