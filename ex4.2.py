students = 1200
rooms = 20
teachers = 20
students_room = 30
students_teacher = 30
req_rooms = students / rooms
avl_rooms = students / students_room

req_teachers = students / teachers
avl_teachers = students / students_teacher
 
print "Required number of rooms are", req_rooms , "but available rooms are", avl_rooms 
print "Required number of teachers are", req_teachers, "but available teachers are", avl_teachers
