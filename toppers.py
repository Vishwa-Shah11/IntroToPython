scores_dataset = [
  {'SeqNo': 1, 'Name': 'Devika', 'Gender': 'F', 'City': 'Bengaluru', 'Mathematics': 64, 'Physics': 48, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 88, 'History': 43, 'Civics': 78, 'Philosophy': 55}, 
  {'SeqNo': 2, 'Name': 'Vishwa', 'Gender': 'F', 'City': 'Pune', 'Mathematics': 98, 'Physics': 73, 'Chemistry': 85, 'Biology': 66, 'Computer Science': 99, 'History': 78, 'Civics': 87, 'Philosophy': 89},
  {'SeqNo': 3, 'Name': 'Kunj', 'Gender': 'M', 'City': 'Bengaluru', 'Mathematics': 99, 'Physics': 98, 'Chemistry': 89, 'Biology': 86, 'Computer Science': 98, 'History': 76, 'Civics': 78, 'Philosophy': 74},
  {'SeqNo': 4, 'Name': 'Sandip', 'Gender': 'M', 'City': 'Vadodara', 'Mathematics': 72, 'Physics': 75, 'Chemistry': 79, 'Biology': 75, 'Computer Science': 89, 'History': 76, 'Civics': 98, 'Philosophy': 88},
  {'SeqNo': 5, 'Name': 'Sonal', 'Gender': 'F', 'City': 'Anand', 'Mathematics': 98, 'Physics': 67, 'Chemistry': 87, 'Biology': 66, 'Computer Science': 87, 'History': 89, 'Civics': 76, 'Philosophy': 77}]
my_dict = {}

def get_toppers(scores_dataset, subject, gender):
    toppers = []

    for i in scores_dataset:
        if (i['Gender'] == gender):
            my_dict[i['Name']] = i[subject]
            my_dict.update(my_dict)

            max_marks = max(zip(my_dict.values(), my_dict.keys()))[0]
            #return max_marks
            #print(max_marks)

    for i in my_dict.items():
        if (i[1] == max_marks):
            toppers.append(i[0])
    return toppers
    #print(toppers)

print(get_toppers(scores_dataset, 'Mathematics', 'M'))