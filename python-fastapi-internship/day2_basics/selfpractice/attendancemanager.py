print("     ATTENDANCE REPORT")
student_name = "Sahad"
print(f"Student Name      : {student_name}")
attendance = [
    'P','P','A','P','P',
    'P','A','P','P','P',
    'P','A','P','P','P',
    'A','P','P','P','P'
]
total_days = len(attendance)
print(f"Total Days        : {total_days}")
present_days = sum(1 for day in attendance if day == 'P')
print(f"Days Present      : {present_days}")
attendance_percentage = (present_days / total_days) * 100
print(f"Attendance %      : {attendance_percentage:.2f}%")
if attendance_percentage < 75:
    print("Status            : Below 75% (Not Eligible)")
else:
    print("Status            : Eligible")