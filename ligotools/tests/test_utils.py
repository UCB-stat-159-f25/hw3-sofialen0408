import ligotools.utils as ul
import numpy as np
from pathlib import Path

def test_whiten():
    fs = 4096
    dt = 1 / fs
    N = 131072
    strain = np.random.normal(0, 1, N)
	
    def interp_psd(freqs):
        return np.ones_like(freqs)
	
    assert len(ul.whiten(strain, interp_psd, dt)) == len(strain)

def test_shift_waves():
    fs = 4096
    fshift = 400.
    data = [0, 1, 0, -1, 0]
    freq_shift = ul.reqshift(data,fshift=fshift,sample_rate=fs)
    
    assert freq_shift[0] == 0.2795084971874737
    
    filename = "test.wav"
    folder = "audio"

    ul.write_wavfile(folder, filename, fs, data)
    filepath = Path(folder) / filename
    assert filepath.exists()