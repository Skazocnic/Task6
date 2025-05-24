def is_lucky_ticket(ticket_number):
    length = len(ticket_number)
    if length % 2 != 0:
        return False

    half = length // 2
    first_half = ticket_number[:half]
    second_half = ticket_number[half:]

    sum_first = sum(int(digit) for digit in first_half)
    sum_second = sum(int(digit) for digit in second_half)

    return sum_first == sum_second

number = input("Введите номер билета: ")

print(is_lucky_ticket(number))