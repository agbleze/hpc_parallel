import pyopencl as cl

for platform in cl.get_platforms():
    print(f"Platform: {platform.name}")
    print(f"Vendor: {platform.vendor}")
    print(f"Version: {platform.version}")
    
    for device in platform.get_devices():
        print(f" Device: {device.name}")
        print(f" Max Clock Speed: {device.max_clock_frequency}")
        print(f" Max Compute Units: {device.max_compute_units}")
        print(f" Local Memory Size Gb: {device.local_mem_size / (1024**3)}")
        print(f" Global Memory Gb: {device.global_mem_size / (1024**3)}")
        
        
        