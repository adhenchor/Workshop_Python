> Pembahasan Pertemuan ke 10

# **Akses Ke Database CockroachDB Menggunakan psycopg2 dan Menggunakan SQLAlchemy**

## **psycopg2**

<hr>

### **Langkah 1 Menginstal CockroachDB**

<hr>

1.  Menginstal CockroachDB binary

```
$ curl https://binaries.cockroachdb.com/cockroach-v21.2.10.linux-amd64.tgz | tar -xz && sudo cp -i cockroach-v21.2.10.linux-amd64/cockroach /usr/local/bin/
```

2.  Memasukan library GEOS

- Membuat direktori untuk menyimpan library

```
$ mkdir -p /usr/local/lib/cockroach
```

- Masukan library kedalam direktori yang telah dibuat

```
$ cp -i cockroach-v21.2.10.linux-amd64/lib/libgeos.so /usr/local/lib/cockroach/
```

```
$ cp -i cockroach-v21.2.10.linux-amd64/lib/libgeos_c.so /usr/local/lib/cockroach/
```

Jika terjadi error, coba untuk menambahkan sudo, berikut contoh perintahnya :

```
$ sudo mkdir -p /usr/local/lib/cockroach
```

3.  Konfirmasi CockroachDB apakah bisa mengeksekusi spesial query

- pastikan bahwa Cockroach binary berhasil terinstall

```
$ which cockroach
```

```
/usr/local/bin/cockroach
```

- Memulai cluster untuk melakukan demo

```
$ cockroach demo
```

- Pada cluster jalankan perintah di bawah untuk menguji apakah library telah berhasil di install

```
> SELECT ST_IsValid(ST_MakePoint(1,2));
```

Berikut hasil outputnya jika berhasil

```
st_isvalid
--------------
true
(1 row)
```

Berikut ini adalah hasil output jika library di instal pada direktori yang salah

```
ERROR: st_isvalid(): geos: error during GEOS init: geos: cannot load GEOS from dir "/usr/local/lib/cockroach": failed to execute dlopen
          Failed running "sql"
```

### **Langkah ke 2 Memulai CockroachDB**

<hr>

1. Menjalakan Cockroach dengan menggunakan perintah

```
$  cockroach start-single-node --advertise-addr 'localhost' --insecure
```

Berikut output yang keluar jika berhasil menjalankan CockroachDB

```
CockroachDB node starting at 2022-05-16 23:11:36.154175237 +0000 UTC (took 1.2s)
build:               CCL v21.2.10 @ 2022/05/02 17:38:58 (go1.16.6)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257/defaultdb?sslmode=disable
sql (JDBC):          jdbc:postgresql://localhost:26257/defaultdb?sslmode=disable&user=root
RPC client flags:    cockroach <client cmd> --host=localhost:26257 --insecure
logs:                /home/ade/cockroach-data/logs
temp dir:            /home/ade/cockroach-data/cockroach-temp263191760
external I/O path:   /home/ade/cockroach-data/extern
store[0]:            path=/home/ade/cockroach-data
storage engine:      pebble
status:              initialized new cluster
clusterID:           aa125fa5-d68d-5152-743b-6c20485872b1
nodeID:              1
```

### **Langkah Ke 3 Mengambil Sampel Code**

<hr>

clone sampel code yang ada pada Github repo :

```
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```

### **Langkah Ke 4 Menginstall psycopg2 driver**

<hr>

```
$ pip install psycopg2-binary
```

### **Langkah Ke 5 Menjalankan Kode**

<hr>

1. Jalakan perintah berikut untuk mengatur koneksi dengan CockroachDB cloud cluster

```
$ export DATABASE_URL="postgresql://root@localhost:26257/defaultdb?sslmode=disable"
```

> Catatan gunakan koneksi db yang terdapat pada komputer anda

Jalankan perintah berikut

```
$ cd hello-world-python-psycopg2
```

```
$ python example.py
```

Berikut outputnya

