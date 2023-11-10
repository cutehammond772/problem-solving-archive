import sys
input = lambda: sys.stdin.readline().rstrip()

grades = {
	'A+': 4.5,
	'A0': 4.0,
	'B+': 3.5,
	'B0': 3.0,
	'C+': 2.5,
	'C0': 2.0,
	'D+': 1.5,
	'D0': 1.0,
	'F': 0.0
}

if __name__ == '__main__':
	total_credits = 0.0
	total_grades = 0.0

	for _ in range(20):
		course, credit, grade = input().split()

		if grade == 'P':
			continue

		total_credits += float(credit)
		total_grades += float(credit) * grades[grade]

	print(total_grades / total_credits)
