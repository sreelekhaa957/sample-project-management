# Simple 12-line grade calculator (each subject out of 100)
n = int(input("Number of subjects: "))
s = 0.0
print("Enter marks (0-100):")
for i in range(n):
    s += float(input(f" {i+1}: "))
p = s / n
g = "F" if p < 60 else ("D" if p < 70 else ("C" if p < 80 else ("B" if p < 90 else "A")))
print(f"Total: {s:.2f}/{n*100:.2f}")
print(f"Percent: {p:.2f}%")
print(f"Grade: {g}")
# end 
