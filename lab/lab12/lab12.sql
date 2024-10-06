.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet FROM students WHERE color='blue' and pet='dog';

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song FROM students WHERE color='blue' and pet='dog';


CREATE TABLE smallest_int AS
  SELECT  time,smallest FROM students WHERE smallest > 2 order by smallest LIMIT 20;


CREATE TABLE matchmaker AS
  SELECT a.pet as total_pet, a.song as total_song, a.color as color1,b.color as color2
    from students as a, students as b
    where a.time < b.time and a.pet=b.pet and a.song=b.song;


CREATE TABLE sevens AS
  SELECT students.seven
    from students, numbers
    where students.number = 7 and numbers.'7'='True' and students.time=numbers.time;