```bash
ade@Adhenchor:~/hello-world-python-psycopg2$ python3 example.py
Balances at Tue May 17 01:43:18 2022:
(1, 1000)
(2, 250)
Balances at Tue May 17 01:43:18 2022:
(1, 900)
(2, 350)
```

## **SQLAlchemy**

<hr>

### **Langkah 1 Dapatkan Kode**

<hr>

Clone code yang terdapat pada github

```
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```

### **Langkah Ke 2 Instal virtualenv**

<hr>

1. Jalankan perintah berikut

```
$ pip install virtualenv
```

2. Buat dan jalankan virtual envirotment

```
$ virtualenv env
```

```
$ source env/bin/activate
3. Install moduls
```

```
$ pip install -r requirements.txt
```

### **Langkah Ke 3 Inisialisai Database**

<hr>

1. Jalakan perintah berikut untuk mengatur koneksi cluster

```
export DATABASE_URL="{connection-string}"
```

2. Untuk inisialisasi sampel database menggunakan Cockroach sql

```
$ cat dbinit.sql | cockroach sql --url $DATABASE_URL
```

Berikut outputnya

```
CREATE TABLE

Time: 19ms
```

### **Langkah Ke 4 Menjalankan Kode**

1. Jalankan perintah berikut

```
$ python main.py
```

Berikut hasil outputnya

```bash
(env) ade@Adhenchor:~/example-app-python-sqlalchemy$ python main.py
Creating new accounts...
Created new account with id 0aad1174-a541-473b-8b74-a267fcafc8f2 and balance 512043.
Created new account with id 5547f6aa-a8e0-49c3-aeae-fdd04985196c and balance 621384.
Created new account with id a4453ccc-491e-4c45-a3ca-efe9e5da880e and balance 935715.
Created new account with id 0d79323f-634d-4597-8213-c291a655680d and balance 743929.
Created new account with id 44c31b10-fb55-4f9e-91d6-6d9f642d6a2c and balance 964568.
Created new account with id b1ac3f8b-ee0e-4bb4-aa3b-774362e49505 and balance 274281.
Created new account with id d68346f5-2d5e-49e2-8427-83bba9ccf4cf and balance 637342.
Created new account with id 534fe2fd-834b-4ea3-a5f8-5f7d6e8e51a3 and balance 645410.
Created new account with id 6c2d71ab-180b-4608-9e45-7df461a01701 and balance 515972.
Created new account with id aed6c03b-4b5f-42d6-9c13-b7de02b528e7 and balance 823291.
Created new account with id 805240c1-241d-41dc-82a6-b7fe1109bb79 and balance 844564.
Created new account with id 8012c16d-d571-4537-8da1-007d54ea0036 and balance 381513.
Created new account with id ed827cf9-b47a-4c3b-9141-84a0d7eb54b4 and balance 932731.
Created new account with id d93f4bd3-4d34-407b-aade-57d0052cf41d and balance 175378.
Created new account with id aa23b487-3b90-418f-bc08-ecdbb9c40cb3 and balance 569715.
Created new account with id fe181250-1b37-47fa-bf43-aed64a3a8b59 and balance 335594.
Created new account with id 824f61e9-2421-4a6b-864e-0deacc6ade3e and balance 163296.
Created new account with id 6f7cfb30-b691-47a4-9daa-bd71baccaac3 and balance 952738.
Created new account with id 4e85af9d-ce0d-4f4f-b67d-5e45b98cb365 and balance 718866.
Created new account with id 07ba7733-d133-4881-80cc-e35c576fe7dd and balance 917863.
Created new account with id 49356d15-0075-46d4-b9b0-83cb58eaacbe and balance 661361.

```

Masuk ke sql cockroach lalu jalankan perintah berikut ini :

```
SELECT COUNT(*) FROM accounts;
```

Outputnya sebagai berikut :

```bash
root@:26257/defaultdb> SELECT COUNT(*) FROM accounts;
  count
---------
     95
(1 row)


Time: 1ms total (execution 1ms / network 0ms)

root@:26257/defaultdb>
```
