import matplotlib.pyplot as plt
import seaborn as sns

# Cek spesifikasi modul
print(plt.__spec__)
print(sns.__spec__)

# Membuat contoh visualisasi sederhana
sns.set_theme()
data = [1, 2, 3, 4, 5]
plt.plot(data)
plt.show()