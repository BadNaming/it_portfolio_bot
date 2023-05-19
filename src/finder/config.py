TEST_URL = ''
CREDS = {
  "type": "service_account",
  "project_id": "itportfolio",
  "private_key_id": "",
  "private_key": "",
  "client_email": "",
  "client_id": "",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/itporfolio%40itportfolio.iam.gserviceaccount.com"
}
URL = ''
TOKEN = ''
TEST_USER = ''


SPECIALITIES = [
  'Менеджер проектов',
  'Python- разработчик',
  'Менеджер продукта',
  'Системный аналитик',
  'Бизнес аналитик',
  'Аналитик данных',
  'Дизайнер',
  'Devops',
  'Маркетолог',
  'SMM',
  'Привлечение трафика',
  'Менеджер маркетплейсов',
  'Тестировщик ручной',
  'Тестировщик авто',
  'Тестирование нагрузочное',
  'Бэкенд',
  'Фронтенд',
  'Разработчика C++',
  'Веб-разработчик',
  'Java-разработчик',
  'Android-разработчик',
  'IOS-разработчик',
  'Go-разработчик',
  'Инженер облачных сервисов',
  'Инженер данных',
  'Data Sceience',
  'Computer Vision',
  'HR',
  'Другая специальность',
]
EXPERIENCE = ['Без опыта', '1 год', '2 года', '3 года', 'Более 3-х лет']


TEXT = ('Имя: <b>{name}</b>,\n'
        'Telegram: {tg_nickname},\n'
        'Город: {city},\n'
        'Занятость: {available},\n'
        'Могу работать в неделю: {worktime}, \n'
        'Где учился: {education},\n'
        'Чего жду: {wants},\n'
        'Чем могу помочь: {can_do}\n'
        '------------------------- \n')


SEARCH_TEXT = 'Искать людей в команду'
ABORT_TEXT = 'Сбросить поиск'
TRIGGERS = SPECIALITIES + EXPERIENCE + [SEARCH_TEXT]
WELCOME_TEXT = ("Привет! Давай-ка я помогу тебе найти "
                "соратников в команду всего в несколько шагов.")
STEP1_TEXT = 'Шаг первый. Выбирай специальность'
STEP2_TEXT = 'Шаг второй. Насколько опытный нужен человек?'
NOT_FOUND = 'Сейчас нет подходящих кандидатов:('
