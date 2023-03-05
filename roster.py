import random
employees = ['Abhishek', 'Siddhesh', 'Ashish', 'Rohit', 'Akshit', 'Siddhant', 'Rijo', 'Warke', 'Omkar_Kamble', 'Vipul', 'Bipin', 'Devendra', 'Madhan', 'Nagendra', 'Ragini', 'Venkatesh']
num_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
dict = {
        'Abhishek': 0, 
        'Ashish': 0,
        'Siddhesh': 0,
        'Rohit': 0,
        'Akshit': 0,
        'Siddhant': 0,
        'Rijo': 0,
        'Warke': 0,
        'Omkar_Kamble': 0,
        'Vipul': 0,
        'Bipin': 0,
        'Devendra': 0,
        'Madhan': 0,
        'Nagendra': 0,
        'Ragini': 0,
        'Venkatesh': 0
        } 
for day in num_days:
    for counter_check in dict:
        if dict[counter_check] >= 3:
            if counter_check in employees:
                employees.remove(counter_check)
    if day == "Wednesday":
        length = len(employees)
        print("Balance : " + str(length))
        print(employees)
        print('\n')
        daily_list = ((random.sample(employees,10)))
        for nm in daily_list:
            dict[nm] += 1
        print(day + " : ")
        print(daily_list)
    else:
        if day == "Thursday":
            length = len(employees)
            print("Balance : " + str(length))
            print(employees)
            print('\n')
            daily_list = ((random.sample(employees,11)))
            for nm in daily_list:
                dict[nm] += 1
            print(day + " : ")
            print(daily_list)
        else:
            length = len(employees)
            print("Balance : " + str(length))
            print(employees)
            print('\n')
            daily_list = ((random.sample(employees,9)))
            for nm in daily_list:
                dict[nm] += 1
            print(day + " : ")
            print(daily_list)
            print('\n')

print('\n')
print(dict)
