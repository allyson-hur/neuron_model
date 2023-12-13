from neuron import h, gui
from neuron.units import ms, mV

def hh_neuron_model():
    # Create a cell
    soma = h.Section(name='soma')

    # Insert Hodgkin-Huxley specific ion channels
    soma.insert('hh')

    # Set properties
    soma.L = 20.0  # length (microns)
    soma.diam = 20.0  # diameter (microns)
    soma.Ra = 100.0  # axial resistance (Ohm * cm)
    soma.cm = 1.0  # membrane capacitance (uF/cm^2)

    # Set initial membrane potential
    soma.v = -65.0  # default initial membrane potential (mV)

    # Access the Hodgkin-Huxley mechanisms
    hh = soma(0.5).hh

    # Set Hodgkin-Huxley parameters
    hh.m = 0.05  # initial m gate value
    hh.h = 0.6   # initial h gate value
    hh.n = 0.32  # initial n gate value

    # Insert a current clamp stimulus
    stim = h.IClamp(soma(0.5))  # place the stimulus in the middle of the soma
    stim.delay = 5.0  # delay before the current starts (ms)
    stim.dur = 50.0  # duration of the current pulse (ms)
    stim.amp = 0.1  # amplitude of the current pulse (nA)

    # Set up recording variables
    time_vec = h.Vector()
    voltage_vec = h.Vector()
    m_vec = h.Vector()
    h_vec = h.Vector()
    n_vec = h.Vector()

    # Record time, voltage, and gating variables
    time_vec.record(h._ref_t)
    voltage_vec.record(soma(0.5)._ref_v)
    m_vec.record(hh._ref_m)
    h_vec.record(hh._ref_h)
    n_vec.record(hh._ref_n)

    # Initialize and run the simulation
    h.load_file('stdrun.hoc')
    h.finitialize(-65.0)
    h.continuerun(100.0)  # run the simulation for 100 ms

    # Plot the results
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time_vec, voltage_vec, label='Membrane Potential (mV)')
    plt.xlabel('Time (ms)')
    plt.ylabel('Membrane Potential (mV)')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(time_vec, m_vec, label='m')
    plt.plot(time_vec, h_vec, label='h')
    plt.plot(time_vec, n_vec, label='n')
    plt.xlabel('Time (ms)')
    plt.ylabel('Gating Variables')
    plt.legend()

    plt.tight_layout()
    plt.show()
