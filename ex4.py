total_students = 1000
no_per_room = 35
no_teachers = 20
req_teachers = total_students/no_per_room
no_classes = total_students / no_teachers
req_classes = total_students / no_per_room
no_studentsperteacher = total_students / no_teachers 
no_illegal_classes = no_classes - req_classes
print no_illegal_classes
print no_studentsperteacher
print req_classes
print no_classes 
