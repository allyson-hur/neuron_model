import matplotlib.pyplot as plt
from neuron import h
from neuron.units import ms, mV

def simple_model():
    # Create a cell
    soma = h.Section(name='soma')

    # Set properties
    soma.L = 20 # length (microns)
    soma.diam = 20  # diameter (microns)

    # Insert ion channels
    soma.insert('hh')

    # Insert a stimulus
    iclamp = h.IClamp(soma(0.5))

    iclamp.delay = 2    # delay before the current starts (ms)
    iclamp.dur = 0.1    # duration of the current pulse (ms)
    iclamp.amp = 0.9    # amplitude of the current pulse (nA)

    # Set up recording variables
    v = h.Vector().record(soma(0.5)._ref_v) # Membrane potential vector
    t = h.Vector().record(h._ref_t) # Time stamp vector

    # Run simulation
    h.load_file('stdrun.hoc')
    h.finitialize(-65 * mV)
    h.continuerun(40 * ms)

    plt.figure()
    plt.plot(t, v)
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane Potential (mV)')
    plt.show()



