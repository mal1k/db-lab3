class View:
    def __init__(self, table, records):
        self.table = table
        self.records = records

    @staticmethod
    def list():
        print(" 1. Owner\n", "2. Football Club\n", "3. Player\n", "4. Head Coach\n", "5. Partner\n", "6. Assistant\n", "7. Contract\n")
        number = input("\nPlease, make your number: ")
        return int(number)

    def show(self):
        if self.table == 1:
            for row in self.records:
                print("\nowner_id =", row[0])
                print("owner_name =", row[1])
                print("owner_surname =", row[2])
        elif self.table == 2:
            for row in self.records:
                print("\nfc_id =", row[0])
                print("fc_name =", row[1])
                print("fc_city =", row[2])
                print("owner_id =", row[3])
        elif self.table == 3:
            for row in self.records:
                print("\nplayer_id =", row[0])
                print("player_name =", row[1])
                print("player_surname = ", row[2])
                print("player_birthDate =", row[3])
                print("fc_id = ", row[4])
        elif self.table == 4:
            for row in self.records:
                print("\ncoach_id =", row[0])
                print("coach_name =", row[1])
                print("coach_surname =", row[2])
        elif self.table == 5:
            for row in self.records:
                print("\npartner_id =", row[0])
                print("partner_name =", row[1])
        elif self.table == 6:
            for row in self.records:
                print("\nassistant_id =", row[0])
                print("assistant_name =", row[1])
                print("assistant_surname =", row[2])
                print("head_id =", row[3])
        elif self.table == 7:
            for row in self.records:
                print("\ncontract_id =", row[0])
                print("fc_id =", row[1])
                print("partner_id =", row[2])

    @staticmethod
    def attribute_list(table):
        if table == 1:
            print(" 1. owner_id\n", "2. owner_name\n", "3. owner_surname\n")
        if table == 2:
            print(" 1. fc_id\n", "2. fc_name\n", "3. fc_city\n", "4. owner_id\n")
        if table == 3:
            print(" 1. player_id\n", "2. player_name\n", "3. player_surname\n", "4. player_birthDate\n", "5. fc_id\n")
        if table == 4:
            print(" 1. coach_id\n", "2. coach_name\n", "3. coach_surname\n")
        if table == 5:
            print(" 1. partner_id\n", "2. partner_name\n")
        if table == 6:
            print(" 1. assistant_id\n", "2. assistant_name\n", "3. assistant_surname\n", "4. head_id\n")
        if table == 7:
            print(" 1. contract_id\n", "2. fc_id\n", "3. partner_id\n")
        number = input('Number of attribute: ')
        return int(number)
