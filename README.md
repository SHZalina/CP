# Описание проекта "Котопес"
## Веб-приложение для продажи и покупки домашних питомцев.
Данное веб-приложение разработано с использованием Django и PostgreSQL и предоставляет функциональность для продажи и покупки домашних питомцев. 
Зарегестрированные пользователи могут размещать объявления о питомцах, просматривать доступных для продажи питомцев, а также осуществлять покупку выбранных питомцев.
Необходимо спроектировать систему для продажи животных “Котопес”, которая должна автоматизировать процесс 
приобретения и сдачи домашних животных. Система должна включать в себя возможность регистрации пользователя, 
размещения анкет животных в каталоге на продажу или передачу в добрые руки, возможность покупки животного, а 
также логистическую службу доставки оного. 
Зарегистрированный пользователь может как размещать обьявления, так и добавлять запросы на приобреьение животных. 
Процесс выбора заключает в себе выбор клиентом животного путем сортировки из списка с применением фильтров: 
вид животного, порода, возраст, вес и прочие сопутствующие характеристики. 
Покупатель может оставлять заявку для продавца на приобретение питомца.
Продавец может связаться с клиентом посредством номера телефона или электронной почты, указанной в запросе. 

# Основные возможности
<ol>
  <li>Регистрация пользователей и аутентификация для доступа к функционалу приложения.</li>
  <li>Смена пароля в личном кабинете.</li>
  <li>Каталог питомцев с фильтрами для удобного поиска.</li>
  <li>Подробные страницы питомцев с информацией о виде, возрасте, характере и других характеристиках.</li>
  <li>Добавление запроса покупки для владельца объявления на определенного питомца с возможностью указать дополнительные требования.</li>
  <li>Личный кабинет для просмотра запросов и редактирования/создания/удаления объявления.</li>
  <li>Уведомления по электронной почте о новых запросах.</li>
  <li>Административный интерфейс для управления питомцами, пользователями и заказами.</li>
</ol> 

# Технологии
<ul>
  <li>Django - фреймворк для разработки веб-приложений на языке Python.</li>
  <li>PostgreSQL - открытая реляционная база данных.</li>
  <li>HTML, CSS и JavaScript - для создания пользовательского интерфейса и взаимодействия с пользователем.</li>
  <li>Bootstrap - фреймворк для создания отзывчивого и стильного веб-дизайна.</li>
</ul> 

# Правила для команды разработчиков

1. Коммуникация:
   - Созвоны для обсуждения прогресса проекта, проблем и решений по четвергам и воскресеньям каждую неделю. О точном времени довогориваемся непосредственно за день до.
   - Коммуникация происходит в Discord и VK. Также используется демонстрация экрана или подключение к ноутбуку разработчика с проблемами через AnyDesk для для быстрого решения проблем.
   
2. Использование системы контроля версий:
   - Все члены команды разработчиков должны использовать систему контроля версий, такую как Git, для управления кодом проекта.
   - Регулярное коммитирование изменений в репозиторий и описание изменений в коммитах для лучшей отслеживаемости и командной работы.
   - Главная ветка, в которой хранится основной рабочий код, - HEADS. В неё происходит слияние веток [main](https://github.com/SHZalina/CP) и [messi!messi!messi!](https://github.com/SHZalina/CP/tree/messi!messi!messi!) через команду "git merge ...".

Ветка, в которой пишет код [Залина](https://github.com/SHZalina) - main. 
Ветка, в которой пишет код [Маша](https://github.com/bread133) - messi!messi!messi! и messi. 

3. Правила написания кода:
   - Соблюдение общепринятых стандартов кодирования Python (PEP 8), для обеспечения читаемости и согласованности кода.
   - Использование описательных и понятных имен переменных, функций и классов.
   - Комментирование кода необязательно. К каждому созвону составляется подробная записка от каждого члена команды о проделанной работе и выполненных задачах.

4. Тестирование:
   - Создание и выполнение тестовых сценариев для проверки функциональности и стабильности приложения.
   - Использование инструментов рунчого и автоматического тестирования для обеспечения надежности и устранения ошибок.
   - Проведение регулярных ревизий кода для выявления потенциальных проблем и улучшения качества кода.
   
5. Документация и знание проекта:
   - Во время реализации веб-приложения происходит создание документации, описывающей архитектуру, функциональность и особенности проекта.
   - Постоянные обмен информацией между членами команды, чтобы каждый был хорошо осведомлен о различных аспектах проекта.

# Распределение задач
1. [Маша](https://github.com/bread133) - разработчик, тестировщик:
   - back + front;
   - создание страницы about.html;
   - cоздание моделей для пользователей;
   - разработка методов регистрации, валидации данных, подтверждения регистрации, аутентификацию и выход из системы;
   - реализация метода контроллера и представления панели управления обьявлений для каждого пользователя dashboard;
   - создание шаблонов для отображения регистрации на сайте, личного кабинета пользователей;
   - разработка представления восстановления пароля по почте;
   - изменение представления сайта администрирования;
   - ручное тестирование аутентификации, авторизации и управления пользователями;
   - ручное тестирования всего реализованного функнционала.
   
2. [Залина](https://github.com/SHZalina) - разработчик, тимлид:
   - back + front;
   - реализация моделей для объявлений и запросов;
   - создание главной статраницы index.html;
   - настройка отображения объявлений на странице, переход между страницами;
   - разработка методов поиска объявлений по фильтрам (описание, цена, порода, город, вид питомца) и перехода на страницу с подробным описанием конкретного объявления;
   - реализация метода запроса на объявление;
   - разработка методов для создания, редактирования и удаления объявления в лк;
   - реализация методов просмотра запросов на объявления конкретного пользователя в лк и запросов самого пользователя на другие объявления;
   - создание шаблонов для поиска, отображения данных питомцев, запросов на объявления и создание нового объявления;
   - ручное тестирование своего реализованного функнционала;
   - дизайн логотипа.
  
Оба разработчика также должны выполнять следующие обязанности:
   - разработка и поддержка серверной и клиентской части приложения на Django;
   - интеграция с базой данных PostgreSQL;
   - разработка пользовательского интерфейса с использованием HTML, CSS и JavaScript;
   - cоблюдение стандартов написания кода;
   - регулярная коммуникация между собой и обмен знаниями для эффективной работы.

# Метрики
1. Оценка размера ПО
  - Количество строк кода:
  <code>
  -------------------------------------------------------------------------------
  Язык ПО                     Файлы    Пустые строки    Комментарии           Код
  -------------------------------------------------------------------------------
  CSS                            5             2441             13          11909
  SVG                            3                0              0           4065
  HTML                          24               59             26           1465
  Python                        39              173             71            952
  JavaScript                     4                1             21              8
  -------------------------------------------------------------------------------
  Всего:                        75             2674            131          18399
  -------------------------------------------------------------------------------
  </code><br>
