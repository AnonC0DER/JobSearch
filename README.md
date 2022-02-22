# Summary
**JobSearch** is an open‑source project. <br>
Users can search and get job positions. <br>
JobSearch uses web scraping to searches and saves job positions. <br>
Job search connected to 5 websites :

<details>
<summary>5 websites list</summary>
<br>
 <a href="https://www.linkedin.com/">Linkedin</a>
 <br>
 <a href="https://www.e-estekhdam.com/">E-estekhdam</a>
 <br>
 <a href="https://yarijob.ir/">Yarijob</a>
 <br>
 <a href="https://karboom.io/">Karboom</a>
 <br>
 <a href="https://jobinja.ir/">Jobinja</a>
</details>

And it extracts data from them using web scraping and return it as a clean Json result. I used Postgresql database for this project. <br>
I created a simple front‑end using Html, Css and Javascript to allow users to search and get their results. <br>


# Setting up things
## Environment
I used two databases for JobSearch, one of them is for Django tables and the other one is for Jobs. Job results insert in second one. <br>
You can use one database if you want, if so fill both database variables like the same. <br>
Create a file named `.env` in the JobSearch directory and add all the variables there. An example of `.env` file:
```
JOBS_HOST = host1
JOBS_DATABASE = database1
JOBS_USER = user1
JOBS_PASSWORD = password1
# Django database
JS_HOST = host2
JS_DATABASE = database2
JS_USER = user2
JS_PASSWORD = password2
```


# Commands
1. `python manage.py migrate`
2. `python manage.py createsuperuser`
3. `python manage.py runserver`


# Frontend
It's just a really simple example. I created it using HTML, Css and Javascript to show you how to use APIs in Frontend. (I'm not a frontend developer, so sorry beacuse of this template) 
<br>
<br>
Demo : https://j0b-search.herokuapp.com/

## Files 
[Templates](https://github.com/AnonC0DER/JobSearch/tree/main/templates) <br>
[Css](https://github.com/AnonC0DER/JobSearch/tree/main/static/css) <br>
[Templates](https://github.com/AnonC0DER/JobSearch/tree/main/static/js) <br>
