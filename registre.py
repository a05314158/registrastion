import json
import hashlib
import tkinter as tk
from tkinter import messagebox


bg_color = '#2b2d42'
text_color = '#8d99ae'
button_bg_color = '#ef233c'
button_text_color = '#edf2f4'
button_disabled_color = '#d90429'

def create_users_json(users_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(users_data, file, indent=4)

def hash_password(password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

def load_users_from_json(file_path):
    with open(file_path, 'r') as file:
        users_data = json.load(file)
    return users_data

def check_password(username, password, users_data):
    if username in users_data:
        stored_password = users_data[username]['password']
        entered_password_hashed = hash_password(password)
        if stored_password == entered_password_hashed:
            return True
    return False

def on_login():
    username = entry_username.get()
    password = entry_password.get()

    if check_password(username, password, users_data):
        messagebox.showinfo("Успех", "Вход выполнен успешно!")
        button_next.config(state=tk.NORMAL, bg='#ff0000')  # Изменение цвета и активации кнопки "Далее"
        root.destroy()  # Закрытие окна после нажатия кнопки "Далее"
    else:
        messagebox.showerror("Ошибка", "Неверный логин или пароль.")

def on_register():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        hashed_password = hash_password(password)
        users_data[username] = {"password": hashed_password}
        create_users_json(users_data, 'users.json')
        messagebox.showinfo("Успех", "Регистрация выполнена успешно!")
    else:
        messagebox.showerror("Ошибка", "Введите логин и пароль.")

# Создание пользователей и хешированных паролей
users_data = {
    "user1": {
        "password": hash_password("password1")
    },
    "user2": {
        "password": hash_password("password2")
    }
}
create_users_json(users_data, 'users.json')

# Загрузка пользователей из JSON файла
users_data = load_users_from_json('users.json')

# Создание графического интерфейса
root = tk.Tk()
root.title("Вход в систему")
root.configure(bg=bg_color)

label_username = tk.Label(root, text="Логин:", bg=bg_color, fg=text_color, font=('Arial', 12))
label_username.pack()
entry_username = tk.Entry(root, font=('Arial', 12))
entry_username.pack()

label_password = tk.Label(root, text="Пароль:", bg=bg_color, fg=text_color, font=('Arial', 12))
label_password.pack()
entry_password = tk.Entry(root, show="*", font=('Arial', 12))
entry_password.pack()

button_login = tk.Button(root, text="Войти", command=on_login, bg=button_bg_color, fg=button_text_color, font=('Arial', 12))
button_login.pack()

button_register = tk.Button(root, text="Регистрация", command=on_register, bg=button_bg_color, fg=button_text_color, font=('Arial', 12))
button_register.pack()

button_next = tk.Button(root, text="Далее", state=tk.DISABLED, bg=button_disabled_color, fg=button_text_color, font=('Arial', 12))
button_next.pack()

root.mainloop()
