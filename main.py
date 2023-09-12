user_list = []
total_ocupado = 0.0
counter = 1


def byte_to_mb(bytes):
    return round(float(bytes) / (1024 ** 2), 2)


def calc_porcentagem(numero, total):
    return round(numero / total * 100, 2)


try:
    with open('users.txt', 'r') as fhand:
        for line in fhand:
            try:
                name = line[:15]
                size = byte_to_mb(line[15:])
                new_user = {'n': counter, 'name': name, 'size': size}
                total_ocupado += new_user['size']
                user_list.append(new_user)
                counter += 1
            except ValueError as e:
                print(f"Error processing line {counter}: {e}")

    media_ocupado = round(total_ocupado / len(user_list),2)

    with open('relatorio.txt', 'w') as fhand:
        fhand.write('''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso

''')

        for user in user_list:
            user['%'] = calc_porcentagem(user['size'],total_ocupado)
            fhand.write(f"{user['n']:<5}{user['name']}{user['size']:<7}{'  MB':<10}{user['%']:>10}%\n")

        fhand.write(f"\nEspaço total ocupado: {total_ocupado} MB\n")
        fhand.write(f"Espaço médio ocupado: {media_ocupado} MB")

except FileNotFoundError:
    print("The 'users.txt' file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
