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

from .host_test_plugins import HostTestPluginBase


class HostTestPluginResetMethod_Stflash(HostTestPluginBase):

    # Plugin interface
    name = 'HostTestPluginResetMethod_Stflash'
    type = 'ResetMethod'
    capabilities = ['stflash']
    required_parameters = ['arm_serial']
    stable = False

    def __init__(self):
        """ ctor
        """
        HostTestPluginBase.__init__(self)

    def setup(self, *args, **kwargs):
        """! Configure plugin, this function should be called before plugin execute() method is used.
        """
        # Note you need to have eACommander.exe on your system path!
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
        if not kwargs['arm_serial']:
            self.print_plugin_error("Error: arm seraial not specified")
            return False

        result = False
        if self.check_parameters(capability, *args, **kwargs) is True:
            if capability == 'stflash':
                # Example:
                # ST-LINK_CLI.exe -Rst -Run
                arm_serial = kwargs['arm_serial']
                cmd = [self.ST_LINK_CLI,'--serial', arm_serial,'reset']
                result = self.run_command(cmd, shell=False)
        return result


def load_plugin():
    """ Returns plugin available in this module
    """
    return HostTestPluginResetMethod_Stflash()
