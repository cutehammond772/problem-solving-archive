# [Diamond IV] Palindromic DNA - 3849 

[문제 링크](https://www.acmicpc.net/problem/3849) 

### 성능 요약

메모리: 19248 KB, 시간: 2260 ms

### 분류

2-sat, 자료 구조, 분리 집합, 그래프 이론, 강한 연결 요소

### 문제 설명

<p>A DNA sequence is composed of a series of four possible nucleobases, namely Adenine, Guanine, Thymine and Cytosine; we will refer to each of these bases by their initial. For our purposes, nucleobases have an associated cyclic “order”: A is followed by G, which in turn is followed by T, which is followed by C, which is followed by A again. State-of-the-art research in genomics has revealed the startling fact that many diseases are caused by certain subsequences of bases not forming a palindromic sequence! Your mission as a leading researcher at ICPC laboratories is to take a DNA string S and a series of subsets P<sub>1</sub>, ... , P<sub>t</sub> of indices to characters (nucleobases) in S, and transform S so that each of the restrictions of the resulting string to P<sub>1</sub>, ... , P<sub>t</sub> are palindromic. (The restriction of S to a subset P = {i<sub>1</sub>, i<sub>2</sub>, ... , i<sub>k</sub>} of indices, where 0 ≤ i<sub>1</sub> < i<sub>2</sub> < . . . < i<sub>k</sub> < |S|, is the string S<sub>i<sub>1</sub></sub> S<sub>i<sub>2</sub></sub> ... S<sub>i<sub>k</sub></sub>). It is possible to inspect any base of S at will, but only three transformations can be applied to a base:</p>

<ol>
	<li>Leave it unaltered.</li>
	<li>Increase it by 1 in the cyclic order of nucleobases (e.g. turn C into A).</li>
	<li>Decrease it by 1 (e.g. turn T into G).</li>
</ol>

<p>Moreover, owing to limitations of current technology, it is impossible to modify two bases in consecutive positions of the sequence. Is our goal achievable?</p>

<p>By way of example, consider DNA sequence AGTAT. Number positions starting from 0, and suppose we have the three subsets P<sub>1</sub> = {1, 4}, P<sub>2</sub> = {0, 1} and P<sub>3</sub> = {0, 2, 4}. One solution is to increase the first character and decrease the last, yielding S' = GGTAG. The restrictions of S' to P<sub>1</sub>, P<sub>2</sub> and P<sub>3</sub> are GG, GG and GTG, respectively; all of them are palindromic.</p>

<p>One case where no solution is possible is when the string is CATGC, and we require the subsequences determined by positions {0, 3} and {3, 4} be palindromic. Here, characters 3, 0 and 4 would all need to become a T. But this entails modifying consecutive characters 3 and 4, which is not allowed.</p>

### 입력 

 <p>The first line of each test case has two integers N and T (1 ≤ N ≤ 10 000, 1 ≤ T ≤ 6 000), the sequence length and number of subsets to consider. The next line contains the DNA sequence of length N, all of whose characters are in ACGT. The subsets are described by the following T lines. Each line starts by “L:”, where L (0 ≤ L ≤ N) is the number of positions in the subset, and is followed by T distinct integers between 0 and N − 1 in increasing order. Subsets may overlap partially or totally.</p>

<p>A blank line separates different test cases. The input file is terminated by a line containing 0 0.</p>

### 출력 

 <p>In a single line per test case, print YES if the task is solvable and NO otherwise.</p>

