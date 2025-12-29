# OR Performance | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/or-performance

OR Performance
Test setup

Object recognition performance tests were done using a dedicated machine that only runs the Object Recognition service with the following hardware:

CPU: 12th Gen Intel(R) Core(TM) i9-12900KF @ 3.20 GHz.

NVIDIA GPU: NVIDIA GeForce RTX 3080 Ti.

Intel GPU: Intel UHD Graphics 750.

During the test, the following metrics were observed and collected:

Input frame rate

Output frame rate

Memory usage (RAM)

CPU usage

GPU usage for model interference

GPU usage for video decompression

GPU memory usage

Tests were performed by using H.264 compressed video clip with 1920x1080 resolution.

Test results
Performance Test Results for Vehicles
CPU: 12th Gen Intel(R) Core(TM) i9-12900KF @ 3.20 GHz
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

GPU memory




1

	

4

	

4

	

25%

	

4.6 GB

	

4%

	

3%

	

3.5 GB




2

	

8

	

8

	

45 %

	

4.8 GB

	

8%

	

8%

	

3.8 GB




3

	

10

	

10

	

88%

	

5.6 GB

	

11%

	

11%

	

4.1 GB

NVIDIA GPU: NVIDIA GeForce RTX 3080 Ti
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

GPU memory




1

	

4

	

4

	

3%

	

2.8 GB

	

25%

	

3%

	

3.9 GB




2

	

8

	

8

	

4 %

	

3.5 GB

	

30%

	

5%

	

4.2 GB




3

	

12

	

12

	

5%

	

3.7 GB

	

30%

	

5%

	

4.6 GB




4

	

16

	

16

	

5%

	

3.8 GB

	

35%

	

5%

	

4.9 GB




5

	

20

	

20

	

6%

	

4.0 GB

	

35%

	

4%

	

5.2 GB




6

	

24

	

24

	

6%

	

4.1 GB

	

35%

	

5%

	

5.5 GB




7

	

28

	

28

	

7%

	

4.3 GB

	

43%

	

6%

	

5.9 GB




8

	

32

	

32

	

8%

	

4.4 GB

	

50%

	

6%

	

6.2 GB




9

	

36

	

36

	

10%

	

4.6 GB

	

95%

	

6%

	

6.6 GB




10

	

40

	

40

	

10%

	

4.8 GB

	

95%

	

6%

	

7.0 GB




11

	

44

	

44

	

13%

	

4.9 GB

	

98%

	

6%

	

7.4 GB




12

	

48

	

48

	

13%

	

5.1 GB

	

98%

	

6%

	

7.8 GB




13

	

52

	

52

	

17%

	

5.2 GB

	

98%

	

6%

	

8.1 GB




14

	

56

	

56

	

17%

	

5.7 GB

	

99%

	

7%

	

8.5 GB




15

	

60

	

60

	

20%

	

6.5 GB

	

99%

	

7%

	

8.9 GB




16

	

55

	

55

	

21%

	

5.5 GB

	

98%

	

7%

	

9.2 GB

Intel GPU: Intel UHD Graphics 750
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

Intel GPU

	

Intel GPU memory




1

	

4

	

4

	

23%

	

3.5 GB

	

2%

	

2%

	

50%

	

0.7 GB




2

	

8

	

8

	

50%

	

4.2 GB

	

3%

	

3%

	

99%

	

0.9 GB




3

	

7

	

7

	

50%

	

4.6 GB

	

3%

	

3%

	

100%

	

0.9 GB

Performance test results for persons
CPU: 12th Gen Intel(R) Core(TM) i9-12900KF 3.20 GHz
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

GPU memory




1

	

4

	

4

	

60%

	

4.9 GB

	

3%

	

3%

	

3.5 GB




2

	

6

	

6

	

86 %

	

5.4 GB

	

3%

	

3%

	

3.8 GB

NVIDIA GPU: NVIDIA GeForce RTX 3080 Ti
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

GPU memory




1

	

4

	

4

	

4%

	

3.3 GB

	

31%

	

2%

	

4.6 GB




2

	

8

	

8

	

6%

	

3.6 GB

	

35%

	

2%

	

5.0 GB




3

	

12

	

12

	

9%

	

3.7 GB

	

90%

	

2%

	

5.3 GB




4

	

16

	

16

	

12%

	

3.9 GB

	

95%

	

2%

	

5.6 GB




5

	

20

	

20

	

14%

	

4.3 GB

	

98%

	

2%

	

6.1 GB




6

	

20

	

20

	

17%

	

5.0 GB

	

99%

	

2%

	

6.4 GB

Intel GPU: Intel UHD Graphics 750
Use table header to sort columns

Streams

	

Input FPS

	

Output FPS

	

Process CPU

	

Process memory

	

NVIDIA GPU

	

NVIDIA decode

	

Intel GPU

	

Intel GPU memory




1

	

4

	

4

	

23%

	

0.6 GB

	

4%

	

4%

	

60%

	

0.7 GB




2

	

2

	

0

	

75%

	

3.1 GB

	

6%

	

6%

	

100%

	

1.0 GB

These tests are indicative and may not be directly applicable to production systems.

Pagination
Previous page
OR Service Installation
Next page
Mirasys List Management (LM)