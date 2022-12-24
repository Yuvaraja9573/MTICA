student=[[66,'yuvaraj',77,90],[2,'roy',80,90],[43,'pradeep',75,85],[52,'praveen',80,75]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
student.sort(key=lambda temp:temp[3])






