from io_data import *


def main(file_in):
    number_of_humsters, amount_of_eat, hamsters_bst = input_data(file_in)

    checked_humsters = 0
    total_avarice = 0
    total_daily_norm = 0

    while checked_humsters < amount_of_eat:
        current = hamsters_bst.get_min_element()
        total_avarice += current.avarice
        total_daily_norm += current.daily_norm
        checked_humsters += 1

        if total_daily_norm + total_avarice * checked_humsters > number_of_humsters:
            break

        hamsters_bst.remove_min_element()
    return checked_humsters


if __name__ == "__main__":
    first_file_in = 'IO/hamster1.in'
    first_file_out = 'IO/hamster1.out'
    first_result = main(first_file_in)
    
    print(f'Hamsters result: {first_result}')

    output_data(first_file_out, str(first_result))
