import telegram
from sqlalchemy.sql import exists
from model import *
import re


class DataBase:
    user_name = ''
    user_id = 0
    user_id_invited = 0

    def __init__(self, user_name, user_id, user_id_invited):
        self.user_name = user_name
        self.user_id = user_id

        self.user_id_invited = self.get_user_id_invited(user_id_invited)

    def get_user_id_invited(self, user_id_invited):
        try:
            s = re.findall(r'[\d]+', user_id_invited)[0]
            return int(s)
        except:
            return 0

    def is_exist_user_database(self):
        user = session.query(UserInfo).filter(UserInfo.user_id == self.user_id).count()
        if user > 0:
            return True
        else:
            return False

    # ==================================================================
    def is_check_active(self):
        user = session.query(UserInfo).filter(UserInfo.user_id == self.user_id).first()
        return user.is_active

    def new_user(self):
        if self.is_exist_user_database() == False:
            user = UserInfo(self.user_name, self.user_id, 0, False)
            session.add(user)
            session.commit()

            text = 'Saved new user name {}'.format(self.user_name)
            print(text)
        else:
            print("is exsist user")

    def new_invited(self, context):

        user = session.query(UserInfo).filter(UserInfo.user_id == self.user_id_invited).first()
        inv = session.query(Invited).filter(Invited.user_info == user)

        is_exsit = False
        for i in inv:
            if i.name == self.user_name:
                is_exsit = True

        if self.user_id_invited > 0:
            if user.user_id == self.user_id:
                is_exsit = True

        if self.user_id_invited > 0 and is_exsit == False:
            invited = Invited(self.user_name, user)
            session.add(invited)
            user.nu_caller += 1

            s = user.nu_caller - user.nu_caller_m
            if s == 1:
                user.nu_caller_m = user.nu_caller
                user.is_active = True
                context.bot.send_message(chat_id=user.user_id, text="شما فعال شدید.")
                print("active")

            session.commit()
            text = 'Saved new invited for {}'.format(user.name)
            print(text)
        else:
            print("Previously registered or no start")
        # check active

    def get_list_invited(self):
        user = session.query(UserInfo).filter(UserInfo.user_id == self.user_id).first()
        invited = session.query(Invited).filter(Invited.user_info == user)
        list = ""
        for inv in invited:
            list += inv.name + "\n"
        return list

    def run(self, context):
        self.new_user()
        self.new_invited(context)
        print("======================================================")
