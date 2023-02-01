from random import choices


def get_data(name):
    with open(name, 'rt', encoding='utf-8') as file:
        data = [item.strip() for item in file.readlines()]
        return choices(data, k=3)


file_1, file_2 = 'first_names.txt', 'last_names.txt'

first_names, last_names = get_data(file_1), get_data(file_2)

# with open('first_names.txt', 'rt', encoding='utf-8') as first:
#     data = [name.strip() for name in first.readlines()]
#     first_names = choices(data, k=3)
#
# with open('last_names.txt', 'rt', encoding='utf-8') as last:
#     data = [name.strip() for name in last.readlines()]
#     last_names = choices(data, k=3)

for i in range(len(first_names)):
    print(f'{first_names[i]} {last_names[i]}')

'''  --- first_names.txt ---
Aaron
Abdul
Abe
Abel
Abraham
Abram
Bret
Brett
Brian
Brice
Britt
Brock
Broderick
Brooks
Bruce
Casey
Cecil
Cedric
Cedrick
Cesar
Chad
Darrin
Darron
Darryl
Darwin
Daryl
Dave
David
Davis
Dean
Emmett
Emmitt
Emory
Enoch
Enrique
Erasmo
Eric
Erich
Fred
Freddie
Freddy
Frederic
Frederick
Fredric
'''

''' --- last_names.txt ---
Torrence
Torres
Torrez
Toscano
Toth
Totten
Tovar
Towle
Townes
Towns
Townsend
Tracey
Tracy
Trahan
Trammell
Surratt
Sutherland
Sutter
Sutton
Swafford
Swain
Swan
Swank
Swann
Swanson
Swartz
Roland
Roldan
Roller
Rollins
Roman
Romano
Rome
Romeo
Romero
Romo
Roney
Rooney
Perez
Perkins
Perreault
Perrin
Perron
Perry
Perryman
Person
Peter
Peterman
Peters
'''