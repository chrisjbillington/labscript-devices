#####################################################################
#                                                                   #
# /NI_DAQmx/models/_subclass_template.py                            #
#                                                                   #
# Copyright 2018, Christopher Billington                            #
#                                                                   #
# This file is part of the module labscript_devices, in the         #
# labscript suite (see http://labscriptsuite.org), and is           #
# licensed under the Simplified BSD License. See the license.txt    #
# file in the root of the project for the full license.             #
#                                                                   #
#####################################################################

#####################################################################
#     WARNING                                                       #
#                                                                   #
# This file is auto-generated, any modifications may be             #
# overwritten. See README.txt in this folder for details            #
#                                                                   #
#####################################################################


from labscript_devices.NI_DAQmx.labscript_devices import NI_DAQmx

#:
CAPABILITIES = {
    'AI_range': None,
    'AI_start_delay': None,
    'AO_range': None,
    'max_AI_multi_chan_rate': None,
    'max_AI_single_chan_rate': None,
    'max_AO_sample_rate': None,
    'max_DO_sample_rate': 20000000.0,
    'min_semiperiod_measurement': None,
    'num_AI': 0,
    'num_AO': 0,
    'num_CI': 0,
    'ports': {
        'port0': {'num_lines': 8, 'supports_buffered': True},
        'port1': {'num_lines': 8, 'supports_buffered': True},
        'port2': {'num_lines': 8, 'supports_buffered': True},
        'port3': {'num_lines': 8, 'supports_buffered': True},
        'port4': {'num_lines': 0, 'supports_buffered': False},
        'port5': {'num_lines': 4, 'supports_buffered': False},
    },
    'supports_buffered_AO': False,
    'supports_buffered_DO': True,
    'supports_semiperiod_measurement': False,
}


class NI_PCI_DIO_32HS(NI_DAQmx):
    description = 'NI-PCI-DIO-32HS'

    def __init__(self, *args, **kwargs):
        """Class for NI-PCI-DIO-32HS"""
        # Any provided kwargs take precedent over capabilities
        combined_kwargs = CAPABILITIES.copy()
        combined_kwargs.update(kwargs)
        NI_DAQmx.__init__(self, *args, **combined_kwargs)
