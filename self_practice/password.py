
from werkzeug.security import generate_password_hash, check_password_hash

print(generate_password_hash('Aaa123400'))
# pbkdf2:sha256:150000$A8MS1NBV$981e4e95eec5683d4a473fab30c0bcacdc45f1c9f3b45cde3e3f22541c092541