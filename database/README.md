# Databse

Edit files in `./sqls` and adjust `Dockerfile` to change docker init schema.

The followings are examples

```sh
ADD ./sqls/init.sql /docker-entrypoint-initdb.d
```
