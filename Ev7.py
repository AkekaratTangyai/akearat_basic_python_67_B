# สร้างรายการของหมายเลขในช่วง 21-40
numbers = range(21, 41)

# แยกหมายเลขเป็นจำนวนคี่และจำนวนคู่
odd_numbers = [num for num in numbers if num % 2 != 0]
even_numbers = [num for num in numbers if num % 2 == 0]

# แสดงผลลัพธ์
print("Odd numbers:", odd_numbers)
print("Even numbers:", even_numbers)
