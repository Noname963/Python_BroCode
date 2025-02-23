# sort() method = used with lists
# sort() function = used with iterables

# students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))


# sorted_students = sorted(students,reverse=True)
grade = lambda grades:grades[2]
sorted_students = sorted(students,key=grade)

for i in sorted_students:
    print(i)