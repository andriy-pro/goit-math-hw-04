import pandas as pd

# Таблиця істинності для висловлювання b)
# (A → (B ∨ C)) ∧ ((C ∧ B) → D)

# Визначення значень змінних A, B, C, D
A_arr = [0, 0, 0, 0, 1, 1, 1, 1]
B_arr = [0, 0, 1, 1, 0, 0, 1, 1]
C_arr = [0, 1, 0, 1, 0, 1, 0, 1]
D_arr = [0, 1, 0, 1, 0, 1, 0, 1]

# Обчислення B ∨ C
B_or_C_arr = [int(B or C) for B, C in zip(B_arr, C_arr)]

# Обчислення A → (B ∨ C)
A_implies_B_or_C_arr = [int(not A or B_or_C) for A, B_or_C in zip(A_arr, B_or_C_arr)]

# Обчислення C ∧ B
C_and_B_arr = [C and B for C, B in zip(C_arr, B_arr)]

# Обчислення (C ∧ B) → D
C_and_B_implies_D_arr = [
    int(not C_and_B or D) for C_and_B, D in zip(C_and_B_arr, D_arr)
]

# Обчислення (A → (B ∨ C)) ∧ ((C ∧ B) → D)
expression_b_arr = [
    A_implies_B_or_C and C_and_B_implies_D
    for A_implies_B_or_C, C_and_B_implies_D in zip(
        A_implies_B_or_C_arr, C_and_B_implies_D_arr
    )
]

# Створення таблиці істинності
df_b = pd.DataFrame(
    {
        "A": A_arr,
        "B": B_arr,
        "C": C_arr,
        "D": D_arr,
        "A → (B ∨ C)": A_implies_B_or_C_arr,
        "(C ∧ B) → D": C_and_B_implies_D_arr,
        "(A → (B ∨ C)) ∧ ((C ∧ B) → D)": expression_b_arr,
    }
)

# Вирівнювання значень у таблиці по центру
df_b_styled = df_b.style.set_properties(**{"text-align": "center"}).set_table_styles(
    [dict(selector="th", props=[("text-align", "center")])]
)

print("\nТаблиця істинності для висловлювання 'b':")
print(
    "“Якщо ми успішно виконаємо домашнє завдання з математичної логіки (A), то ми отримаємо заліковий бал (B) або візьмемо участь у науковому семінарі (C),"
)
print(
    "водночас якщо ми візьмемо участь у науковому семінарі (C) і отримаємо заліковий бал (B), то ми отримаємо стипендію (D)”"
)
print("(A → (B ∨ C)) ∧ ((C ∧ B) → D)")
print()
print(df_b_styled)
