1) В настройках Google аккаунта: Security - Less secure app access = ON

2) В настройках Google почты поменять язык интерфейса на английский

3) Собрать Docker образ для запуска тестов командой 
	"docker build -t your_image_name ."
	
4) Подставить в docker-compose.yml имя собранного образа, логин и пароль от почты gmail 
(соответственно в значения image, EMAIL_ADDRESS, EMAIL_PASS)

5) Запустить тесты командой
	"docker-compose up"
	
6) После завершения посмотреть отчет можно с помощью команды
	"allure serve ./allure_report"