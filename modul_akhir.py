import numpy as np

nilai_latsol = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20LS.csv", delimiter=",", skiprows=1, dtype=(str))
nilai_kuis = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Kuis.csv", delimiter=",", skiprows=1, dtype=(str))
nilai_lab = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Lab.csv", delimiter=",", skiprows=1, dtype=(str))
nilai_proyek = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Proyek.csv", delimiter=",", skiprows=1, dtype=(str) )
nilai_jurnal = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Jurnal.csv", delimiter=",", skiprows=1, dtype=(str))
nilai_ujian = np.loadtxt("https://raw.githubusercontent.com/yozeftjandra/MATH2031/main/Penilaian%20MATH2031%20Angkatan%20XX%20-%20Ujian.csv", delimiter=",", skiprows=1, dtype=(str))
NIM = nilai_latsol[:, :1]

# [[70, 80, 70]       70*0.01 + 80*0.01 + 70*0.01        0.01(70+80+70)        [[2.2]
# [80, 80, 80]   -->  80*0.01 + 80*0.01 + 80*0.01   -->  0.01(80+80+80)   -->  [2.4]
# [90, 95, 100]]      90*0.01 + 95*0.01 + 100*0.01       0.01(90+95+100)       [2.85]]
total_latsol = np.reshape([sum(np.float_(nilai_baris))*0.01 for nilai_baris in nilai_latsol[:, 1:]], (len(nilai_latsol), 1))
total_kuis = np.reshape([sum(np.float_(nilai_baris))*0.02 for nilai_baris in nilai_kuis[:, 1:]], (len(nilai_latsol), 1))
total_lab = np.reshape([sum(np.float_(x))*0.04 for x in nilai_lab[:, 1:]], (len(nilai_latsol), 1))
total_proyek = np.reshape([sum(np.float_(x))*0.075 for x in nilai_proyek[:, 1:]], (len(nilai_latsol), 1))
total_jurnal = np.reshape([sum(np.float_(x))*0.03 for x in nilai_jurnal[:, 1:]], (len(nilai_latsol), 1))
total_ujian = np.reshape([sum(np.float_(x))*0.25 for x in nilai_ujian[:, 1:]], (len(nilai_latsol), 1))

total_nilai = np.block([total_latsol, total_kuis, total_lab, total_proyek, total_jurnal, total_ujian])
nilai_akhir = np.reshape([round(np.sum(x), 2) for x in total_nilai], (len(total_nilai), 1))


indeks_nilai = []
for nilai in nilai_akhir:
    if nilai >= 91:
        indeks_nilai.append("A")
    elif 86 <= nilai < 91:
        indeks_nilai.append("A-")
    elif 81 <= nilai < 86:
        indeks_nilai.append("B+")
    elif 76 <= nilai < 81:
        indeks_nilai.append("B")
    elif 71 <= nilai < 76:
        indeks_nilai.append("B-")
    elif 61 <= nilai < 71:
        indeks_nilai.append("C+")
    elif 51 <= nilai < 61:
        indeks_nilai.append("C")
    elif 46 <= nilai < 51:
        indeks_nilai.append("C-")
    elif 41 <= nilai < 46:
        indeks_nilai.append("D")
    elif nilai < 41:
        indeks_nilai.append("F")

indeks_prestasi = np.reshape(indeks_nilai, (len(nilai_latsol), 1))

print(np.mean(nilai_akhir)) # 64.0335
print(indeks_nilai.count("A")) # 0
print(indeks_nilai.count("F")) # 1

excel = np.block([NIM, nilai_akhir, indeks_prestasi])
np.savetxt("hasil.csv", excel, fmt="%s, %s, %s", header="NIM, Nilai Akhir, Indeks Prestasi", comments="")