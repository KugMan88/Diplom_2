import requests
import allure
from constants.urls_constants import UrlsConstants


@allure.feature('Проверка авторизации пользователя')
class TestLoginUser:
    @allure.title('Тест авторизации существующего пользователя')
    @allure.description('Успешная авторизация пользователя')
    def test_login_existing_user_successful(self, user_data):
        payload = user_data
        response = requests.post(UrlsConstants.LOGIN_USER, data=payload)
        assert response.status_code == 200 and response.json()['success']

    @allure.title('Тест авторизации с неверным логином и паролем')
    @allure.description('Получение ошибки. Авторизация не выполнена')
    def test_login_user_incorrect_email_and_password_error(self, user_data):
        payload = user_data.copy()
        payload["email"] += 'incorrect'
        payload["password"] += 1
        response = requests.post(UrlsConstants.LOGIN_USER, data=payload)
        assert response.status_code == 401
        assert response.text == '{"success":false,"message":"email or password are incorrect"}'