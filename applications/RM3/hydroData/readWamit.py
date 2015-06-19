
from bemio.io import wamit
from bemio.io.output import write_hdf5

# Load the data
wamit_data = wamit.WamitOutput(out_file='rm3.out')

# Calculate IRF
for i in xrange(wamit_data.data[0].num_bodies):
	wamit_data.data[i].calc_irf_radiation()
#	wamit_data.data[i].calc_ss_radiation()

# Save the data in HDF5 format
write_hdf5(wamit_data)