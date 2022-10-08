# Inno-Music-Club-Bot
![version](https://img.shields.io/badge/version-alpha_2.0-blue) ![version](https://img.shields.io/badge/python-3.10-58851e.svg)


##### This is second realization of music club bot, performed for Innopolis University Music Club.

## Key goals of this project are:
    
* Create telegram bot for the music club using
    ideas and functional of previous one. 
* Use new technological
    stack of python (previous one was in C#).

## Requirements:
* `python 3.10`
* `pyrogram`
* `pyromod`
* `psycopg` Note: Third version of psycopg

## How to start:

[//]: # (TODO: show normal context)

### Context
+ PostgreSQL

---

### Run PostgreSQL (optional)

Get official postgres docker image

    docker pull postgres

You can run Postgres this way (map a port):

MY_POSTGRES_PASSWORD - your password to access to postgres

    docker run --name some-postgres -e POSTGRES_PASSWORD=MY_POSTGRES_PASSWORD -d -p 5432:5432 postgres

To test: Run the postgres database (command above)

    docker ps
    CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                 NAMES
    05b3a3471f6f        postgres            "/docker-entrypoint.s"   1 seconds ago       Up 1 seconds        0.0.0.0:5432->5432/tcp    some-postgres

Go inside your container and create a database:


    docker exec -it 05b3a3471f6f bash
    root@05b3a3471f6f:/# psql -U postgres
    postgres-# CREATE DATABASE mytest;
    postgres-# \q

Go to your localhost (where you have some tool or the psql client).

    psql -h localhost -p MY_POSTGRES_PORT -U postgres

(Password: MY_POSTGRES_PASSWORD)

    postgres=# \l

                             List of databases
       Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges
    -----------+----------+----------+------------+------------+-----------------------
    mytest    | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
    postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 |
    template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres
...




![Telegram](https://img.shields.io/badge/Join-Telegram-blue?style=for-the-badge&logo=data:image/svg%2bxml;base64,PHN2ZyBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCAyNCAyNCIgaGVpZ2h0PSI1MTIiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjUxMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJtOS40MTcgMTUuMTgxLS4zOTcgNS41ODRjLjU2OCAwIC44MTQtLjI0NCAxLjEwOS0uNTM3bDIuNjYzLTIuNTQ1IDUuNTE4IDQuMDQxYzEuMDEyLjU2NCAxLjcyNS4yNjcgMS45OTgtLjkzMWwzLjYyMi0xNi45NzIuMDAxLS4wMDFjLjMyMS0xLjQ5Ni0uNTQxLTIuMDgxLTEuNTI3LTEuNzE0bC0yMS4yOSA4LjE1MWMtMS40NTMuNTY0LTEuNDMxIDEuMzc0LS4yNDcgMS43NDFsNS40NDMgMS42OTMgMTIuNjQzLTcuOTExYy41OTUtLjM5NCAxLjEzNi0uMTc2LjY5MS4yMTh6IiBmaWxsPSIjMDM5YmU1Ii8+PC9zdmc+)
