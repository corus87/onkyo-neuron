# -*- coding: iso-8859-1 -*-
import eiscp
import logging
from kalliope.core.NeuronModule import NeuronModule, MissingParameterException

logging.basicConfig()
logger = logging.getLogger("kalliope")

class Onkyo(NeuronModule):
    def __init__(self, **kwargs):
        super(Onkyo, self).__init__(**kwargs)
    # the args from the neuron configuration
        self.ip_address = kwargs.get('ip_address', None)
        self.volume = kwargs.get('volume', None)
        self.command_1 = kwargs.get('command_1', None)
        self.command_2 = kwargs.get('command_2', None)
        self.command_3 = kwargs.get('command_3', None)
        self.command_4 = kwargs.get('command_4', None)
        self.command_5 = kwargs.get('command_5', None)
        self.command_6 = kwargs.get('command_6', None)


    # check if parameters have been provided
        if self._is_parameters_ok():
            receiver = eiscp.eISCP(self.ip_address)

            if self.volume is not None:
                try:                
                    receiver.command("volume=%s" % int(self.volume))                
                    receiver.disconnect()  
                except ValueError:
                    logger.debug("Attention: Onkyo volume needs to be integer")
                    
            if self.command_1 is not None:
                receiver.command(self.command_1)                
               
            if self.command_2 is not None:
                receiver.command(self.command_2)
             
            if self.command_3 is not None:
                receiver.command(self.command_3)
                       
            if self.command_4 is not None:      
                receiver.command(self.command_4)
         
            if self.command_5 is not None:
                receiver.command(self.command_5)
          
            if self.command_6 is not None:
                receiver.command(self.command_6)
            receiver.disconnect()

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise

        .. raises:: MissingParameterException
        """
        if self.ip_address is None:
            raise MissingParameterException("You must set the IP address")
        return True
