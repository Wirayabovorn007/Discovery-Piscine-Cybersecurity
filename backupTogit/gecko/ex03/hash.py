import hashlib
import itertools

words = ['liam', '42', 'barcelona', 'up2u', '1978', 'lion', 'spain', 'hacking']
target_hash = 'c967d488512ab5559b446f97843de1be0d615088'

for r in range(1, len(words) + 1):
    for combo in itertools.permutations(words, r):
        candidate = ''.join(combo)  # ต่อคำแบบไม่มีเว้นวรรค
        hashed = hashlib.sha1(candidate.encode()).hexdigest()
        if hashed == target_hash:
            print(f'พบรหัสผ่าน! → {candidate}')
            exit()

print("ไม่พบคำที่ตรงกัน")