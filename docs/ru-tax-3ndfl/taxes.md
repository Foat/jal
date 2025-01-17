### Инструкция по подготовке данных для декларации 3-НДФЛ для Interactive Brokers

*Данная инструкция представлена здесь в ознакомительных целях. Скриншоты ниже представлены на английском языке, но вы можете выбрать русский в программе (для смены языка с Английского на Русский нужно выбрать пункт меню Languages->Russian и перезапустить программу).
Данное программное обеспечение было создано для использования в личных целях и большая часть расчетов тестировалась с дивидендами и длинными позициями в долларах.  
Другие валюты, а так же короткие продажи, операции с опционами, облигациями, корпоративные события и специфические комиссии Interactive Brokers поддерживаются, но могут иметь недочёты.*


*Вы можете использовать jal свободно, но с обязательной ссылкой на https://github.com/titov-vv/jal в случае публикации в сети Интернет  
Информация об ошибках, замечания, пожелания и благодарности приветствуются. Помимо Github связаться со мной и задать вопросы можно по адресу [jal@gmx.ru](mailto:jal@gmx.ru?subject=%5BJAL%5D%20Tax%20report) или в [Telegram](https://t.me/jal_support).*


1. Нужно получить flex-отчет по всем операциям в формате XML.  
Для этого необходимо в личном кабинете Interactive Brokers выбрать раздел *Reports / Tax Docs*. 
На появившейся странице *Reports* нужно выбрать закладку *Flex Queries*. В разделе *Activity Flex Query* нужно нажать *'+'*, чтобы создать новый отчёт.
Далее необходимо выполнить настройку отчета:
    - *Query name* - нужно указать уникальное имя отчёта
    - *Sections* - нужно отменить необходимые секции отчета. Минимально необходимы: *Account Information, Cash Transactions, Corporate Actions, Financial Instrument Information, Trades, Transactions Fees, Transfers, Stock Grant Activity* (*Option Exercises, Assignments and Expirations* - если торгуете опционами)
    - *Format* - XML
    - *Date Format* - yyyyMMdd
    - *Time Format* - HHmmss
    - *Date/Time separator* - ;(semi-colon)
    - *Profit and Loss* - Default
    - на вопросы *Include Canceled Trades?, Include Currency Rates?, Display Account Alias in Place of Account ID?, Breakout by Day?* ответить No.  
    После этого нажать *Continue* и затем *Create*  
При выборе секций будет появляться окно для более детальной настройки - я рекомендую оставлять верхнюю часть *"Options"* без изменений, а в нижней выбирать *"Select All"*, чтобы включить все галочки (пример на скриншоте ниже).  
![IBRK account](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/ibkr_selection_example.png?raw=true)  
      
2. Вновь созданный flex-отчет появится в списке *Activity Flex Query*. Его нужно запустить по нажатию на стрелку вправо (команда *Run*).
Формат нужно оставить XML. В качестве периода максимум можно выбрать год — поэтому нужно выполнить отчет несколько раз, чтобы последовательно получить операции за всё время существования счёта.
В результате у вас будет один или несколько XML файлов с отчетами. В качестве примера для дальнейших действий я буду использовать [IBKR_flex_sample.xml](https://cdn.jsdelivr.net/gh/titov-vv/jal/docs/ru-tax-3ndfl/IBKR_flex_sample.xml)  

3. В *jal* все транзакции привязаны к тому или иному счету с определённой валютой. При импорте отчёта Interactive Brokers *jal* создаст нужные счета автоматически (при этом имя счёта будет иметь вид *Номер.Валюта*).
Если счёт с таким номером и валютой уже существует, то *jal* будет использовать его (новый счёт создан не будет). Для учёта операций ввода/вывода средств необходимо добавить ещё один счёт любого типа — его можно создать, когда *jal* спросит о том откуда или куда были переведены средства.  
В примере ниже я создал 2 счёта (как указано выше — этот шаг можно было пропустить):
    - счет типа *Investment*, у которого номер и валюта будут совпадать с номером и валютой счета Interactive Brokers (если бы я этого не сделал, то счёт был бы создан автоматически с именем U1234567.USD).  
Если вы хотите сохранить данные в файл программы 'Декларация', то нужно также указать страну счёта.  
    ![IBRK account](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/ibkr_account.png?raw=true)   
Так же я указал здесь Interactive Brokers в поле Bank/Broker - это название будет использоваться для учёта сумм удержанных/выплаченных брокером (комиссий, процентов и т.п.).
    - ещё один счет любого типа — он будет необходим для учета транзакций ввода/вывода денежных средств. Например:  
    ![Bank account](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/bank_account.png?raw=true)  
   
4. Непосредственно для загрузки отчёта вам необходимо выбрать пункт меню *Import->Statement->Interactive Brokers XML* (в русской версии *Импорт->Выписка->Interactive Brokers XML*), после чего указать XML файл, который необходимо загрузить.  
![Select statement](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/menu_selection.png?raw=true)  
Если ваш отчет содержит транзакции ввода/вывода денежных средств, то вы *jal* попросит вас указать какой счет нужно использовать для списания/зачисления этих средств (это должен быть другой счёт, отличный от вашего брокерского счёта). Например:   
![Select account](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/account_selection.png?raw=true)  
В случае успешного импорта, вы увидите сообщение *IB Flex-statement loaded successfully* на закладке *Logs* внизу главного окна программы:  
![Import success](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/import_log.png?raw=true)
  
5. После инициализации база *jal* содержит 3 валюты - RUB, USD и EUR. Если ваш отчет содержит больше валют, то *jal* добавит символ новой валюты автоматически.  
Для правильного создания налогового отчёта нужно через меню *Data->Assets* (*Данные->Ценные бумаги*) указать полное наименование валюты и указать источник для загрузки курсов - *Bank of Russia*.
   
6. После загрузки вы можете выбрать полный интервал времени и нужный счёт, чтобы проверить корректность импорта данных:  
![Main window](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/main_window.png?raw=true)  
Конечный баланс счёта может иметь незначительный отклонения - у меня они составляют несколько центов. Они связаны с тем, что Interactive Brokers округляют удержанный налог в отчётах. Чтобы исправить это, вы можете проголосовать по [этой ссылке](https://interactivebrokers.com/en/general/poll/featuresPoll.php?sid=15422).
   
7. Если ваш отчёт содержит корпоративные действия (особенно Spin-Off), то я рекомендую ознакомиться с [логикой, которая используется *jal* для их обработки](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/corporate_actions.md) и убедиться что вы указали правильную долю выделяемого актива.  
   
8. При подготовке декларации все суммы нужно пересчитать в рубли — для этого необходимо загрузить курсы валют.
Сделать это можно с помощью меню *Import->Quotes...* (в русской версии *Импорт->Котировки...*), указав необходимый диапазон дат:  
![Quotes](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/update_quotes.png?raw=true)
   
9. С помощью *jal* вы можете подготовить как просто расчёт в виде файла Excel, так и автоматически занести данные в файл программы *"Декларация"* (Версии 2020 и 2021 года). 
Все шаги, связанные с программой *"Декларация"* являются необязательными и вы можете их пропустить.
      
10. Для выполнения расчёта вам необходимо выбрать пункт меню *Export->Tax Report \[RU]* (в русской версии *Экспорт->Налоговый отчёт \[RU]*) и заполнить параметры в появившемся диалоговом окне:  
![Report parameters](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_params.png?raw=true)  
Вам необходимо задать:
    - год за который формируется отчёт (2020)
    - счёт, который содержит операции, для отчёта (в моём примере *IBKR*)
    - имя файла Excel, куда будет сохранён отчёт
    - поставить галочку *Create tax form in "Декларация" file format*, если вы хотите внести данные в файл программы *"Декларация"*
    - *Output file* - указать имя файла, куда будет сохранена декларация в формате **.dcX*
    - *Update only information about dividends* - существуют разные практики занесения информации о сделках в декларацию. 
    Поэтому если вы не хотите, чтобы каждая сделка добавлялась отдельным листом — поставьте эту галочку и в файл будет добавлена лишь информация о дивидендах.
Нажмите кнопку *OK* - в случае успешного выполнения на диске будут записаны соответствующие файлы
      
11. Если вы выбирали обновление файла декларации, то вы можете теперь открыть его с помощью программы *"Декларация"* и проверить, что информация была добавлена на закладку *Доходы за пределами РФ*  
![Declaration Updated](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/declaration_3.png?raw=true)
    
12. [Получившийся Excel-файл с расчётом](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/3ndfl_tax_report.xlsx) будет содержать 7 закладок: Дивиденды, Акции, Облигации, ПФИ, Корпоративные события, Комиссии и Проценты. 
    Некоторые из страниц могут быть пустыми, если у вас не было соответствующих операций в отчётном периоде. Ниже примеры скриншотов для некоторых отчётов:    
    - Расчёт дивидендов  
    ![Report Dividends](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_1.png?raw=true)  
      Если вы видите N/A в столбце 'Страна' (столбец 10). то это значит страна не была указана для данной бумаги. Это не влияет на расчёт если уплаченный налог (столбец 7) равен нулю, т.к. СОИДН не имеет значения. 
      В противном случае вам нужно указать страну для ценной бумаги через меню Данные-> Ценные бумаги.
    - Расчёт сделок с ценными бумагами 
    ![Report Deals](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_2.png?raw=true)
    - Расчёт сделок с производными финансовыми инструментами
    ![Report Derivatives](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_3.png?raw=true)
    - Расчёт комиссий и прочих операций  
    ![Report Fees](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_4.png?raw=true)
    - Расчёт по корпоративным событиям  
    ![Report Corporate Actions](https://github.com/titov-vv/jal/blob/master/docs/ru-tax-3ndfl/img/report_5.png?raw=true)

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Ftitov-vv%2Fjal%2Fblob%2Fmaster%2Fdocs%2Fru-tax-3ndfl%2Ftaxes.md&count_bg=%23B981DD&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=tax&edge_flat=false)](https://hits.seeyoufarm.com)
