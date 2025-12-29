# Spotter Video settings | Mirasys Help Center

Source: https://documentation.mirasys.com/spotter-user-guide/V-9.9/spotter-video-settings

Spotter Video settings

The video settings allow setting custom decoding and change rendering technologies to help improve performance depending on hardware.

Video decoding

Use custom decoding settings allows you to select a specific decoding setting and decide what per cent of streams are decoded using GPU.

H.264 codec

IPP: uses CPU 

CoreAVC: Can use CPU or Nvidia CUDA

Nvidia: requires Nvidia GPU

Intel: uses CPU; if processor chip has Intel Graphics inbuilt GPU, it can also use GPU

H.265 codec

Nvidia: based requires Nvidia GPU

Intel: uses CPU; if the processor chip has Intel Graphics inbuilt GPU, it can also use GPU, slider affects how many cameras use CPU/GPU.

How many streams are decoded with the display hardware 

Defines how percentages of cameras use CPU/GPU.
If decoding method Nvidia is chosen and the slider is set to, E.g. 50%, half of the cameras will be decoded using Nvidia and the other half will use CoreAVC if they are H.264 and Intel CPU if they are H.265

Video rendering

Allows to change video rendering to WPF (default) or DirectX

Enable smooth video scaling

It uses a different image drawing mechanism, and it will have a smoothening effect on video, especially if the framerate is high (over 20 fps).
However, the smooth video scaling setting should not be used if the user has multiple Spotter windows open.
Smooth video scaling will make video image appearance better, but this setting increases the computer load slightly.

Pagination
Previous page
Spotter Streaming Settings
Next page
Spotter Display Settings