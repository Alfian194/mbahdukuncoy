import random

# Kata-kata utama yang harus tetap ada
main_words = [
    "love", "trust", "future", "together",
    "heart", "dream", "vault", "security",
    "unlock", "eternal", "embrace", "balance",
    "life", "true", "smile", "happy"
]

# Kata tambahan yang akan diacak
shuffle_words = [
    "forever", "passion", "soulmate", "promise",
    "unity", "joy", "hope", "bliss"
]

# Fungsi untuk mengacak kata
def shuffle_phrase():
    random.shuffle(shuffle_words)  # Mengacak kata tambahan
    return main_words + shuffle_words  # Menggabungkan kata utama dan kata acakan

# Menampilkan 30 hasil acakan
for _ in range(30):
    shuffled_phrase = shuffle_phrase()
    print(" ".join(shuffled_phrase))  # Menampilkan hasil acakan
