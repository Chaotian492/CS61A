.read data.sql


CREATE TABLE average_prices AS
  SELECT category, avg(MSRP) as average_price
      from products
          group by category;


CREATE TABLE lowest_prices AS
  SELECT store,item, min(price) as lowest_price
    from inventory
        group by item;

CREATE TABLE best_deal AS
    SELECT name, min(MSRP/rating) as best_choose
        from products
            group by category;
CREATE TABLE shopping_list AS
    SELECT item, store
        from lowest_prices,best_deal
        where item=name;


CREATE TABLE total_bandwidth AS
  SELECT sum(Mbs)
    from shopping_list as sh, stores as st
    where sh.store=st.store;

