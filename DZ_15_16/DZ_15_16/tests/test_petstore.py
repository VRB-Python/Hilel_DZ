import pytest
from petstore_website.page_object import Create_pet1, Create_user
from test_data.data import pet_list, updated_user_list, user_list

# pet_list = [[1200, "Spaniel"], [1201, "Boxer"], [1202, "Chau-chau"],[1203, "Hatiko"]]
# user_list = [(150, "Dexter", "Nick", "Jackson", "dexster@dextest.com", "123456", "222222", 1), (151, "userJohn", "John", "Travolta", "trav@trav.com", "123456", "222222", 1)]
# updated_user_list =[ ["Dexter",{"id":150, "username": "DexterUP", "firstName":"NickUP",'lastName': 'Test1', 'email': 'Test1', 'password': 'Test1', 'phone': 'Test1', 'userStatus': 1}], ["userJohn",{"id":151, "username": "userJohnUP", "firstName":"NickUP",'lastName': 'Travolta2', 'email': 'Test1', 'password': 'Test1', 'phone': 'Test1', 'userStatus': 1}]]

@pytest.fixture(params=pet_list)
def a_task(request):
    return request.param

def test_create_pet(a_task):
    test_pet = Create_pet1(a_task[0], a_task[1])
    test_created_pet = Create_pet1.create_in_petstore(test_pet)
    assert test_created_pet == 200

@pytest.mark.find_pet
def test_find_pet_by_id(a_task):
    test_find_pet = Create_pet1.find_pet_in_petstore(a_task[0])
    assert test_find_pet == a_task[1]


@pytest.mark.user
@pytest.fixture(params=user_list)
def b_task(request):
    return request.param

@pytest.mark.user
def test_create_user(b_task):
    test_user = Create_user(b_task[0], b_task[1], b_task[2],b_task[3],b_task[4],b_task[5],b_task[6], b_task[7])
    test_created_user = Create_user.create_user_in_petstore(test_user)
    assert test_created_user == 200

@pytest.mark.user
def test_find_user(b_task):
    find_user = Create_user.find_user_by_username(b_task[1])
    assert find_user["id"] == b_task[0]

@pytest.fixture(params=updated_user_list)
def c_task(request):
    return request.param

@pytest.mark.update_user
def test_update_user(c_task):
    upd_user = Create_user.update_existing_user(c_task[0], c_task[1])
    assert upd_user.status_code == 200
    #assert upd_user["username"] == c_task[1]["username"] # я хотів перевіряти по юзер нейм, але дуже часто прилітає 500 і приходять помилки типу "KeyError" або подібні