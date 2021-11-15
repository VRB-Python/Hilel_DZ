import pytest
from School_code.DZ_12_School import Pupil, Employee, School, Group


pupils_for_test = [["One", "Pupil1"], ["Two", "Pupil2"], ["Three", "Pupil3"], ["Four", "Pupil4"], ["Five", "Pupil5"], ["Six", "Pupil6"]]
profit_add_pupil = [["1", "Profit1"], ["2", "Profit2"], ["3", "Profit3"]]
delete_pupil = [["Andr", "Buk"], ["Roksolana", "Silent"]]

@pytest.fixture(scope="session")
def test_creating_school():
    ivo = Employee("Ivo1", "Bobul", "director", 3000)
    nati = Employee("Nata", "Gnat", "teacher", 2000)
    school1 = School([ivo, nati])
    group1 = Group("1 - E", nati)
    andr = Pupil("Andr", "Buk")
    roskana = Pupil("Roksolana", "Silent")
    group1.add_pupil(andr)
    group1.add_pupil(roskana)
    return school1, group1

@pytest.fixture(params=pupils_for_test)
def a_task(request):
    return request.param

def test_add_pupil(test_creating_school, a_task):
    one_test = Pupil(a_task[0], a_task[1])
    test_creating_school[1].add_pupil(one_test)
    exp_res = test_creating_school[0].pupils_in_school[-1] #запит до класу School, щоб перевірити чи користувач там додався.
    assert str(one_test) == exp_res

@pytest.fixture(params=profit_add_pupil)
def b_task(request):
    return request.param

def test_profit_after_adding(test_creating_school, b_task):
    exp_result = test_creating_school[0].profit() + 3000 #Expected result: прибуток до додавання учня + 3000 (вартість навчання для одного учня)
    one_test = Pupil(b_task[0], b_task[1])
    test_creating_school[1].add_pupil(one_test)
    act_result = test_creating_school[0].profit() #Actual result: прибуток після додавання учня.
    assert act_result == exp_result

@pytest.fixture(params=delete_pupil)
def c_task(request):
    return request.param

def test_remove_pupil(test_creating_school, c_task):
    pupil_for_deleting = " ".join(c_task)
    exp_res1 = len(test_creating_school[0].pupils_in_school) - 1
    test_creating_school[1].remove_pupil(pupil_for_deleting)
    act_res = test_creating_school[0].pupils_in_school
    assert len(act_res) == exp_res1 and pupil_for_deleting not in test_creating_school[0].pupils_in_school #Перевіряю чи кількість учнів зменшилась на 1 і чи конкретного учня не має у загальному списку учнів


def test_profit_after_removing(test_creating_school, b_task):
    pupil_for_deleting = " ".join(b_task)
    exp_result = test_creating_school[0].profit() - 3000  # Expected result: прибуток до видалення учня - 3000 (вартість навчання для одного учня)
    test_creating_school[1].remove_pupil(pupil_for_deleting)
    act_result = test_creating_school[0].profit()  # Actual result: прибуток після додавання учня.
    assert act_result == exp_result

@pytest.mark.exist_pupil
def test_add_existing_pupil(test_creating_school, c_task):
    exist_pupil = Pupil(c_task[0], c_task[1]) #Пробую додати знову учнів зі списку delete_pupil = [["Andr", "Buk"], ["Roksolana", "Silent"]]
    act_res = test_creating_school[1].add_pupil(exist_pupil)
    exp_res = "Цей учень вже зарахований до школи!" #test_creating_school[0].pupils_in_school[-1]  # запит до класу School, щоб перевірити чи користувач там додався.
    assert act_res == exp_res