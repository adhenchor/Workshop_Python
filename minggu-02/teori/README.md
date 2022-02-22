> Pertemuan Minggu ke - 2

# Pengaturan Aliran Control Flow

## 1. Pernyataan IF

Pada python pernyataan if sangatlah sederhana, tidak menggunakan tanda () dan {}. Kata kunci else if juga bisa diringkas menjadi elif saja.

## 2. Perulangan for

Perulangan for pada python memiliki perbedaan dengan perulangan for yang ada pada bahasa pemrograman lain. nilai pengubah pada perulangan for juga tidak harus selalu dalam bentuk angka, nilai - nilai yang berada didalam list juga dapat langsung ditampilkan secara urut.

## 3. Fungsi range()

Fungsi range dapat digunakan untuk mengulangi urutan angka. misal menampilkan urutan angka dari 0 sampai 7, maka tinggal mengetikkan range(6).

## 4. Pernyataan break dan continue

Pernyataan break digunakan untuk menghentikan program atau keluar dari perulangan(stop). Pernyataan continue digunakan untuk melanjutkan perulangan.

## 5. Pernyataan pass

Pernyataan pass digunakan untuk pernyataan yang tidak melakukan apa - apa, atau bisa digunakan sebagai placeholder untuk fungsi dan pernyataan bersyarat.

## 6. Mendefinisikan Fungsi

Untuk mendefinisikan sebuah fungsi digunakan kata kunci def. Setalah kata kunci def diikuti dengan nama fungsi dan parameternya. Kemudian baru badan dari fungsi yang didefinisikan.
Mendefiniskan Fungsi Lebih Lanjut

### 1. **Nilai Argumen Bawaan**

Pada suatu fungsi dapat didefinisikan nilai atribut default.

> def ask_ok(prompt, retries=4, reminder='Please try again!'): nilai dari atribut retries dan reminder sudah di set pada fungsi, sehingga ketika fungsi dipanggil attribut sudah mempunyai nilai default untuk ditampilkan.

### 2. **Argumen Kata Kunci**

Dalam pemanggilan fungsi, argumen kata kunci harus mengikuti posisi argumen daripada fungsi. Semua argumen kata kunci yang diteruskan kepada fungsi juga harus cocok dengan salah satu argumen yang ada pada fungsi.

### 3. **Parameter spesial**

berikut adalah cara mendefinisikan parameter spesial

> def f(pos1, pos2, /, pos_or_kwd, \*, kwd1, kwd2):

---

| | |
| Positional or keyword |
| - Keyword only
-- Positional only

Simbol - simbol yang ada menunjukkan jenis parameter dengan cara meneruskan argumen ke fungsi
String Dokumentasi

Baris pertama diharuskan untuk selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Jika ada lebih banyak baris dalam string dokumentasi, baris kedua diharuskan kosong, tujuannya ialah untuk memisahkan ringkasan secara visual dari deskripsi.
