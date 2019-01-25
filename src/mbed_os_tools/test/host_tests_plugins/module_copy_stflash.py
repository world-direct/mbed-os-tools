"""
mbed SDK
Copyright (c) 2011-2015 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Author: Przemyslaw Wirkus <Przemyslaw.Wirkus@arm.com>
"""

import os
from .host_test_plugins import HostTestPluginBase


class HostTestPluginCopyMethod_Stflash(HostTestPluginBase):

    # Plugin interface
    name = 'HostTestPluginCopyMethod_Stflash'
    type = 'CopyMethod'
    capabilities = ['stflash']
    required_parameters = ['image_path','arm_serial']

    def __init__(self):
        """ ctor
        """
        HostTestPluginBase.__init__(self)

    def setup(self, *args, **kwargs):
        """! Configure plugin, this function should be called before plugin execute() method is used.
        """
        self.ST_LINK_CLI = 'st-flash'
        return True

    def execute(self, capability, *args, **kwargs):
        """! Executes capability by name

        @param capability Capability name
        @param args Additional arguments
        @param kwargs Additional arguments

        @details Each capability e.g. may directly just call some command line program or execute building pythonic function

        @return Capability call return value
        """
        if not kwargs['image_path']:
            self.print_plugin_error("Error: image path not specified")
            return False
        
        if not kwargs['arm_serial']:
            self.print_plugin_error("Error: arm seraial not specified")
            return False

        result = False
        if self.check_parameters(capability, *args, **kwargs) is True:
            image_path = os.path.normpath(kwargs['image_path'])
            arm_serial = kwargs['arm_serial']
            if capability == 'stflash':
                # Example:
                # ST-LINK_CLI.exe -p "C:\Work\mbed\build\test\DISCO_F429ZI\GCC_ARM\MBED_A1\basic.bin"
                cmd = [self.ST_LINK_CLI, '--reset','--serial', arm_serial, 'write', image_path, '0x08000000']
                result = self.run_command(cmd, shell=False)
        return result


def load_plugin():
    """ Returns plugin available in this module
    """
    return HostTestPluginCopyMethod_Stflash()
