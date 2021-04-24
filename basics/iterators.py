def zipping():
    people = ['Alice', 'Bob', 'Eva', 'Tom']
    ages = [29, 30, 34, 36]
    nationalities = ['Canada', 'US', 'South Africa', 'England']
    for person, age, nationality in zip(people, ages, nationalities):
        print(person, age, nationality)


def main():
    zipping()


if __name__ == '__main__':
    main()