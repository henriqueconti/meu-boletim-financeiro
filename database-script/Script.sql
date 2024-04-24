CREATE TABLE db_users_tickers (
  email VARCHAR(256) not null,
  ticker VARCHAR(5) not null,
  PRIMARY KEY (email, ticker)
);

select  * from db_users_tickers;