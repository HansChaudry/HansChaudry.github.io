-- A1
Select count(actors) from actors
where date_of_birth > '1970-01-01';

--A2
select max(domestic_takings), min(domestic_takings) from movie_revenues;

-- A3
select sum(movie_length) from movies
where age_certificate = '15';

--A4
select count(directors) from directors
where nationality = 'Japanese';

--A5
select avg(movie_length) from movies
where movie_lang = 'Chinese';

--B1
select nationality, count(directors) from directors
group by nationality;

--B2
select movie_lang, age_certificate, sum(movie_length) from movies
group by movie_lang, age_certificate;

--B3
select movie_lang, sum(movie_length) from movies
group by movie_lang
having sum(movie_length)>500;

--C1
select ac.first_name, ac.last_name
from movies_actors ma join actors ac using(actor_id)
join movies mo using (movie_id)
join directors d on mo.director_id = d.director_id 
where d.first_name  = 'Wes' and d.last_name = 'Anderson';

--C2
select first_name, last_name, date_of_birth
from actors
where 
date_of_birth = (select max(date_of_birth) from actors) or
date_of_birth = (select min(date_of_birth) from actors);

--C3
select movie_name, movie_length, age_certificate
from movies
where movie_length > 
(select avg(movie_length) from movies 
where movie_length = movie_length);