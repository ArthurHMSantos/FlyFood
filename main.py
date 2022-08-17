import time

initial_time = time.time()

matriz = open('Entrada.txt')
matrix = matriz.readlines()


class Address:
    def __init__(self, letter, tuple_coordinate):
        self.letter = letter
        self.tuple_coordinate = tuple_coordinate


address_set = []
r = Address("R", (0, 0))  # default position for R is 0, 0

count = 0
for row_index, item in enumerate(matrix):
    row = matrix[row_index].split()
    for column_index in range(len(row)):
        if row[column_index] == 'R':
            r.tuple_coordinate = (row_index, column_index)
        elif row[column_index] != '0':
            address_set.append(Address(row[column_index], (row_index, column_index)))
            count += 1


def permute_list(informed_list):
    if len(informed_list) == 0:
        return []
    if len(informed_list) == 1:
        return [informed_list]

    aux = []
    for index in range(len(informed_list)):
        chain = informed_list[index]
        remix = informed_list[:index] + informed_list[index + 1:]

        for unchained in permute_list(remix):
            aux.append([chain] + unchained)
    return aux


def get_total_distance(informed_distance_list):
    total = 0
    for distance in informed_distance_list:
        total += distance
    return total


def get_distance_list_from_coordinates(address_sequence):
    temp = []

    for i in range(len(sequence) - 1):
        first_tuple = address_sequence[i].tuple_coordinate
        second_tuple = address_sequence[i + 1].tuple_coordinate

        d1 = abs(first_tuple[0] - second_tuple[0])
        d2 = abs(first_tuple[1] - second_tuple[1])
        distance_result = (d1 + d2)
        temp.append(distance_result)
    return temp


permuted_list = permute_list(address_set)

for permutation in permuted_list:
    permutation.insert(0, r)
    permutation.append(r)

media = 0
results_list = []
for sequence in permuted_list:
    distance_list = get_distance_list_from_coordinates(sequence)
    result = get_total_distance(distance_list)
    media += result
    results_list.append(result)


min_distance_index = 0
for distance_index in range(len(results_list)):
    if results_list[distance_index] < results_list[min_distance_index]:
        min_distance_index = distance_index


def show(informed_list):
    minimum = ""
    for address in informed_list[min_distance_index]:
        minimum += str(address.letter)
    return minimum


print(f"The shortest path is {show(permuted_list)} with {results_list[min_distance_index]} distance.")

final_time = time.time()

execution_time = final_time - initial_time
print(f'Execution time was {execution_time} seconds for {count} instances')
