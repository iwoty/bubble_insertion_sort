
import csv


def read_data(amount_data):
    """
    Implement a function read_data which takes an amount of data and returns list of numbers
    from appropriate file (name of file indicates an amount of numbers).

    Parameters
    ----------
    amount_data : int

    Returns
    -------
    None
    """
    possible_amount = {1000: 'one_thousand',
                       10000: 'ten_thousand',
                       50000: 'fifty_thousand',
                       100000: 'one_hundred_thousand',
                       500000: 'five_hundred_thousand',
                       1000000: 'one_million',
                       3000000: 'three_millions'}
    try:
        path_to_file = ('/home/iwotyszkowski/codecool/python/bubble_insertion_sort/data_to_sort/'
                        + possible_amount[amount_data] + '.csv')
        with open(path_to_file, 'r') as f:
            reader = csv.reader(f, delimiter=',')
            numbers = []
            for row in reader:
                numbers.append(int(row[0]))     # [0] beacause csv has column in every row -it would create nested list
        return numbers
    except FileNotFoundError:
        return '(FileNotFoundError) Missing file.'
    except KeyError:
        return '(KeyError) There is no such thing to sort.'


def save_data(numbers):
    """
    Implement a function save_data which takes a list of (sorted)
    numbers and create an .csv file with prefix: "sorted_" in the package sorted_data.

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    None

    """
    pass


def bubble_sort(numbers):
    """
    Implement a function bubble_sort, which takes a list of numbers to sort and returns list of sorted numbers.
    Implement a bubble sort algorithm by yourself based on your flowchart.

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int

    """
    '''
    for i in numbers:
        for j in range(1, len(numbers)):    # i-1 so begin from 2nd element
            if numbers[j-1] > numbers[j]:
                numbers.insert(j, numbers.pop(j-1))
    return numbers
    '''
    '''
    length = len(numbers)
    for i in range(length):
        for j in range(1, len(numbers)):    # i-1 so begin from 2nd element
            if numbers[j-1] > numbers[j]:
                numbers.insert(j, numbers.pop(j-1))
        length -= 1
    return numbers
    '''
    '''
    n = length(A)
    repeat until n = 0
        newn = 0
        for i = 1 to n-1 inclusive do
            if A[i-1] > A[i] then
                swap(A[i-1], A[i])
                newn = i
        n = newn
    '''
    '''
    n = len(numbers)
    while n != 0:
        newn = 0
        for i in range(1, n):
            if numbers[i-1] > numbers[i]:
                numbers.insert(i, numbers.pop(i-1))
                newn = i
        n = newn
    return numbers
    '''

    for passnum in range(len(numbers)-1,0,-1):
        for i in range(passnum):
            if numbers[i]>numbers[i+1]:
                temp = numbers[i]
                numbers[i] = numbers[i+1]
                numbers[i+1] = temp


def insertion_sort(numbers):
    """
    Implement a function insertion_sort, which takes a list of numbers to sort and returns list of sorted numbers.
    Implement an insertion sort algorithm by yourself based on your flowchart.

    Parameters
    ----------
    numbers : list of int

    Returns
    -------
    list of int
    """
    pass


def sort_data(amount_data, sort_type='bubble'):
    """
    Implement a function sort_data which takes a type of sorting ('bubble' or 'insertion')
    and amount of numbers to sort and returns sorted numbers in list. Sort_type is a default parameter.

    Parameters
    ----------
    sort_type : string, optional
    amount_data : int

    Returns
    -------
    list of int
    """
    pass


def get_computing_time(amount_data, computing_type='import data'):
    """

    * Implement a function get_computing_time which takes a type of computing
    ('import data', 'export data', 'bubble sort' or 'insertion sort') and an amount of data and returns a time
    of computing in milliseconds.

    Parameters
    ----------
    computing_type : string, optional
    amount_data : int

    Returns
    -------
    int
    """
    pass


def print_computing_summary(computing_data):
    """
    *Implement a function print_sort_summary which prints in board the comparison of computing time for
    all amounts of data. Function takes a dictionary with data about computing.
    The key is a tuple with of string computing_type and integer amount_data, the value is an integer computing_time.
    The following picture shows a piece of the example board:

    Parameters
    ----------
    computing_data : dict : { key : tuple of string, value : int }

    Returns
    -------
    None
    """
    pass


def main():
    # print(read_data(10000))
    # print(bubble_sort())
    bubble_sort(read_data(1000)))

if __name__ == '__main__':
    main()
