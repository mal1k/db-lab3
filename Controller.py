import Model
from View import View

class Controller:
    @staticmethod
    def menu():
        flag = 0
        while flag == 0:
            print("   MENU ")
            print("1. show one table")
            print("2. show all tables")
            print("3. insert data")
            print("4. delete data")
            print("5. update data")
            print("6. exit")
            number = int(input('\nMake your number: '))
            if number == 1 or number == 2:
                Model.show_table(number)
            elif number == 3:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.Owner.Insert()
                    elif number2 == 2:
                        Model.FootballClub.Insert()
                    elif number2 == 3:
                        Model.Player.Insert()
                    elif number2 == 4:
                        Model.HeadCoach.Insert()
                    elif number2 == 5:
                        Model.Partner.Insert()
                    elif number2 == 6:
                        Model.Assistant.Insert()
                    elif number2 == 7:
                        Model.Contract.Insert()
                except Exception:
                    print("\n... Key Error  ... Please try again ...\n")
            elif number == 4:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.Owner.Delete()
                    elif number2 == 2:
                        Model.FootballClub.Delete()
                    elif number2 == 3:
                        Model.Player.Delete()
                    elif number2 == 4:
                        Model.HeadCoach.Delete()
                    elif number2 == 5:
                        Model.Partner.Delete()
                    elif number2 == 6:
                        Model.Assistant.Delete()
                    elif number2 == 7:
                        Model.Contract.Delete()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 5:
                number2 = View.list()
                try:
                    if number2 == 1:
                        Model.Owner.Update()
                    elif number2 == 2:
                        Model.FootballClub.Update()
                    elif number2 == 3:
                        Model.Player.Update()
                    elif number2 == 4:
                        Model.HeadCoach.Update()
                    elif number2 == 5:
                        Model.Partner.Update()
                    elif number2 == 6:
                        Model.Assistant.Update()
                    elif number2 == 7:
                        Model.Contract.Update()
                except Exception:
                    print("\n... Key Error ... Please try again ...\n")
            elif number == 6:
                flag = 1
