CREATE TABLE db_users_tickers (
  email VARCHAR(256) not null primary key,
  tickers VARCHAR(5)[] not null
);


select  * from db_users_tickers;
