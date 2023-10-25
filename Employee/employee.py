from DAO import query_base_employee as q
from DAO import database as db

USER_CHOICE = """
Enter:
- '1' View my detail
- '2' Update my detail
- '3' Apply for leaves
- '4' View my leave status
- '5' View my salary status
- 'q' quit

Your choice:- """

class Employee:

    def __init__(self,userid):
        self.userid = userid
        print(f"\nWelcome {self.userid}")

    def menu_employee(self):
        user_input = input(USER_CHOICE)
        while user_input != 'q':
            match user_input:
                case '1':
                    db.display_employee_data(q.QUERY_TO_DISPLAY_LOGGEDIN_EMPLOYEE_DETAILS,self.userid,q.LIST_TO_DISPLAY_EMPLOYEE_DETAILS)
                case '2':
                    self.update_details()
                case '3':
                    self.apply_leaves()
                case '4':
                    db.display_employee_data(q.QUERY_TO_DISPLAY_SELF_LEAVES_STATUS,self.userid,q.LIST_TO_DISPLAY_LEAVES_DETAILS)
                case '5':
                   db.display_employee_data(q.QUERY_TO_DISPLAY_SALARY_STATUS,self.userid,q.LIST_TO_DISPLAY_SALARY_DETAILS)
                case _:
                    print("Wrong input entered!! Please try again")
            user_input = input(USER_CHOICE)

    def apply_leaves(self):
        leave_data = input("Enter date in dd\mm\YYYY format: -")
        db.add_data(q.QUERY_TO_ADD_IN_LEAVE_TABLE,(leave_data,self.userid))

    def update_details(self):
        self.update_input = input("- '1' to update email\n- '2' to update age\n- '3' to update phone number\n- '4' to update gender")
        match self.update_input:
            case '1':
                email_to_update = input("Enter the new mail:- ")
                db.update_data(q.QUERY_TO_UPDATE_EMP_MAIL,(email_to_update,self.userid,))
            case '2':
                age_to_update = input("Enter the new age:- ")
                db.update_data(q.QUERY_TO_UPDATE_EMP_AGE,(age_to_update,self.userid,))
            case '3':
                phone_to_update = input("Enter the new phone number:- ")
                db.update_data(q.QUERY_TO_UPDATE_EMP_PHONE,(phone_to_update,self.userid,))
            case '4':
                gender_to_update = input("Enter the new gender:- ")
                db.update_data(q.QUERY_TO_UPDATE_EMP_GENDER,(gender_to_update,self.userid,))
            case _:
                print("Wrong input entered!!")
