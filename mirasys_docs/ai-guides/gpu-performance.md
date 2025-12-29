# GPU Performance | Mirasys Help Center

Source: https://documentation.mirasys.com/ai-guides/V9.9/gpu-performance

GPU Performance

Here is a basic explanation of what the CPU is used for. The CPU is used for the following

Decoding the incoming RTSP stream

Encoding any outgoing annotated RTSP 

Resizing frames before being passed to the analytic engine

Preprocessing before the frame is passed to the GPU for the DL tracker to process

The first 3 points are currently performed for all trackers, the standard motion object tracker and the DL trackers.

The last point is performed when using the DL trackers and requires some additional resources from the CPU. As a result, the number of channels that can be supported on a particular CPU is reduced when using the DL trackers.

This chart is giving some overview how VCA can perform with GPU. Different scenarios may affect performance.

GPU

	

CUDA cores

	

Tensor cores

	

Memory

	

Processor frequency

	

Memory Bandwidth (GB/sec)

	

Actual channels DLOT tested




RTX A4000

	

6144

	

192

	

16 GB

	

1750

	

448

	

56




GeForce RTX 3070

	

5888

	

180

	

8 GB

	

1440-1710

	

19

	

54




GeForce RTX 2080 Ti

	

4352

	

368

	

11GB

	

1350-1545

	

616

	

50




Tesla T4

	

2560

	

320

	

16GB

	




	

320

	

45




GeForce GTX 1660 SUPER

	

1408

	




	

6 GB

	

1530-1785

	

336

	

28




GeForce GTX 1650

	

896

	




	

4 GB

	

1485-1665

	

128

	

18

Pagination
Previous page
Presence in A or B