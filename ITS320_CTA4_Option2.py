print ('')
print ('Grade Statistics App')
print ('This python program is designed to provide a minimum, maximum',end ='')
print ('and average score out of 5 students in a class\n')

def main():
    scores = get_scores()
    total = get_total(scores)
    average = total/len(scores)
    my_list = [get_scores]
    print('Lowest score: ', min(scores))
    print('Highest score: ', max(scores))
    print('Average score: ', average)

def get_scores():
    test_scores = []
    for scores in range(5):
        value = float(input('Enter score: '))
        test_scores.append(value)
    return test_scores

def get_total(value_list):
    total = 0.0
    for num in value_list:
        total += num
    return total

main()
