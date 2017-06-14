students = 1200
rooms = 20
teachers = 20
students_room = 30
students_teacher = 30
req_rooms = students / rooms
avl_rooms = students / students_room

req_teachers = students / teachers
avl_teachers = students / students_teacher
 
print "Required number of rooms are %s but available rooms are %s" %(req_rooms, avl_rooms) #respective %s will be equal to respective value in the paranthesis)
print "Required number of teachers are %d but available teachers are %d" %(req_teachers,avl_teachers)
print "Deficit number of teachers are %d Deficit number of rooms are %d" %(req_rooms - avl_rooms, req_teachers - avl_teachers)
