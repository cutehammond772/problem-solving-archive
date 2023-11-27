# [Platinum I] Mosaic - 4112 

[문제 링크](https://www.acmicpc.net/problem/4112) 

### 성능 요약

메모리: 34952 KB, 시간: 56 ms

### 분류

비트마스킹, 다이나믹 프로그래밍, 비트필드를 이용한 다이나믹 프로그래밍

### 제출 일자

2023년 11월 27일 19:44:30

### 문제 설명

<p>An architect wants to decorate one of his buildings with a long, thin mosaic. He has two kinds of tiles available to him, each 2 inches by 2 inches:</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/4112/1.png" style="height:100px; width:271px"></p>

<p>He can rotate the second kind of tile in any of four ways. He wants to fill the entire space with tiles, leaving no untiled gaps. Now, he wonders how many different patterns he can form. He considers two mosaics to be the same only if they have exactly the same kinds of tiles in exactly the same positions. So, if a rotation or a reflection of a pattern has tiles in different places than the original, he considers it a different pattern. The following are examples of 4” x 16” mosaics, and even though they are all rotations or reflections of each other, the architect considers them to be four different mosaics:</p>

<p><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/4112/2.png" style="height:162px; width:544px"></p>

### 입력 

 <p>There will be several test cases. Each test case will consist of two integers on a single line, N and M (2 ≤ N ≤ 10, 2 ≤ M ≤ 500). These represent the dimensions of the strip he wishes to fill, in inches. The data set will conclude with a line with two 0's.</p>

### 출력 

 <p>For each test case, print out a single integer representing the number of unique ways that the architect can tile the space, modulo 10<sup>6</sup>. Print each integer on its own line, with no extra whitespace. Do not print any blank lines between answers.</p>

