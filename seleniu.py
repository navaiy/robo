import time
from threading import Thread

from colorama import Fore
from selenium import webdriver

from model_alarm import BuyQueue, SaleQueue, HoghoghiBuySale, CapitaBuySale, GroupBuySale, session


class AlarmBorce:
    script2 = ''
    script1 = ''

    def __init__(self):
        self.driver1 = webdriver.Firefox()
        self.driver2 = webdriver.Firefox()
        self._config(self.driver1, 1)
        self._config(self.driver2, 2)

    def _config(self, driver, n):
        market_watch_url = 'http://cdn2.tsetmc.com/Loader.aspx?ParTree=15131F#'
        driver.get(market_watch_url)
        # choose make filter
        driver.find_element_by_xpath('//*[@id="SettingsDesc"]/div[1]/a[7]').click()
        # click new filter
        driver.find_element_by_xpath('//*[@id="FilterIndex"]/div[1]').click()
        # click filter 0
        driver.find_element_by_xpath('//*[@id="FilterIndex"]/div[1]').click()
        # write filter
        if n == 1:
            filter1 = """
               (cfield0)=(ct).Sell_CountI;
               (cfield1)=(ct).Buy_I_Volume;
               (cfield2)=(ct).Buy_CountI;
               """
        else:
            filter1 = """
               (cfield0)=(ct).Sell_I_Volume;
               (cfield1)=(ct).Sell_N_Volume;
               (cfield2)=(ct).Buy_N_Volume;
               """
        driver.find_element_by_xpath('//*[@id="InputFilterCode"]').send_keys(filter1)
        # rename filter
        elm = driver.find_element_by_xpath('//*[@id="InputFilterName"]')
        elm.clear()
        elm.send_keys('myFilter')

        # submit filter
        driver.find_element_by_xpath('//*[@id="FilterContent"]/div[1]').click()

        # close filter box
        time.sleep(0.1)
        driver.find_element_by_css_selector('#ModalWindowOuter1 > div.popup_close').click()

        ##  Display format ##
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/a[5]').click()
        time.sleep(1)
        # make format

        driver.find_element_by_css_selector("div.SlideItem:nth-child(13)").click()
        time.sleep(1)
        # title
        driver.find_element_by_xpath('//*[@id="Col0_Title"]').send_keys('خرید فروش حقوقی')
        driver.find_element_by_xpath('//*[@id="Col1_Title"]').send_keys('خرید حقیقی')
        driver.find_element_by_xpath('//*[@id="Col2_Title"]').send_keys('تعداد خرید حقیقی')
        # Data
        driver.find_element_by_xpath('//*[@id="Col0_Data"]').find_element_by_css_selector(
            '#Col0_Data > option:nth-child(25)').click()
        driver.find_element_by_xpath('//*[@id="Col1_Data"]').find_element_by_css_selector(
            '#Col1_Data > option:nth-child(26)').click()
        driver.find_element_by_xpath('//*[@id="Col2_Data"]').find_element_by_css_selector(
            '#Col2_Data > option:nth-child(27)').click()
        # save format
        driver.find_element_by_css_selector('.awesome').click()
        # change display
        driver.find_element_by_xpath('/html/body/div[6]/div[1]/a[5]').click()
        time.sleep(1)
        driver.find_element_by_css_selector('div.SlideItem:nth-child(5)').click()
        print('ok')

        ##  FILTER SETTING ##
        def setup(css_selector):
            driver.find_element_by_id('id1').click()
            time.sleep(0.1)
            driver.find_element_by_css_selector(css_selector).click()

        # farabours
        setup('div.awesome:nth-child(33)')
        # no industry group by
        setup('div.awesome:nth-child(17)')
        # no realstate right - tashilat maskan
        setup('div.awesome:nth-child(34)')
        # no bonds
        setup('div.awesome:nth-child(36)')
        # no options
        setup('div.awesome:nth-child(37)')
        # no Futures
        setup('div.awesome:nth-child(38)')
        # no kala
        setup('div.awesome:nth-child(40)')
        # no Futures
        setup('div.awesome:nth-child(44)')
        # simple show
        setup('div.awesome:nth-child(27)')

        # choose asasi metals
        # setup('#SectorList > option:nth-child(18)')

        try:
            driver.find_element_by_css_selector('.popup_close').click()
        except Exception as e:
            pass

        print("market watch ready!")
        time.sleep(1)
        if n == 1:
            # yesterdayPrice: columns[5].innerHTML,
            # closePrice: columns[10].innerHTML,
            # closePercent: columns[12].innerText,
            # nm_qu_buy: columns[17].innerHTML,
            # hajm: columns[3].children[0].innerHTML,
            # price_qu_buy: columns[19].innerText,
            # nm_qu_sell: columns[22].innerText,
            # price_qu_sell: columns[20].innerText,

            self.script1 = """
                   function readFilter() {
                       let result = document.getElementById('main').children;
                       let data = {};
                       for (let i=0; i < result.length; i++){
                           let row = result[i];
                           let columns = row.children;
                           let tseId = columns[0].children[0].target;
                           data[tseId] = {
                               symbol: columns[0].innerText,
                               link: columns[0].children[0].href,
                               base_vol: columns[3].children[0].title,
                               lastPrice: columns[7].innerHTML,
                               lastPercent: columns[9].innerText,
                               vol_qu_buy: columns[18].innerText,
                               vol_qu_sell: columns[21].innerText,
                               haghighiSellNum: columns[23].innerText,
                               haghighiBuy: columns[24].innerText,
                               haghighiBuyNum: columns[25].innerText

                           };
                       }
                       return data
                   }
                   return readFilter()
                   """
        else:
            self.script2 = """
               function readFilter() {
                   let result = document.getElementById('main').children;
                   let data = {};
                   for (let i=0; i < result.length; i++){
                       let row = result[i];
                       let columns = row.children;
                       let tseId = columns[0].children[0].target;
                       data[tseId] = {
                           haghighiSellVol: columns[23].innerText,
                           hoghoghiSellVol: columns[24].innerText,
                           hoghighiBuyVol: columns[25].innerText,

                       };
                   }
                   return data
               }
               return readFilter()
               """

    # 1-1-آلارم صف خرید نزدیک به ریختن
    def _buy_queue(self, new_symbols, old_symbols):
        for symbol in new_symbols:
            a = int(new_symbols[symbol]['vol_qu_buy'].replace(',', ''))  # حجم اولین صف فروش
            a1 = int(old_symbols[symbol]['vol_qu_buy'].replace(',', ''))  # حجم اولین صف فروش بعد ده ثانیه
            a3 = abs(a - a1)  # اختلاف حجم صف فروش در ده ثانیه

            m = new_symbols[symbol]['base_vol']
            m = int(m.split(':')[2].replace(',', ''))  # حجم مبنا

            data = new_symbols[symbol]['symbol']
            link = new_symbols[symbol]['link']

            if a3 > m * 2 / 100:
                BuyQueue(data, a1, a, "link", time.strftime("%H:%M:%S")).add()
                print(
                    Fore.GREEN + f' {str(a1) + " صف جدید"}{str(a) + " صف قدیم" : >20} {"[" + data + "]":>10}')

    # 0-1-آلارم صف فروش نزدیک به ریختن
    def _sale_queue(self, new_symbols, old_symbols):
        for symbol in new_symbols:
            a = int(new_symbols[symbol]['vol_qu_sell'].replace(',', ''))  # حجم اولین صف فروش
            a1 = int(old_symbols[symbol]['vol_qu_sell'].replace(',', ''))  # حجم اولین صف فروش بعد ده ثانیه
            a3 = abs(a - a1)  # اختلاف حجم صف فروش در ده ثانیه

            m = new_symbols[symbol]['base_vol']
            m = int(m.split(':')[2].replace(',', ''))  # حجم مبنا

            data = new_symbols[symbol]['symbol']
            link = new_symbols[symbol]['link']

            if a3 > m * 2 / 100:
                print(
                    Fore.RED + f' {str(a1) + " صف جدید"}{str(a) + " صف قدیم" : >20} {"[" + data + "]":>10}')

    # 3- آلارم خرید و فروش گروهی
    def _group_buy_sale(self, new_symbols, old_symbols):
        for symbol in new_symbols:
            bu1 = int(new_symbols[symbol]['haghighiBuy'].replace(',', ''))  # حجم خرید حقیقی
            se1 = int(new_symbols[symbol]['haghighiSellVol'].replace(',', ''))  # حجم فروش حقیقی

            nbu1 = int(new_symbols[symbol]['haghighiBuyNum'].replace(',', ''))  # تعداد معاملات خرید حقیقی
            nse1 = int(new_symbols[symbol]['haghighiSellNum'].replace(',', ''))  # تعداد معلاملات فروش حقیقی
            # بعد ده ثانیه
            bu2 = int(old_symbols[symbol]['haghighiBuy'].replace(',', ''))  # حجم خرید حقیقی
            se2 = int(old_symbols[symbol]['haghighiSellVol'].replace(',', ''))  # حجم فروش حقیقی

            nbu2 = int(old_symbols[symbol]['haghighiBuyNum'].replace(',', ''))  # تعداد معاملات خرید حقیقی
            nse2 = int(old_symbols[symbol]['haghighiSellNum'].replace(',', ''))  # تعداد معلاملات فروش حقیقی

            bu3 = abs(bu1 - bu2)
            se3 = abs(se1 - se2)

            nbu3 = abs(nbu1 - nbu2)
            nse3 = abs(nse1 - nse2)

            m = new_symbols[symbol]['base_vol']
            m = int(m.split(':')[2].replace(',', ''))  # حجم مبنا
            lastPrice = new_symbols[symbol]['lastPrice']  # قیمت اخرین معامله
            lastPercent = new_symbols[symbol]['lastPercent']  # قیمت اخرین معامله
            link = new_symbols[symbol]['link']
            data = new_symbols[symbol]['symbol']
            price_and_percentage = f"{lastPrice} ({lastPercent})"  # قیمت معامله و درصد

            try:
                each_haghighi_buy = nbu3 / nbu2 * lastPercent  # هر کد حقیقی
                each_haghighi_sel = nse3 / nse2 * lastPercent  # هر کد حقیقی
                if float(bu3 / nbu3) > m * 1 / 100:
                    GroupBuySale(data, "خرید", nbu2, each_haghighi_buy, bu3, price_and_percentage, link, time.strftime(
                        "%H:%M:%S")).add()
                    print(
                        Fore.GREEN + f'{str(bu3 / nbu3) + " میزان خرید هر خریدار"} {str(nbu3) + "تعداد خریدار": >20}{str(bu3) + " میزان خرید" : >20}{"[" + data + "]":>10}')

                if float(se3 / nse3) > m * 1 / 100:
                    GroupBuySale(data, "فروش", nse2, each_haghighi_sel, se3, price_and_percentage, link, time.strftime(
                        "%H:%M:%S")).add()
                    print(
                        Fore.RED + f'{str(se3 / nse3) + " میزان فروش هر فروشنده"} {str(nse3) + " تعداد فروشنده": >20}{str(se3) + " میزان فروش" : >20}{"[" + data + "]":>10}')
            except:
                pass

    # 2- آلارم تغییر سرانه قدرت خریدار و فروشنده
    def _capita_buy_sale(self, new_symbols, old_symbols):
        for symbol in new_symbols:
            bu1 = int(new_symbols[symbol]['haghighiBuy'].replace(',', ''))  # حجم خرید حقیقی
            nbu1 = int(new_symbols[symbol]['haghighiBuyNum'].replace(',', ''))  # تعداد معاملات خرید حقیقی
            se1 = int(new_symbols[symbol]['haghighiSellVol'].replace(',', ''))  # حجم فروش حقیقی
            nse1 = int(new_symbols[symbol]['haghighiSellNum'].replace(',', ''))  # تعداد معاملات فروش حقیقی

            bu2 = int(old_symbols[symbol]['haghighiBuy'].replace(',', ''))  # حجم خرید حقیقی
            nbu2 = int(old_symbols[symbol]['haghighiBuyNum'].replace(',', ''))  # تعداد معاملات خرید حقیقی
            se2 = int(old_symbols[symbol]['haghighiSellVol'].replace(',', ''))  # حجم فروش حقیقی
            nse2 = int(old_symbols[symbol]['haghighiSellNum'].replace(',', ''))  # تعداد معاملات فروش حقیقی

            data = new_symbols[symbol]['symbol']
            lastPrice = new_symbols[symbol]['lastPrice']  # قیمت اخرین معامله
            lastPercent = new_symbols[symbol]['lastPercent']  # قیمت اخرین معامله
            link = new_symbols[symbol]['link']

            try:
                percentage_change_buy_sale = ((bu2 / nbu2) / (se2 / nse2))
                if ((bu2 / nbu2) / (se2 / nse2)) > 2 * ((bu1 / nbu1) / (se1 / nse1)):
                    CapitaBuySale(data, "خرید", bu1 / nbu1, se1 / nse1, bu2 / nbu2, se2 / nse2,
                                  percentage_change_buy_sale, f"{lastPrice} ({lastPercent})", link,
                                  time.strftime("%H:%M:%S")).add()
                    print(
                        Fore.GREEN + f'{str(round(se1 / nse1)) + " سرانه فروش قدیم"}{str(round(bu1 / nbu1)) + " سرانه خرید قدیم":>25}{str(round(se2 / nse2)) + " سرانه فروش جدید":>25}{str(round(bu2 / nbu2)) + " سرانه خرید جدید" : >25}{" سرانه خریدار : وضعیت ":>25}{"[" + data + "]":>10}')

                if ((se2 / nse2) / (bu2 / nbu2)) > 2 * ((se1 / nse1) / (bu1 / nbu1)):
                    CapitaBuySale(data, "فروش", bu1 / nbu1, se1 / nse1, bu2 / nbu2, se2 / nse2,
                                  percentage_change_buy_sale, f"{lastPrice} ({lastPercent})", link,
                                  time.strftime("%H:%M:%S")).add()
                    print(
                        Fore.RED + f'{str(round(se1 / nse1)) + " سرانه فروش قدیم"}{str(round(bu1 / nbu1)) + " سرانه خرید قدیم":>25}{str(round(se2 / nse2)) + " سرانه فروش جدید":>25}{str(round(bu2 / nbu2)) + " سرانه خرید جدید" : >25}{"سرانه فروشند : وضعیت":>25}{"[" + data + "]":>10}')
            except:
                pass

    # 4- آلارم خرید و فروش سنگین حقوقی
    def _hoghoghi_buy_sale(self, new_symbols, old_symbols):
        for symbol in new_symbols:
            bu1 = int(new_symbols[symbol]['hoghighiBuyVol'].replace(',', ''))  # حجم خرید حقوقی
            se1 = int(new_symbols[symbol]['hoghoghiSellVol'].replace(',', ''))  # حجم  فروش حقوقی

            bu2 = int(old_symbols[symbol]['hoghighiBuyVol'].replace(',', ''))  # حجم خرید حقوقی
            se2 = int(old_symbols[symbol]['hoghoghiSellVol'].replace(',', ''))  # حجم  فروش حقوقی

            se3 = abs(se1 - se2)
            bu3 = abs(bu1 - bu2)

            lastPrice = new_symbols[symbol]['lastPrice']  # قیمت اخرین معامله
            lastPercent = new_symbols[symbol]['lastPercent']  # قیمت اخرین معامله
            data = new_symbols[symbol]['symbol']
            link = new_symbols[symbol]['link']
            m = new_symbols[symbol]['base_vol']
            m = int(m.split(':')[2].replace(',', ''))  # حجم مبنا  # حجم مبنا

            if bu3 > (m * 1 / 10):
                HoghoghiBuySale(data, "خرید", bu3, f"{lastPrice} ({lastPercent})", link,
                                time.strftime("%H:%M:%S")).add()

                print(
                    Fore.GREEN + f' {str(bu3) + " حجم خرید حقوقی"}{"[" + data + "]":>10}')

            if se3 > (m * 1 / 10):
                HoghoghiBuySale(data, "خرید", se3, f"{lastPrice} ({lastPercent})", link,
                                time.strftime("%H:%M:%S")).add()
                print(
                    Fore.RED + f' {str(se3) + " حجم فروش حقوقی"}{"[" + data + "]":>10}')

    def _clean_table(self):
        session.query(SaleQueue).delete()
        session.query(BuyQueue).delete()
        session.query(CapitaBuySale).delete()
        session.query(HoghoghiBuySale).delete()
        session.query(GroupBuySale).delete()
        session.commit()

    def main(self):
        time_queue = 1
        for i in range(2000):
            all = time.time()
            div1 = self.driver1.execute_script(self.script1)
            div2 = self.driver2.execute_script(self.script2)
            # اضافه کردن اطلاعات سه ستون به درایور دیگه
            new_symbols = {}
            a = 1
            for id in div2:
                try:
                    # test
                    if a == 4:
                        break
                    new_symbols[id] = {**div1[id], **div2[id]}
                    a += 1
                except:
                    pass

            if i == 0:
                old_symbols = new_symbols
            # claen database
            self._clean_table()
            try:
                print(Fore.WHITE + "-------------_group_buy_sale--------------------")
                self._group_buy_sale(new_symbols, old_symbols)
                print(Fore.WHITE + "-------------_capita_buy_sale--------------------")
                self._capita_buy_sale(new_symbols, old_symbols)
                print(Fore.WHITE + "-------------_hoghoghi_buy_sale--------------------")
                self._hoghoghi_buy_sale(new_symbols, old_symbols)
                if time_queue == 10:
                    print(Fore.WHITE + "-------------_sale_queue--------------------")
                    self._sale_queue(new_symbols, old_symbols)
                    print(Fore.WHITE + "-------------_buy_queue--------------------")
                    self._buy_queue(new_symbols, old_symbols)
                    time_queue = 0
            except Exception as e:
                print(Fore.RED + f"-----------{e}--------------")
            session.commit()
            old_symbols = new_symbols
            print(
                Fore.RED + f"___________________  all {time.time() - all} seconds____________")
            time.sleep(abs(1 - (time.time() - all)))
            time_queue += 1

    def run(self):
        Thread(target=self.main, args=()).start()

# a = AlarmBorce()
# a.run()
