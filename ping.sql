/* i created a database named ping and a table with ping results and the time of ping */

/* CREATE DATABASE ping; */
CREATE TABLE ping_results(
    the_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP PRIMARY KEY,
    ping INT NOT NULL
);

SELECT (data_length+index_length)/power(1024,1) tablesize_kb
FROM information_schema.tables
WHERE table_schema='ping' and table_name='ping_results';
