passwords = []

for i in range(1, 1000):
    passwords.append(f"TrainingPass{i:04d}!")

passwords.append("Enterprise@7392")

with open("wordlist.txt", "w", encoding="utf-8") as file:
    for password in passwords:
        file.write(password + "\n")

print("Wordlist created!")
print("Total passwords:", len(passwords))
