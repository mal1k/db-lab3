from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from View import View

DATABASE = {
    'drivername': 'postgres',
    'host': 'localhost',
    'port': '5432',
    'username': 'postgres',
    'password': 'qwerty123',
    'database': 'Football Club'
}

db = declarative_base()

class Owner(db):
    __tablename__ = 'Owner'

    owner_id = Column(Integer, primary_key = True, nullable = False)
    owner_name = Column(String, nullable = False)
    owner_surname = Column(String, nullable = False)

    def __init__(self, id, name, surname):
        self.owner_id = id
        self.owner_name = name
        self.owner_surname = surname

    @staticmethod
    def Insert():
        new_owner_id = input('owner_id = ')
        new_owner_name = input('owner_name = ')
        new_owner_surname = input('owner_surname = ')
        new_owner = Owner(new_owner_id, new_owner_name, new_owner_surname)
        session.add(new_owner)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('owner_id delete = ')
        session.delete(session.query(Owner).filter(Owner.owner_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(1)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Owner).filter(Owner.owner_id == value).update({Owner.owner_id: value2})
        elif num == 2:
            session.query(Owner).filter(Owner.owner_name == value).update({Owner.owner_name: value2})
        elif num == 3:
            session.query(Owner).filter(Owner.owner_surname == value).update({Owner.owner_surname: value2})
        session.commit()

    def print(self):
        return "<Owner('%s', '%s', '%s')>" % (self.owner_id, self.owner_name, self.owner_surname)


class FootballClub(db):
    __tablename__ = 'FootballClub'

    fc_id = Column(Integer, primary_key = True, nullable = False)
    fc_name = Column(String, nullable = False)
    fc_city = Column(String, nullable = False)
    owner_id = Column(Integer, ForeignKey(Owner.owner_id), nullable = False)

    def __init__(self, id, name, city, owner):
        self.fc_id = id
        self.fc_name = name
        self.fc_city = city
        self.owner_id = owner

    @staticmethod
    def Insert():
        new_fc_id = input('fc_id = ')
        new_fc_name = input('fc_name = ')
        new_fc_city = input('fc_city = ')
        new_owner_id = input('owner_id = ')
        new_fc = FootballClub(new_fc_id, new_fc_name, new_fc_city, new_owner_id)
        session.add(new_fc)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('fc_id delete = ')
        session.delete(session.query(FootballClub).filter(FootballClub.fc_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(2)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(FootballClub).filter(FootballClub.fc_id == value).update(
                {FootballClub.fc_id: value2})
        elif num == 2:
            session.query(FootballClub).filter(FootballClub.fc_name == value).update(
                {FootballClub.fc_name: value2})
        elif num == 3:
            session.query(FootballClub).filter(FootballClub.fc_city == value).update(
                {FootballClub.fc_city: value2})
        elif num == 4:
            session.query(FootballClub).filter(FootballClub.owner_id == value).update(
                {FootballClub.owner_id: value2})
        session.commit()

    def print(self):
        return "<FootballClub('%s', '%s', '%s', '%s')>" % (self.fc_id, self.fc_name, self.fc_city, self.owner_id)

class Player(db):
    __tablename__ = 'Player'

    player_id = Column(Integer, primary_key = True, nullable = False)
    player_name = Column(String, nullable = False)
    player_surname = Column(String, nullable=False)
    player_birthDate = Column(DateTime, nullable=False)
    fc_id = Column(Integer, ForeignKey(FootballClub.fc_id), nullable = False)

    def __init__(self, id, name, surname, birthDate, fc):
        self.player_id = id
        self.player_name = name
        self.player_surname = surname
        self.player_birthDate = birthDate
        self.fc_id = fc

    @staticmethod
    def Insert():
        new_player_id = input('player_id = ')
        new_player_name = input('player_name = ')
        new_player_surname = input('player_surname = ')
        new_player_birthDate = input('player_birthDate = ')
        new_fc_id = input('fc_id = ')
        new_player = Player(new_player_id, new_player_name, new_player_surname, new_player_birthDate, new_fc_id)
        session.add(new_player)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('player_id delete = ')
        session.delete(session.query(Player).filter(Player.player_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(3)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Player).filter(Player.player_id == value).update({Player.player_id: value2})
        elif num == 2:
            session.query(Player).filter(Player.player_name == value).update({Player.player_name: value2})
        elif num == 3:
            session.query(Player).filter(Player.player_surname == value).update({Player.player_surname: value2})
        elif num == 4:
            session.query(Player).filter(Player.player_birthDate == value).update({Player.player_birthDate: value2})
        elif num == 5:
            session.query(Player).filter(Player.fc_id == value).update({Player.fc_id: value2})
        session.commit()

    def print(self):
        return "<Player('%s', '%s', '%s', '%s', '%s')>" % (self.player_id, self.player_name, self.player_surname, self.player_birthDate, self.fc_id)

class HeadCoach(db):
    __tablename__ = 'HeadCoach'

    coach_id = Column(Integer, ForeignKey(FootballClub.fc_id), primary_key = True, nullable = False)
    coach_name = Column(String, nullable = False)
    coach_surname = Column(String, nullable = False)

    def __init__(self, id, name, surname):
        self.coach_id = id
        self.coach_name = name
        self.coach_surname = surname

    @staticmethod
    def Insert():
        new_coach_id = input('coach_id = ')
        new_coach_name = input('coach_name = ')
        new_coach_surname = input('coach_surname = ')
        new_coach = HeadCoach(new_coach_id, new_coach_name, new_coach_surname)
        session.add(new_coach)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('coach_id delete = ')
        session.delete(session.query(HeadCoach).filter(HeadCoach.coach_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(4)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(HeadCoach).filter(HeadCoach.coach_id == value).update({HeadCoach.coach_id: value2})
        elif num == 2:
            session.query(HeadCoach).filter(HeadCoach.coach_name == value).update({HeadCoach.coach_name: value2})
        elif num == 3:
            session.query(HeadCoach).filter(HeadCoach.coach_surname == value).update({HeadCoach.coach_surname: value2})

    def print(self):
        return "<HeadCoach('%s', '%s', '%s')>" % (self.coach_id, self.coach_name, self.coach_surname)

class Partner(db):
    __tablename__ = 'Partner'

    partner_id = Column(Integer, primary_key = True, nullable = False)
    partner_name = Column(String, nullable = False)

    def __init__(self, id, name):
        self.partner_id = id
        self.partner_name = name

    @staticmethod
    def Insert():
        new_partner_id = input('partner_id = ')
        new_partner_name = input('partner_name = ')
        new_partner = Partner(new_partner_id, new_partner_name)
        session.add(new_partner)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('partner_id delete = ')
        session.delete(
            session.query(Partner).filter(Partner.partner_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(5)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Partner).filter(Partner.partner_id == value).update({Partner.partner_id: value2})
        elif num == 2:
            session.query(Partner).filter(Partner.partner_name == value).update({Partner.partner_name: value2})
        session.commit()

    def print(self):
        return "<Partner('%s', '%s')>" % (self.partner_id, self.partner_name)

class Assistant(db):
    __tablename__ = 'Assistant'

    assistant_id = Column(Integer, primary_key=True, nullable=False)
    assistant_name = Column(String, nullable=False)
    assistant_surname = Column(String, nullable=False)
    head_id = Column(Integer, ForeignKey(HeadCoach.coach_id), nullable=False)

    def __init__(self, id, name, surname, head):
        self.assistant_id = id
        self.assistant_name = name
        self.assistant_surname = surname
        self.head_id = head

    @staticmethod
    def Insert():
        new_assistant_id = input('assistant_id = ')
        new_assistant_name = input('assistant_name = ')
        new_assistant_surname = input('assistant_surname = ')
        new_head_id = input('head_id = ')
        new_assistant = Assistant(new_assistant_id, new_assistant_name, new_assistant_surname, new_head_id)
        session.add(new_assistant)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('assistant_id delete = ')
        session.delete(session.query(Assistant).filter(Assistant.assistant_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(6)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Assistant).filter(Assistant.assistant_id == value).update({Assistant.assistant_id: value2})
        elif num == 2:
            session.query(Assistant).filter(Assistant.assistant_name == value).update(
                {Assistant.assistant_name: value2})
        elif num == 3:
            session.query(Assistant).filter(Assistant.assistant_surname == value).update(
                {Assistant.assistant_surname: value2})
        elif num == 4:
            session.query(Assistant).filter(Assistant.head_id == value).update(
                {Assistant.head_id: value2})
        session.commit()

    def print(self):
        return "<Assistant('%s', '%s', '%s', '%s')>" % (self.assistant_id, self.assistant_name, self.assistant_surname, self.head_id)

class Contract(db):
    __tablename__ = 'Contract'

    contract_id = Column(Integer, primary_key=True, nullable=False)
    fc_id = Column(Integer, ForeignKey(FootballClub.fc_id), nullable=False)
    partner_id = Column(Integer, ForeignKey(Partner.partner_id), nullable=False)

    def __init__(self, id, fc, partner):
        self.contract_id = id
        self.fc_id = fc
        self.partner_id = partner

    @staticmethod
    def Insert():
        new_contract_id = input('contract_id = ')
        new_fc_id = input('fc_id = ')
        new_partner_id = input('partner_id = ')
        new_contract = Contract(new_contract_id, new_fc_id, new_partner_id)
        session.add(new_contract)
        session.commit()

    @staticmethod
    def Delete():
        delete_id = input('contract_id delete = ')
        session.delete(session.query(Contract).filter(Contract.contract_id == delete_id).first())
        session.commit()

    @staticmethod
    def Update():
        num = View.attribute_list(7)
        value = input('Attribute value to update = ')
        value2 = input('New attribute value = ')
        if num == 1:
            session.query(Contract).filter(Contract.contract_id == value).update(
                {Contract.contract_id: value2})
        elif num == 2:
            session.query(Contract).filter(Contract.fc_id == value).update(
                {Contract.fc_id: value2})
        elif num == 3:
            session.query(Contract).filter(Contract.partner_id == value).update(
                {Contract.partner_id: value2})
        session.commit()

    def print(self):
        return "<Contract('%s', '%s', '%s')>" % (self.contract_id, self.fc_id, self.partner_id)

engine = create_engine(URL(**DATABASE))
db.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def show_table(number):
    flag = 0
    table = 0
    while flag == 0:
        if number == 1:
            table = View.list()
            flag = 1
        elif number == 2:
            table += 1
            if table == 7:
                flag = 1
        if table == 1:
            print("table: Owner")
            for row in session.query(Owner):
                print(row.print())
            print("\n")
        elif table == 2:
            print("table: Football Club")
            for row in session.query(FootballClub):
                print(row.print())
            print("\n")
        elif table == 3:
            print("table: Player")
            for row in session.query(Player):
                print(row.print())
            print("\n")
        elif table == 4:
            print("table: Head Coach")
            for row in session.query(HeadCoach):
                print(row.print())
            print("\n")
        elif table == 5:
            print("table: Partner")
            for row in session.query(Partner):
                print(row.print())
            print("\n")
        elif table == 6:
            print("table: Assistant")
            for row in session.query(Assistant):
                print(row.print())
            print("\n")
        elif table == 7:
            print("table: Contract")
            for row in session.query(Contract):
                print(row.print())
            print("\n")