"""Classes for melon orders."""
import random, datetime

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from
    
    subclasses should have order_type and tax"""

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False

    def get_base_price(self):

        rand_base_price = random.randint(5, 9)    

        

        return rand_base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        if self.species == "Christmas melons":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total = total + 3

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = .08

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        

   


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    tax = 0
    order_type = "domestic"
    passed_inspection = False
    
    def  __init__(self, species, qty):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
       

    def mark_inspection(self, passed):

        if passed == True:
            self.passed_inspection = True