import abc

class PickuplineAbstract(metaclass=abc.ABCMeta):
    """
    Abstract class to be used across multiple website where we can find pickuplines
    """

    @abc.abstractproperty
    def source_url(self):
        """source_url of the website or any remote data source path"""
        raise NotImplementedError

    @abc.abstractmethod
    def get_pickupline(self, *args, **kwargs):
        """
        Get pickupline based on whatever parameters you define in args,kwargs
        """
        raise NotImplementedError
