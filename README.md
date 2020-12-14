# NOTE TAKING REST API

### To run the application (on Windows):

Clone this repository

Activate the virtual environment:

`cd notes_api`

`python -m pip install virtualenv`

`virtualenv venv -p python`

`cd venv`

`.\Scripts\activate`

Back in the `note_taking_api` directory:

`pip install django`\
`pip install djangorestframework`\
`pip install psycopg2`

Then start the server with:

 `python manage.py runserver`


### Working with the program

To see the project, navigate to `http://localhost:8000/api/note/`

Here you can use GET and POST requests on the notes API.

POST some notes then to see one note, navigate to: 

`http://localhost:8000/api/note/<ANY-NOTE-ID>`

and have the Delete, Put and Patch Options.

To stop the virtual environment: `deactivate`
