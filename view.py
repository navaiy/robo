import telegram
from sqlalchemy.sql import exists
from model import *
import re
import time


def add_subscripi(user, session):
    now = time.localtime()  # زمان فعلی سیستم
    sec = time.mktime(now)  # تبدیل به ثانیه
    if user.time_active > sec:
        add_time = user.time_active + 60
        user.time_active = add_time
    else:
        add_time = sec + 60
        user.time_active = add_time
    session.commit()

    r = time.strptime(time.ctime(user.time_active), "%a %b %d %H:%M:%S %Y")
    r = time.strftime("%m/%d/%Y %H:%M:%S", r)
    return r


class DataBase:
    user_name = ''
    user_id = 0
    user_id_invited = 0
    session = Session()

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
        user = self.session.query(UserInfo).filter(UserInfo.user_id == self.user_id).count()
        if user > 0:
            return True
        else:
            return False

    # ==================================================================
    def is_check_active(self):
        user = self.session.query(UserInfo).filter(UserInfo.user_id == self.user_id).first()
        t = user.time_active
        self.session.close()
        time_now = time.mktime(time.localtime())
        if t > time_now:
            return True
        return False

    def new_user(self):
        if self.is_exist_user_database() == False:
            user = UserInfo(self.user_name, self.user_id, 0, False)
            self.session.add(user)
            self.session.commit()
            self.session.close()

            text = 'Saved new user name {}'.format(self.user_name)
            print(text)
        else:
            print("is exsist user")

    def new_invited(self, context):

        user = self.session.query(UserInfo).filter(UserInfo.user_id == self.user_id_invited).first()
        inv = self.session.query(Invited).filter(Invited.user_info == user)

        is_exsit = False
        for i in inv:
            if i.name == self.user_name:
                is_exsit = True

        if self.user_id_invited > 0:
            if user.user_id == self.user_id:
                is_exsit = True

        if self.user_id_invited > 0 and is_exsit == False:
            invited = Invited(self.user_name, user)
            self.session.add(invited)
            user.nu_caller += 1

            s = user.nu_caller - user.nu_caller_m
            if s == 1:
                user.nu_caller_m = user.nu_caller
                str_time = add_subscripi(user, self.session)
                user.is_active = True
                self.session.commit()

                context.bot.send_message(chat_id=user.user_id,
                                         text="شما فعال شدید تا {}".format(str_time))
                print("active")

            text = 'Saved new invited for {}'.format(user.name)
            print(text)

            self.session.close()

        else:
            print("Previously registered or no start")
        # check active

    def get_list_invited(self):
        user = self.session.query(UserInfo).filter(UserInfo.user_id == self.user_id).first()
        invited = self.session.query(Invited).filter(Invited.user_info == user)
        self.session.close()
        list = ""
        for inv in invited:
            list += inv.name + "\n"
        return list

    def run(self, context):
        self.new_user()
        self.new_invited(context)
        print("======================================================")
