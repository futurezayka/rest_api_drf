##### git clone https://github.com/futurezayka/rest_api_drf.git
##### cd rest_api_drf
##### pip install requirements.txt
##### python manage.py makemigrations
##### python manage.py migrate
##### python manage.py runserver


# **Endpoints**

### **Teams**

* **(GET) /api/teams/** Get a list of all teams.
* **(GET) /api/teams/{team_id}/** Get information about a specific team.
* **(POST) /api/teams/** Creating a new team.
* **(PUT/PATCH) /api/teams/{team_id}/** Update team info.
* **(DELETE) /api/teams/{team_id}/** Delete a team.

### **Persons**

* **(GET) /api/persons/** Get a list of all people.
* **(GET) /api/persons/{person_id}/** Getting information about a specific person.
* **POST) /api/persons/** Creating a new person.
* **(PUT/PATCH) /api/persons/{person_id}/** Update person information.
* **(DELETE) /api/persons/{person_id}/** Delete a person.

### **Team Actions**

* **(POST) /api/teams/{team_id}/add_people_to_team/** Adding people to a team.
* **(DELETE) /api/teams/{team_id}/remove_people_from_team/** Remove people from team

### **JSON STRUCTURE**
#### Teams
* Required: `{"name": "Team name"}`
#### Persons
* Required: `{"name": "name", "surname": "name", "email": "email@mail.ua"}`
* Additional: `{"team": 1}`
#### Team Actions
* Required: `{"people_ids": [1, 2, 3]}` - list of people ids or empty list for **!!REMOVE!!** all people from team. Empty list for **!!ADD!!** will be ignored
