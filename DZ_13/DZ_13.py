import requests

#Exercise 2.1
# 1

class Create_pet1:
    headers = {'accept': 'application/xml', 'Content-Type': 'application/json'}
    petstore_link = "https://petstore3.swagger.io/api/v3/pet/"

    def __init__(self, id, name, category={'id': 1, 'name': 'Dogs'}, photoUrls=['string'], status='available',
                 tags={"id": 0, "status": "string"}):
        self.category = category
        self.id = id
        self.name = name
        self.photoUrls = photoUrls
        self.status = status
        self.tags = tags

    def create_in_petstore(self):
        create_pet_req = requests.post(__class__.petstore_link, json=self.return_dict(),headers=__class__.headers)
        return create_pet_req.status_code#f"The status code is {create_pet_req.status_code}. The pet is created."

    def find_pet_in_petstore(id):
        find_pet = requests.get(f"{__class__.petstore_link}+{id}")
        return find_pet.json()['name']#f"The pet {find_pet.json()['name']} is created and found by id {id}."

    def return_dict(self):
        c = {"id": self.id, "name": self.name, "category": {'id': 1, 'name': 'Dogs'}, "photoUrls": ["string"],
             "tags": [{"id": self.id, "name": self.name}]}
        return c

#
#"Exercise 2.2
class Create_user:

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    petstore_link = "https://petstore3.swagger.io/api/v3/user/"

    def __init__(self, id = 1000, username = "Test1", firstName = "Test1", lastName = "Test1", email = "Test1", password = "Test1", phone = "Test1", userStatus = 1):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.password = password
        self.email = email
        self.phone = phone
        self.userStatus = userStatus

    def create_user_in_petstore(self):
        create_new_user = requests.post(__class__.petstore_link, json=self.return_dict(), headers=__class__.headers)
        return create_new_user.status_code

    def find_user_by_username(username):
        find_user = requests.get(__class__.petstore_link+username, headers=__class__.headers)
        return find_user.json()

    def update_existing_user(username, test_dict):
        update_user = requests.put(__class__.petstore_link + username, json= test_dict,  headers=__class__.headers)
        return update_user

    def return_dict(self):
        c1 = {"id": self.id, "username": self.username, "firstName": self.firstName, "lastName": self.lastName,
              "email": self.email, "password": self.password, "phone": self.phone, "userStatus": self.userStatus}
        return c1

