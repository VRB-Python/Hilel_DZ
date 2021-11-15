
class Employee():
    def __init__(self, name, surname, posada, salary):
        self.name = name
        self.surname = surname
        self.posada = posada
        self.salary = salary

    def __str__(self):
        return " ".join((self.name, self.surname))


class School():
    planovi_total_costs = 10000
    planovyj_prybutok = planovi_total_costs * 0.5 # Закладаємо плановий прибуток 50%
    planova_kilkist_pupils = 5 # планова кількість учнів
    vartist_navchannja_for_pupil = (planovi_total_costs + planovyj_prybutok) / planova_kilkist_pupils #вартість навчання для одного студента 3000
    pupils_in_school = []

    def __init__(self, employees: [Employee] = None):
        self.employees = employees if employees else list()

    @staticmethod
    def static_costs_for_school():  # Сталі витрати на утримання школи (такі як оренда) за 1 місяць.
        return 5000

    def total_salary(self):
        total = 0
        for i in self.employees:
            total += i.salary
        return total

    def how_many_teachers(self):
        numb = 0
        for i in self.employees:
            if i.posada in ["teacher", "director", "zavuch"]:
                numb += 1
        return numb

    def total_costs(self):
        return self.total_salary() + self.static_costs_for_school()

    def calculate_pupils(self):  #
        """Припускаємо що в приватній школі в одному класі може вчитись 5 учнів.
        Також не можливо мати класи без класного керівника, класним керівником може бути вчитель, завуч або директор.
        Двірник, прибиральниця чи завгосп не може бути класним керівником."""
        d = {}
        for pupil in range(self.how_many_teachers()):
            d[pupil + 1] = round(self.total_costs() / ((pupil + 1) * 20), 0)
        d2 = ["Якщо кількість класів = " + str(a) + ", тоді загальна кількість учнів = " + str(
            a * 20) + ". Вартість навчання для 1 учня = " + str(d[a]) + " грн/міс" for a in d]
        return "\n".join(d2)

    def group_amount(self):
        return [Group]

    def income(self):
        return len(self.pupils_in_school) * self.vartist_navchannja_for_pupil

    def profit(self):
        return self.income() - self.total_costs()

    def __str__(self):
        spec_list = []
        for i in self.employees:
            spec_list.append(i)
        return " ".join((self.first_name, self.last_name))

class Group():
    def __init__(self, name, classmate, pupils = []):
        self.name = name
        self.classmate = classmate
        self.pupils = pupils

    def add_pupil(self, pupil):
        if str(pupil) not in School.pupils_in_school:
            School.pupils_in_school.append(str(pupil))
            return self.pupils.append(str(pupil))
        else:
            return "Цей учень вже зарахований до школи!"

    def remove_pupil(self, pupil):
        if str(pupil) in School.pupils_in_school:
            School.pupils_in_school.remove(str(pupil))
            return self.pupils.remove(str(pupil))

    def __str__(self):
        pup = " ".join(self.pupils)
        teach = self.classmate
        return str(pup)#str(self.classmate)


class Pupil():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return " ".join((self.first_name, self.last_name))