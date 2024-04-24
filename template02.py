# Name: *** Enter your name here ***
#
# Student-ID: *** Enter your student ID here ***
#
# Rename the file to <yourname>02.py
#
import numpy as np
import matplotlib.pylab as plt

def upsample(f_sampled, N):
    """Convenience function for resampling a signal using an explicit iDFT matrix."""
    F_sampled = np.fft.fftshift(np.fft.fft(f_sampled)) / len(f_sampled)
    n_sampled = np.arange(-len(f_sampled) // 2, len(f_sampled) // 2)
    F_inv = np.exp(2j * np.pi * np.multiply.outer(np.arange(N), n_sampled) / N)
    return F_inv @ F_sampled

# Please do not change the code above this line

# Exercise 1: Fourier pairs
#
def exercise1():

    # close all figures
    plt.close('all')

    # Task 1A: Implement the tringular function
    
    def tri(x):
        # *** Insert your Python code here ***
        pass
    
    # Task 1B: Sample sinc squared at locations `a + (b-a) m / N` where
    # a, b, N = -64, 64, 512

    # *** Insert your Python code here ***
    
    # Task 1C: Compute the FFT of the signal sampled in 1B and shift its zero-
    # frequency component to the center
    
    # *** Insert your Python code here ***
    
    # Task 1D: Construct the frequency grid `2pi / (b-a) * n` for n ranging from
    # -N/2 to N/2-1

    # *** Insert your Python code here ***
    
    # Task 1E: Multiply the FFT computed in 1C with the factor derived in
    # equation (6)

    # *** Insert your Python code here ***
    
    # Task 1F: Plot the left and right hand side of equation (6) to verify that
    # indeed the sinc squared and triangular function form a Fourier pair

    # *** Insert your Python code here ***

    
# Exercise 2: Sampling `cos(x) + 2 sin(4x)`
#
def exercise2():

    # close all figures
    plt.close('all')

    # Task 2A: Implement a Python function `signal` that evaluates
    # `cos(x) + 2 sin(4x)`
    #
    def signal(x):
        # *** Insert your Python code here ***
        pass
    
    # Task 2B: Sample the signal using 96 equidistant grid points covering the
    # interval [0, 2pi)
    
    # *** Insert your Python code here ***
    
    # Task 2C: Sample the signal using a smaller number of grid points covering
    # [0, 2pi). Use the two strategies explained in the exercise description to
    # generate the coarsely sampled signals and check (e.g. with `np.allclose`)
    # that the results indeed agree. 

    # *** Insert your Python code here ***
    
    # Task 2D: Plot the fine signal and the coarsely sampled signals
    
    # *** Insert your Python code here ***
        
    # Task 2E: Plot the fine signal and the coarse signals with `plot`
    
    # *** Insert your Python code here ***
        
    # Task 2F: Upsample the coarse signals and plot them. Use the Fourier transform
    # to do the interpolation. Implement the upsampling procedure as a local Python
    # function `upsample(f, N)` with two arguments: the coarse signal `f` (a NumPy
    # array) and the desired size of the upsampled signal `N` (an integer larger
    # than `len(f)`). Plot the original signal as a transparent black line and the
    # upsampled signal as a red line

    def upsample(f_coarse, N):
        # *** Insert your Python code here ***
        pass
    
    # *** Insert your Python code here ***
