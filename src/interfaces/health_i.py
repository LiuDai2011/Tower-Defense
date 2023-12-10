import abc
from src.types.unit import Unit


class IHealth(abc.ABC):
    @abc.abstractmethod
    def get_health(self) -> float:
        """Get Health"""

    @abc.abstractmethod
    def set_health(self, amount: float = 0):
        """Set Health"""

    @abc.abstractmethod
    def get_max_health(self) -> float:
        """Get Max Health"""

    @abc.abstractmethod
    def set_max_health(self, amount: float = 0):
        """Set Max Health"""

    @abc.abstractmethod
    def damageable(self) -> bool:
        """Return self.damageable"""

    @abc.abstractmethod
    def damage(self, amount: float = 0, attack: Unit = None) -> bool:
        """Return false If self is not damageable, Else Damage"""
