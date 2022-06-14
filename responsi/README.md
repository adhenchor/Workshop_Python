> Pembahasan Responsi

# **RESPONSI WORKSHOP PYTHON**

## menampilkan data dari file yang telah saya ambil di internet.

<hr>

```
import csv
import urllib.request

url = ('https://people.sc.fsu.edu/~jburkardt/data/csv/addresses.csv' 'r')
response = urllib.request.urlopen(url)
cr = csv.reader(response)

for rows in cr:
    print(rows)
```

pertama adalah import library csv dan urllib.request untuk python 3 ke atas.
selanjutnya adalah memasukkan url dari file csv yang diambil dari internet. lalu terakhir print data tersebut.
