from grab import Grab
from datetime import datetime, date

# now_date = datetime.today()                         # Получаем текущую дату    
# cur_year = str(now_date.year)                       # Год текущий
# cur_month = str(now_date.month)                     # Месяц текущий
# cur_day = str(now_date.day)                         # День текущий

#url = 'https://my.kvant-telecom.ru/calls/?&period_start=' + cur_year + '-' + cur_month + '-' + cur_day + '&period_end=' + cur_year + '-' + cur_month + '-' + cur_day # Формируем ссылку с детализацией за сегодняшний день
g = Grab()                                          # Инициализация объекта для граббинга страницы
g.go('https://lkz.ahml.ru/borrower/')          # Авторизация на сайте детализации Квант-телеком
g.set_input_by_id('b_auth_login', '00087432')     # Вводим логин
g.set_input_by_id('b_auth_password', '')    # Водим пароль
g.submit()                                          # Отсылаем форму
g.go(url) 
