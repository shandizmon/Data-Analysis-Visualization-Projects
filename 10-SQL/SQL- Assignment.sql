USE sakila;
# 1a:
SELECT first_name, last_name FROM actor;

# 1b:
SELECT CONCAT(UPPER(first_name) ,'-', UPPER(last_name)) as 'Actor Name' FROM actor limit 10;

# 2a:
SELECT actor_id, first_name, last_name FROM actor WHERE first_name = 'Joe';

# 2b:
SELECT actor_id, first_name, last_name FROM actor WHERE last_name like '%Gen%';

# 2c:
SELECT actor_id, first_name, last_name FROM actor WHERE last_name like '%LI%' ORDER BY last_name ASC , first_name ASC;

# 2d:
SELECT country_id, country FROM country WHERE country in ('Afghanistan', 'Bangladesh', 'China');

# 3a:
ALTER TABLE actor ADD middle_name VARCHAR(47) AFTER first_name;

# 3b:
ALTER TABLE actor MODIFY COLUMN middle_name blob;

#3c:
ALTER TABLE actor DROP COLUMN middle_name;

#4a:
SELECT last_name, COUNT(*) FROM actor GROUP BY last_name;

#4b:
SELECT last_name, last_name_count From 
(SELECT last_name, COUNT(*) AS last_name_count FROM actor GROUP BY last_name) as t1
WHERE last_name_count > 1;

#4c:
UPDATE actor SET first_name='HARPO' 
WHERE last_name='WILLIAMS' AND first_name='GROUCHO';

#4d: ( #actor_id=172)
UPDATE actor SET first_name= IF (first_name='HARPO','GROUCHO','MUCHO GROUCHO')
WHERE actor_id=172;

# Just to check and make sure that the changes happend (SELECT actor_id, first_name, last_name FROM actor WHERE actor_id=172)

#5a: 
SHOW CREATE TABLE address;

#6a:
SELECT first_name, last_name, address FROM staff JOIN address USING(address_id);

#6b:
SELECT first_name, last_name, Sum(amount) AS total_amount FROM staff JOIN payment USING(staff_id)
WHERE payment_date LIKE '2005-08%'
GROUP BY staff_id;

#6c:
SELECT title, COUNT(actor_id) AS actor_count FROM film JOIN film_actor USING(film_id)
GROUP BY title;

#6d:
SELECT title, COUNT(inventory_id) AS numper_of_copies FROM film JOIN inventory USING(film_id)
WHERE title='Hunchback Impossible';

#6e:
SELECT first_name, last_name, SUM(amount) AS payment FROM customer JOIN payment USING(customer_id)
GROUP BY customer_id
ORDER by last_name DESC;

#7a: 
SELECT title FROM film
WHERE (title LIKE 'K%' OR title LIKE 'Q%')
AND language_id IN (
       SELECT language_id 
       FROM language
       WHERE name='English' );

#7b:
SELECT first_name, last_name FROM actor 
WHERE actor_id IN (
	SELECT actor_id FROM film_actor
    WHERE film_id IN (
		SELECT film_id FROM film
		WHERE title='ALONE TRIP'));

#7c:
SELECT first_name, last_name, email FROM customer JOIN address USING (address_id)
JOIN city USING (city_id)
JOIN country USING (country_id)
WHERE country='Canada';
 
#7d:
SELECT title, category.name FROM film JOIN film_category USING(film_id)
JOIN category 
USING (category_id)
WHERE category.name='Family';
 
#7e:
SELECT title, COUNT(title) As number_of_order FROM film JOIN inventory USING(film_id)
JOIN rental USING (inventory_id)
GROUP BY title
ORDER BY number_of_order DESC;

#7f:
SELECT store_id, SUM(payment.amount) AS income FROM inventory JOIN rental USING (inventory_id)
JOIN payment USING (rental_id)
GROUP BY store_id;

#7g:
SELECT store_id, city, country FROM store JOIN address USING (address_id)
JOIN city USING (city_id)
JOIN country USING (country_id);

#7h:
SELECT category.name AS genre, SUM(amount) AS revenue FROM category JOIN film_category USING (category_id)
JOIN inventory USING (film_id)
JOIN  rental    USING(inventory_id)
JOIN  payment USING (rental_id)
GROUP BY genre
ORDER BY revenue DESC
LIMIT 5;

#8a:
CREATE VIEW  top_five_genres_revenue AS
SELECT category.name AS genre, SUM(amount) AS revenue FROM category JOIN film_category
USING (category_id)
JOIN inventory USING (film_id)
JOIN  rental USING(inventory_id)
JOIN  payment USING (rental_id)
GROUP BY genre
ORDER BY revenue DESC
LIMIT 5;

#8b: 
SELECT * FROM top_five_genres_revenue;
 
#8c:
DROP VIEW top_five_genres_revenue;

