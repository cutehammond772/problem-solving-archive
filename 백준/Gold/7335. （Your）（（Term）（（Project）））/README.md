# [Gold IV] (Your)((Term)((Project))) - 7335 

[문제 링크](https://www.acmicpc.net/problem/7335) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

파싱, 문자열, 트리

### 제출 일자

2023년 12월 6일 12:04:59

### 문제 설명

<p>You have typed the report of your term project in your personal computer. There are several one line arithmetic expressions in your report. There is no redundant parentheses in the expressions (omitting a pair of redundant matching parentheses does not change the value of the expression). In your absence, your little brother inserts some redundant matching parentheses in the expressions of your report. Assume that the expressions remain syntactically correct and evaluate to their original value (the value before inserting redundant parentheses). To restore your report to its original form, you are to write a program to omit all redundant parentheses.</p>

<p>To make life easier, consider the following simplifying assumptions:</p>

<ol>
	<li>The input file contains a number of expressions, each in one separate line.</li>
	<li>Variables in the expressions are only single uppercase letters.</li>
	<li>Operators in the expressions are only binary ‘+’ and binary ‘-’.</li>
</ol>

<p>Note that the only transformation allowed is omission of redundant parentheses, and no algebraic simplification is allowed.</p>

### 입력 

 <p>The input file consists of several test cases. The first line of the file contains a single number M, which is the number of test cases (1 ≤ M ≤ 10). Each of the following M lines, is exactly one correct expression. There may be arbitrarily space characters in each line. The length of each line (including spaces) is at most 255 characters.</p>

### 출력 

 <p>The output for each test case is the same expression without redundant parentheses. Notice that the order of operands in an input expression and its corresponding output should be the same. Each output expression must be on a separate line. Space characters should be omitted in the output expressions.</p>

