# [Gold I] Street Checkers - 23943 

[문제 링크](https://www.acmicpc.net/problem/23943) 

### 성능 요약

메모리: 210028 KB, 시간: 9212 ms

### 분류

수학, 정수론, 소수 판정, 에라토스테네스의 체

### 제출 일자

2023년 11월 8일 12:51:28

### 문제 설명

<p>Alice and Bob are playing a new virtual reality team game - Street Checkers. The game is set on an insanely long street divided into tiles which are numbered from 0 to 10<sup>9</sup>(inclusive of both). At the start of the game, Alice and Bob are standing on tile number 0 and are given a random number X in range [<b>L</b>, <b>R</b>] (both ends are inclusive). Alice only jumps to odd numbered tiles, while Bob only jumps to even numbered tiles. If the number on the tile divides X, then the player landing on it has to color it with their favorite color. The game is over after tile X has been colored.</p>

<p>A game is considered interesting by both the players if the absolute difference between the number of tiles painted by each is not greater than 2. Help Alice and Bob find how many numbers in the interval [<b>L</b>, <b>R</b>] could make for an interesting game.</p>

### 입력 

 <p>The first line of the input gives the number of test cases, <b>T</b>. <b>T</b> lines follow each containing two integers <b>L</b> and <b>R</b>, the start and end of the interval used to generate the random number X.</p>

### 출력 

 <p>For each test case, output one line containing <code>Case #x: y</code>, where <code>x</code> is the test case number (starting from 1) and <code>y</code> is the count of numbers in interval [<b>L</b>, <b>R</b>] which results in an interesting game for Alice and Bob.</p>

