# help(str.split)
# split is to separate every element that you want using a specific str to add the limit
# split uses space by default

courses = 'Java python javascript angular excel'

coursesList = courses.split()
print(f'Courses list: {coursesList}')
"""
Courses list: ['Java', 'python', 'javascript', 'angular', 'excel']
"""
# from a string we are creating a list


courses_with_comma = 'Java,python,javascript,angular,excel'
coursesList = courses_with_comma.split(',')
print(f'Courses list: {coursesList}')

"""
Courses list using comma: ['Java', 'python', 'javascript', 'angular', 'excel']
"""