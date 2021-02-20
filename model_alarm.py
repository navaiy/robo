from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()
engine = create_engine('sqlite:///database_alarm.db', connect_args={'check_same_thread': False})
Se = sessionmaker(bind=engine)
session = scoped_session(Se)


# 1-1-آلارم صف خرید نزدیک به ریختن
class BuyQueue(Base):
    __tablename__ = "buy_queue"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    new_queue = Column(Integer, default=0)
    old_queue = Column(Integer, default=0)
    link = Column(String)
    time = Column(String)
    base_vol = Column(String)

    def __init__(self, symbol, new_queue, old_queue, link, time, base_vol):
        self.symbol = symbol
        self.new_queue = new_queue
        self.old_queue = old_queue
        self.link = link
        self.time = time
        self.base_vol = base_vol

    def add(self):
        a = BuyQueue(self.symbol, self.new_queue, self.old_queue, self.link, self.time, self.base_vol)
        session.add(a)


# 0-1-آلارم صف فروش نزدیک به ریختن
class SaleQueue(Base):
    __tablename__ = "sale_queue"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    new_queue = Column(Integer, default=0)
    old_queue = Column(Integer, default=0)
    link = Column(String)
    time = Column(String)
    base_vol = Column(String)

    def __init__(self, symbol, new_queue, old_queue, link, time, base_vol):
        self.symbol = symbol
        self.new_queue = new_queue
        self.old_queue = old_queue
        self.link = link
        self.time = time
        self.base_vol = base_vol

    def add(self):
        a = SaleQueue(self.symbol, self.new_queue, self.old_queue, self.link, self.time, self.base_vol)
        session.add(a)


# 3- آلارم خرید و فروش گروهی
class GroupBuySale(Base):
    __tablename__ = "group_buy_sale"
    id = Column(Integer, primary_key=True)
    status = Column(String)  # نوع اتفاق خرید یا فروش
    symbol = Column(String)
    number_buy_or_sale = Column(Integer, default=0)  # تعداد خریدار یا فروشنده
    each_haghighi = Column(Integer, default=0)  # هر کد حقیقی
    value_buy_or_sale = Column(Integer, default=0)  # ارزش خرید یا فروش
    price_and_percentage = Column(Integer, default=0)  # قیمت معامله و درصد
    link = Column(String)
    time = Column(String)
    base_vol = Column(String)

    def __init__(self, symbol, status, number_buy_or_sale, each_haghighi,
                 value_buy_or_sale, price_and_percentage, link, time, base_vol):
        self.symbol = symbol
        self.status = status
        self.number_buy_or_sale = number_buy_or_sale
        self.each_haghighi = each_haghighi
        self.value_buy_or_sale = value_buy_or_sale
        self.price_and_percentage = price_and_percentage
        self.link = link
        self.time = time
        self.base_vol = base_vol

    def add(self):
        a = GroupBuySale(self.symbol, self.status, self.number_buy_or_sale, self.each_haghighi,
                         self.value_buy_or_sale, self.price_and_percentage, self.link, self.time, self.base_vol)
        session.add(a)


# 2- آلارم تغییر سرانه قدرت خریدار و فروشنده
class CapitaBuySale(Base):
    __tablename__ = "capita_buy_sale"
    id = Column(Integer, primary_key=True)
    status = Column(String)  # نوع اتفاق خرید یا فروش
    symbol = Column(String)
    old_buy = Column(Integer, default=0)  # سرانه خریدار قدیم
    old_sale = Column(Integer, default=0)  # سرانه فروشنده قدیم
    new_buy = Column(Integer, default=0)  # سرانه خریدار جدید
    new_sale = Column(Integer, default=0)  # سرانه فروشنده جدید
    percentage_change_buy_sale = Column(String)  # درصد تغییر سرانه خریدار به فروشنده
    percentage_change = Column(String)  # قیمت معامله و درصد
    link = Column(String)
    time = Column(String)
    base_vol = Column(String)

    def __init__(self, symbol, status, old_buy, old_sale, new_buy, new_sale,
                 percentage_change_buy_sale, percentage_change, link, time,base_vol):
        self.symbol = symbol
        self.status = status
        self.old_buy = old_buy
        self.old_sale = old_sale
        self.new_buy = new_buy
        self.new_sale = new_sale
        self.percentage_change = percentage_change
        self.percentage_change_buy_sale = percentage_change_buy_sale
        self.link = link
        self.time = time
        self.base_vol = base_vol

    def add(self):
        a = CapitaBuySale(self.symbol, self.status, self.old_buy, self.old_sale,
                          self.new_buy, self.new_sale, self.percentage_change_buy_sale, self.percentage_change,
                          self.link, self.time,self.base_vol)
        session.add(a)
        # session.commit()
        # session.close()


# 4- خرید و فروش سنگین حقوقی
class HoghoghiBuySale(Base):
    __tablename__ = "hoghoghi_buy_sale"
    id = Column(Integer, primary_key=True)
    status = Column(String)  # نوع اتفاق خرید یا فروش
    symbol = Column(String)
    value_buy_or_sale = Column(Integer, default=0)  # ارزش خرید یا فروش
    price_and_percentage = Column(String)  # قیمت معامله و درصد
    link = Column(String)
    time = Column(String)
    base_vol = Column(String)

    def __init__(self, symbol, status,
                 value_buy_or_sale, price_and_percentage, link, time, base_vol):
        self.symbol = symbol
        self.status = status
        self.value_buy_or_sale = value_buy_or_sale
        self.price_and_percentage = price_and_percentage
        self.link = link
        self.time = time
        self.base_vol = base_vol

    def add(self):
        a = HoghoghiBuySale(self.symbol, self.status, self.value_buy_or_sale
                            , self.price_and_percentage, self.link, self.time, self.base_vol)
        session.add(a)


Base.metadata.create_all(engine)

# look = Lock()
#
#
# def w():
#     semega = pandas.read_excel('id_stocks.xls')
#     while True:
#         for i in range(2):
#             s = semega['symbol'][i]
#             SaleQueue(s, 1, 2, "http://example.com/", time.strftime('%H:%M:%S')).add()
#             # BuyQueue(s, 1, 2, "http://example.com/", time.strftime('%H:%M:%S')).add()
#             # GroupBuySale(s, "خرید", 1, 2, 3, 4, "http://example.com/", time.strftime('%H:%M:%S')).add()
#             # CapitaBuySale(s, "خریدار", 1, 2, 3, 4, 5, 6, "http://example.com/", time.strftime('%H:%M:%S')).add()
#             # HoghoghiBuySale(s, "خرید", 1, 2, "http://example.com/", time.strftime('%H:%M:%S')).add()
#             # with look:
#             # print(Fore.GREEN + f"add {s} in {time.strftime('%H:%M:%S')}")
#         session.commit()
#         time.sleep(1)
#     # session.close()
#
#
# # w()
#
#
# def r():
#     i = 0
#     while True:
#         time_start = time.time()
#         last_old = session.query(SaleQueue).count()
#         time.sleep(1)
#         last_new = session.query(SaleQueue).count()
#         if last_old < last_new:
#             list = session.query(SaleQueue).all()[last_old:]
#             with look:
#                 for i in list:
#                     print(Fore.CYAN + f"{i.time} {i.symbol:>10} {i.id:>5}")
#         session.close()
#         # print(f'=========new{last_new} old{last_old} time{time.time()-time_start}')


# Thread(target=w, args=()).start()
# time.sleep(10)
# Thread(target=r, args=()).start()
# print("--- %s seconds ---" % (time.time() - start_time))
