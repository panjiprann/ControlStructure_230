def evaluate_performance(percentage):
   
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below Average performance"
percentage = float(input("masukkan nilai presentase: "))
print(evaluate_performance(percentage))

def find_largest(a, b, c):
  
    return max(a, b, c)
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
print("angka terbesar:", find_largest(a, b, c))

def print_fibonacci(n):
   
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()  # For a newline after the series
n = int(input("Masukkan nomor dalam seri Fibonacci: "))
print_fibonacci(n)

def print_odd_numbers(n):
    
    for i in range(1, n + 1, 2): 
        print(i, end=" ")
    print() 
n = int(input("masukkan angka ganjil: "))
print_odd_numbers(n)

def print_design(n):
    
    for i in range(1, n + 1):
        print((str(i) + ' ') * i)  
n = int(input("masukkan jumlah baris: "))
print_design(n)