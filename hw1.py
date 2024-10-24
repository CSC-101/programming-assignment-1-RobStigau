import data
import math
# Write your functions for each part in the space below.

# Part 1
def vowel_count(vowel : str) -> int:
    count = 0
    vowel.lower()
    word_list = list(vowel)
    for item in word_list:
        if item == 'a' or item == 'e' or item == 'i' or item == 'u' or item == 'o':
            count += 1
    print(count)
    return count



# Part 2
def shorts_lists(lists):
    new_list = []
    for item in lists:
        if type(item) is list:
            if len(item) == 2:
                for x in item:
                    new_list.append(x)
            else:
                continue
        else:
            continue
    return new_list




# Part 3
def ascending_pairs(lists):
    new_list = []
    for item in lists:
        if len(item) == 2:
            item.sort()
            for x in item:
                new_list.append(x)

        else:
            for x in item:
                new_list.append(x)
    return new_list



# Part 4
def add_prices(price1 : data.Price, price2 : data.Price):
    added_cents = price1.cents + price2.cents
    added_dollars = price1.dollars + price2.dollars
    if added_cents < 100:
        return data.Price(added_dollars, added_cents)
    else:
        return data.Price(added_dollars, added_cents - 100)




# Part 5
def rectangle_area(rectangle : data.Rectangle):
    topx = rectangle.top_left.x
    topy = rectangle.top_left.y
    bottomx = rectangle.bottom_right.x
    bottomy = rectangle.bottom_right.y
    lengthx = abs(topx - bottomx)
    lengthy = abs(topy - bottomy)
    area = lengthx * lengthy
    return area


# Part 6
def books_by_author(authname : str, books : list[data.Book]) -> list[data.Book]:
    book_list = []
    authnames = [str(authname)]
    for book in books:
        if authnames == book.authors:
            book_list.append(data.Book(book.authors, book.title))
        else:
            continue
    return book_list

# Part 7
def circle_bound(rectangle : data.Rectangle) -> data.Circle:
    deltax = (abs(rectangle.top_left.x - rectangle.bottom_right.x))/2
    deltay = (abs(rectangle.top_left.y - rectangle.bottom_right.y))/2
    distcorner = math.sqrt(deltax**2 + deltay**2)
    center = data.Point(deltax, deltay)
    return data.Circle(center, distcorner)


# Part 8
def below_pay_average(employee_list : list[data.Employee]) -> list[str]:
    avg = 0
    employee_new_list = []
    if len(employee_list) == 0:
        print("inputted employee list was empty")
        return employee_new_list
    for employee in employee_list:
        avg += employee.pay_rate
    avg = avg/len(employee_list)
    for employee in employee_list:
        if employee.pay_rate < avg:
            employee_new_list.append(employee.name)
        else:
            continue
    return employee_new_list





