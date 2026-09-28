# Автоматизация проверок в Postman
**API:** Petstore Swagger (`https://petstore.swagger.io/v2`)

В коллекции реализован CRUD-цикл сущности Pet. Базовый URL вынесен в переменную окружения `{{baseUrl}}`.

## Запросы и автотесты (вкладка Tests)

**1. POST /pet (Создание питомца)**
Тело (JSON): `{"id": {{petId}}, "name": "Balu", "status": "available"}`
```javascript
pm.test("Status code is 200", function () {
    pm.response.to.have.status(200);
});
pm.test("Pet name is correct", function () {
    var jsonData = pm.response.json();
    pm.expect(jsonData.name).to.eql("Balu");
});
pm.test("Response time is less than 500ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(500);
});