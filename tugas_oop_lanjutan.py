# ================================================================
# TUGAS OOP LANJUTAN
# ================================================================


# ================================================================
# BAGIAN 1 — Class Restaurant
# ================================================================
# Kelas    : Restaurant
# State    : restaurant_name, cuisine_type, number_served
# Behavior : __init__(), describe_restaurant(), open_restaurant()
#            set_number_served(), increment_number_served()
# ================================================================

class Restaurant:
    """Kelas yang merepresentasikan sebuah restoran."""

    def __init__(self, restaurant_name, cuisine_type):
        """Menginisialisasi atribut restoran."""
        self.restaurant_name = restaurant_name  # STATE
        self.cuisine_type    = cuisine_type     # STATE
        self.number_served   = 0               # STATE — default 0

    def describe_restaurant(self):             # BEHAVIOR
        """Mencetak informasi ringkasan restoran."""
        print(f"  Nama Restoran : {self.restaurant_name}")
        print(f"  Jenis Masakan : {self.cuisine_type}")

    def open_restaurant(self):                 # BEHAVIOR
        """Mencetak pesan bahwa restoran sedang buka."""
        print(f"  {self.restaurant_name} sedang BUKA. Selamat datang!")

    def set_number_served(self, number):       # BEHAVIOR
        """Mengatur jumlah pelanggan ke nilai tertentu."""
        if number >= 0:
            self.number_served = number
            print(f"  Jumlah pelanggan diatur menjadi : {self.number_served}")
        else:
            print("  ERROR: Jumlah pelanggan tidak boleh negatif.")

    def increment_number_served(self, increment):  # BEHAVIOR
        """Menambah jumlah pelanggan yang telah dilayani."""
        self.number_served += increment
        print(f"  +{increment} pelanggan dilayani.")
        print(f"  Total pelanggan sekarang : {self.number_served}")


# ================================================================
# BAGIAN 2 — Class User
# ================================================================
# Kelas    : User
# State    : first_name, last_name, username, email, age, city,
#            login_attempts
# Behavior : __init__(), describe_user(), greet_user()
#            increment_login_attempts(), reset_login_attempts()
# ================================================================

class User:
    """Kelas yang merepresentasikan seorang pengguna."""

    def __init__(self, first_name, last_name, username, email, age, city):
        """Menginisialisasi atribut profil pengguna."""
        self.first_name     = first_name  # STATE
        self.last_name      = last_name   # STATE
        self.username       = username    # STATE
        self.email          = email       # STATE
        self.age            = age         # STATE
        self.city           = city        # STATE
        self.login_attempts = 0           # STATE — default 0

    def describe_user(self):              # BEHAVIOR
        """Mencetak ringkasan informasi pengguna."""
        print(f"  Nama Lengkap   : {self.first_name} {self.last_name}")
        print(f"  Username       : {self.username}")
        print(f"  Email          : {self.email}")
        print(f"  Usia           : {self.age} tahun")
        print(f"  Kota           : {self.city}")
        print(f"  Login Attempts : {self.login_attempts}")

    def greet_user(self):                 # BEHAVIOR
        """Mencetak salam pribadi kepada pengguna."""
        print(f"  Halo, {self.first_name} {self.last_name}!"
              f" Selamat datang kembali, @{self.username}!")

    def increment_login_attempts(self):   # BEHAVIOR
        """Menambah login_attempts sebesar 1 setiap dipanggil."""
        self.login_attempts += 1
        print(f"  Login attempt ke-{self.login_attempts} tercatat.")

    def reset_login_attempts(self):       # BEHAVIOR
        """Mengatur ulang login_attempts menjadi 0."""
        self.login_attempts = 0
        print(f"  Login attempts direset menjadi : {self.login_attempts}")


# ================================================================
# BAGIAN 3 — Program Utama
# ================================================================

# ---------------------------------------------------------------
# SOAL 1 — Restaurant & number_served
# ---------------------------------------------------------------
print("=" * 55)
print("  SOAL 1 — Restaurant & Jumlah Pelanggan")
print("=" * 55)

# Membuat instance restaurant
restaurant = Restaurant("Warung Pak Budi", "Masakan Padang")
restaurant.describe_restaurant()

# [1] Cetak jumlah pelanggan awal (default 0)
print(f"\n  [1] Jumlah pelanggan awal          : {restaurant.number_served}")

# [2] Ubah nilai secara langsung lalu cetak lagi
restaurant.number_served = 30
print(f"  [2] Jumlah pelanggan (ubah langsung) : {restaurant.number_served}")

# [3] Gunakan set_number_served() untuk mengatur nilai baru
print()
restaurant.set_number_served(100)   # [3]

# [4] Gunakan increment_number_served() untuk menambah pelanggan harian
print()
restaurant.increment_number_served(45)  # [4]


# ---------------------------------------------------------------
# SOAL 2 — User & login_attempts
# ---------------------------------------------------------------
print("\n" + "=" * 55)
print("  SOAL 2 — User & Login Attempts")
print("=" * 55)

# Membuat instance user
user1 = User("Andi", "Saputra", "andi_sptr", "andi@email.com", 22, "Jakarta")

# [1] Tampilkan profil awal
print("\n  [Profil Awal]")
user1.describe_user()

# [2] Panggil increment beberapa kali
print("\n  [Simulasi Percobaan Login]")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

# [3] Cetak untuk memastikan nilai bertambah benar
print(f"\n  Total login_attempts sekarang : {user1.login_attempts}")

# [4] Reset login attempts
print()
user1.reset_login_attempts()

# [5] Cetak untuk memastikan nilai sudah 0
print(f"  login_attempts setelah reset  : {user1.login_attempts}")

print("\n" + "=" * 55)
