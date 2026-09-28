-- 1. Вывод всех строк таблицы (базовая проверка содержимого)
SELECT * FROM users;

-- 2. Фильтрация по двум условиям (найти активных клиентов из Москвы)
SELECT * FROM users 
WHERE city = 'Moscow' AND status = 'active';

-- 3. Сортировка и лимит (топ-10 самых дорогих заказов)
SELECT order_id, total_amount 
FROM orders 
ORDER BY total_amount DESC 
LIMIT 10;

-- 4. Группировка и подсчет (количество заказов по статусам)
SELECT status, COUNT(order_id) as orders_count 
FROM orders 
GROUP BY status;

-- 5. JOIN двух таблиц (информация о заказе + email пользователя)
SELECT o.order_id, o.total_amount, u.email 
FROM orders o
JOIN users u ON o.user_id = u.user_id;

-- 6. Поиск дубликатов (пользователи с одинаковым email)
SELECT email, COUNT(*) 
FROM users 
GROUP BY email 
HAVING COUNT(*) > 1;

-- 7. Поиск записей с NULL (заказы без назначенного курьера)
SELECT * FROM orders 
WHERE courier_id IS NULL;

-- 8. Отчет с агрегацией (выручка и средний чек по месяцам)
SELECT 
    EXTRACT(MONTH FROM created_at) as order_month,
    COUNT(order_id) as total_orders,
    SUM(total_amount) as revenue,
    AVG(total_amount) as average_check
FROM orders
GROUP BY EXTRACT(MONTH FROM created_at);

-- 9. Поиск "потерянных" данных (пользователи без единого заказа - LEFT JOIN)
SELECT u.user_id, u.email
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

-- 10. Ситуация из работы: проверка конкретного заказа после создания на фронте
SELECT status, total_amount, payment_status 
FROM orders 
WHERE order_number = 'A-993812';