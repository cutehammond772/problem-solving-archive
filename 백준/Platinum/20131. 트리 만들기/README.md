# [Platinum V] 트리 만들기 - 20131 

[문제 링크](https://www.acmicpc.net/problem/20131) 

### 성능 요약

메모리: 204588 KB, 시간: 1016 ms

### 분류

자료 구조, 우선순위 큐, 트리

### 제출 일자

2024년 2월 10일 22:45:31

### 문제 설명

<p>정점이 <em>N</em>개가 있는 트리가 있고 각 정점들은 1부터 <em>N</em>까지 번호가 매겨있다. 해당 트리로부터 (<em>N</em>-2)개의 양의 정수로 이루어진 수열 하나를 다음과 같은 과정을 통해서 만들 것이다.</p>

<ol>
	<li>차수가 1인 정점들 중에서 번호가 가장 큰 정점을 하나 고른다. 해당 정점을 <em>x</em>라고 부르자.</li>
	<li>정점 <em>x</em>와 인접한 정점의 번호를 수열에 넣는다.</li>
	<li>정점 <em>x</em>와 인접한 간선들을 해당 트리에서 지운다.</li>
	<li>1번부터 3번까지의 과정을 총 (<em>N</em>-2) 번 진행한다.</li>
</ol>

<p>수열 {<em>a<sub>1</sub></em>, ... , <em>a<sub>N-2</sub></em>}가 주어졌을 때, 위의 과정을 통해서 이 수열을 만들 수 있는 트리를 구하여라.</p>

### 입력 

 <p>다음과 같이 입력이 주어진다.</p>

<div style="background:#eeeeee;border:1px solid #cccccc;padding:5px 10px;"><em>N</em><br>
<em>a<sub>1</sub></em> . . . <em>a<sub>N-2</sub></em></div>

### 출력 

 <p>해당 트리가 존재한다면 간선 (<em>N</em>-1) 개를 다음 규칙에 만족하게 출력한다.</p>

<ul data-indent="0" data-stringify-type="unordered-list">
	<li>각 간선은 <span class="marker"><em>a</em> <em>b</em></span> 형태로 출력해야 하며 <em>a</em> < <em>b</em>를 만족하여야 한다.</li>
	<li>간선을 사전 순으로 출력해야 한다. 즉, 임의의 두 간선 (<em>a<sub>1</sub></em>, <em>b<sub>1</sub></em>)과 (<em>a<sub>2</sub></em>, <em>b<sub>2</sub></em>)에 대해 <em>a<sub>1</sub></em> < <em>a<sub>2</sub></em>를 만족하거나 <em>a<sub>1</sub></em> = <em>a<sub>2</sub></em>, <em>b<sub>1</sub></em> < <em>b<sub>2</sub></em>를 만족하는 경우 (<em>a<sub>1</sub></em>, <em>b<sub>1</sub></em>) 간선을 (<em>a<sub>2</sub></em>, <em>b<sub>2</sub></em>) 간선보다 먼저 출력해야 한다.</li>
</ul>

<p>만약에 트리가 존재하지 않거나 2개 이상 존재하는 경우에는 <span style="color:#e74c3c;"><code>-1</code></span>을 출력하여라.</p>

