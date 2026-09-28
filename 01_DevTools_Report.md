# Отчет по анализу трафика (DevTools)
**Объект тестирования:** Форма авторизации (тестовый стенд)

## 1. Анализ запросов (Network)
**Успешная авторизация:**
* **Метод:** POST
* **URL:** `/api/v1/auth/login`
* **Status Code:** 200 OK
* **Request Payload (Тело запроса):** `{"username": "testuser", "password": "Password123!"}`
* **Response (Тело ответа):** `{"token": "eyJhbGciOiJIUzI...", "userId": 7483}`
* *[Скриншот: вкладка Network, выделен запрос login, видно статус 200]*

**Неуспешная авторизация (неверный пароль):**
* **Status Code:** 401 Unauthorized
* **Response:** `{"error": "Invalid credentials", "code": 104}`
* *[Скриншот: вкладка Network, статус 401, вкладка Response]*

## 2. Анализ производительности и кэша
* **Самый долгий запрос:** `GET /api/v1/products` (Время: 1.2s, TTFB: 1.1s). Сервер долго формирует ответ.
* **Cache-Control:** В заголовках статики (CSS/JS) указан `Cache-Control: max-age=31536000`. При повторной загрузке файлы отдаются со статусом `200 OK (from memory cache)` или `(from disk cache)`.
* *[Скриншот: колонка Size со значениями memory cache]*

## 3. Анализ Cookies (Application)
* Токен авторизации сохраняется в Cookies.
* **Атрибуты безопасности:** Установлены флаги `HttpOnly` (защита от XSS) и `Secure` (передача только по HTTPS). `SameSite=Lax`.
* *[Скриншот: вкладка Application -> Cookies, видны галочки в столбцах Secure и HttpOnly]*

## 4. Ошибки фронтенда (Console)
* Найдена ошибка: `Uncaught TypeError: Cannot read properties of undefined (reading 'map') at renderList (main.js:45)`
* *[Скриншот: вкладка Console с красным текстом ошибки]*