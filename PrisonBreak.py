from csv import reader

# convert csv file to a readble file
read_file = list(reader(open('heli_prison_list.csv')))[1:]
for row in read_file:
    row[0] = int(row[0][-4:])


def list_of_occurence(file, x):
    """
    :param file: csv file
    :param x: occurence per x
    :return: list of occurence of the element located at the x index per row
    """
    attempts_per_x = {}
    for row in file:
        if row[x] not in attempts_per_x:
            attempts_per_x[row[x]] =  1
        else:
            attempts_per_x[row[x]] = attempts_per_x[row[x]] + 1
    return attempts_per_x
  

def list_of_success(f, x)-> dict:
      """
    :param file: csv file
    :param x: success per x
    :return: list of success of the element located at the x index per row
    """
    success_per_x = {}
    for row in f:
        if row[x] not in success_per_x:
            if row[3] == 'Yes':
                success_per_x[row[x]] = 1
            if row[3] == 'No':
                success_per_x[row[x]] = -1
        else:
            if row[3] == 'Yes':
                success_per_x[row[x]] = success_per_x[row[x]] + 1
            if row[3] == 'No':
                success_per_x[row[x]] = success_per_x[row[x]] - 1

    return success_per_x
  
  
def find_max_years(f: list)-> list:
    """ :return: find the year with maximum attempts """
    f = list_of_occurence(f, 0)
    mx = [max(f, key=f.get)]
    for key, value in f.items():
        if value == f[mx[0]] and key not in mx:
            mx.append(key)
    return mx


def find_max_countries(f: list) -> str:
    """ :return: find the country/s with maximum attempts """
    f = list_of_occurence(f, 2)
    mx = [max(f, key=f.get)]
    for key, value in f.items():
        if value == f[mx[0]] and key not in mx:
            mx.append(key)
    return ", ".join(mx)


def chances_of_success(f) -> list:
      """ :return: the country with the highest chance of success """
    suc_per_country = list_of_success(f, 2)
    att_per_country = list_of_occurence(f, 2)
    chances = {}

    for key, value in suc_per_country.items():
        for key2, value2 in att_per_country.items():
            if (key == key2 and key not in chances):
                chances[key] = (value/value2)*100

    mx = [[max(chances, key=chances.get)]]
    for key, value in chances.items():
        if value == chances[mx[0][0]] and key not in mx:
            mx.append([key,"{0}%".format(value)])

    return mx[1:]


def more_than_once(f):
        """ :return: the countries with prison breaks more than once  """
    f = list_of_occurence(f, 2)
    f_new = {}

    for key, value in f.items():
        if value > 1:
            f_new[key] = value

    return f_new
