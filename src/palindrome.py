from time import perf_counter


def is_palindrome_new(word):
    return word == word[::-1]


def compare_functions(word):
    print(f"\nMot à tester: {word}")

    start_time = perf_counter()
    is_palindrome_new(word)
    end_time = perf_counter()
    new_time = end_time - start_time

    start_time = perf_counter()
    is_palindrome(word)
    end_time = perf_counter()
    loop_time = end_time - start_time

    print(f"New: {new_time}")
    print(f"Loop: {loop_time}")
    print(f"Différence (loop - reverse): {loop_time - new_time}")


compare_functions("coucou")
compare_functions("kayak")
compare_functions("jepensequecemotnestpasunpalindrome")
