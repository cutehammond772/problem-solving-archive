# [Gold IV] Friends - 6579 

[문제 링크](https://www.acmicpc.net/problem/6579) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

자료 구조, 파싱, 스택, 문자열

### 제출 일자

2024년 2월 26일 00:06:24

### 문제 설명

<p>You want to plan a big birthday party with your friends. On planning you notice that you have to do a lot of operations with sets of friends. There is one group which consist of Arthur, Biene and Clemens. Then there is a group of friends you know from snowboarding which consists of Daniel, Ernst, Frida and Gustav. If you want to invite them both, the resulting party group consists of g1 + g2 (the result is the union of both groups). Then you can compute the intersection of the two groups g1 * g2, which consists of the empty set. Maybe you want to invite a group g1, but excluding all members of an other group g2, which is written as g1 - g2.</p>

<p>Intersection (*) has precedence over union (+) and set difference (-). All operations are left associative, which means that in A op<sub>1</sub> B op<sub>2</sub> C you first have to evaluate A op<sub>1</sub> B (provided op<sub>1</sub> and op<sub>2</sub> have equal precedence).</p>

### 입력 

 <p>The input consists of one or more lines. Each line contains one expression that you have to evaluate. Expressions are syntactically correct and only consist of the characters:</p>

<ul>
	<li>'{' and '}'</li>
	<li>the elements 'A' to 'Z' meaning friend Arthur to Zora.</li>
	<li>the operations '+', '-' and '*'</li>
	<li>'(' and ')' for grouping operations</li>
	<li>the newline character '\n' marking the end of an expression.</li>
</ul>

<p>A line is never longer than 255 characters.</p>

### 출력 

 <p>Output the resulting set in curly braces '{' and '}', each on a line of its own. Print elements of sets sorted alphabetically.</p>

