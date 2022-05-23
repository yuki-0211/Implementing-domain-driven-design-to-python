from typing import Optional, Type, TypeVar, TypedDict
from pydantic import BaseModel


CustomerTable = TypedDict('CustomerTable', {
    'customerId': str,
    'customerFirstName': str,
    'customerLastName': str,
    'streetAddress1': str,
    'streetAddress2': str,
    'city': str,
    'stateOrProvince': str,
    'postalCode': str,
    'country': str,
    'homePhone': str,
    'mobilePhone': str,
    'primaryEmailAddress': str,
    'secondaryEmailAddress': str,
})

example_customer: CustomerTable = {
    'customerId': 'exampleId001',
    'customerFirstName': 'exampleFirstName001',
    'customerLastName': 'exampleLastName001',
    'streetAddress1': 'exampleAddress001',
    'streetAddress2': 'exampleAddress002',
    'city': 'exampleCity001',
    'stateOrProvince': 'exampleProvince001',
    'postalCode': 'examplePostalCode001',
    'country': 'exampleCountry001',
    'homePhone': 'examplePhone001',
    'mobilePhone': 'examplePhone002',
    'primaryEmailAddress': 'exampleEmail001',
    'secondaryEmailAddress': 'exampleEmail002',
}

T = TypeVar('T', bound='Customer')


class Customer(BaseModel):
    """
    Class containing the methods necessary to execute save_customer.
    It also includes processing of the persistence layer.
    Do not imitate.
    """
    customerId: str
    customerFirstName: str
    customerLastName: str
    streetAddress1: str
    streetAddress2: str
    city: str
    stateOrProvince: str
    postalCode: str
    country: str
    homePhone: str
    mobilePhone: str
    primaryEmailAddress: str
    secondaryEmailAddress: str

    def to_dto(self, customer: "Customer") -> "Customer":
        return Customer(
            customerId=customer.customerId,
            customerFirstName=customer.customerFirstName,
            customerLastName=customer.customerLastName,
            streetAddress1=customer.streetAddress1,
            streetAddress2=customer.streetAddress2,
            city=customer.city,
            stateOrProvince=customer.stateOrProvince,
            postalCode=customer.postalCode,
            country=customer.country,
            homePhone=customer.homePhone,
            mobilePhone=customer.mobilePhone,
            primaryEmailAddress=customer.primaryEmailAddress,
            secondaryEmailAddress=customer.secondaryEmailAddress
        )

    @classmethod
    def from_dto(cls: Type[T], dto: CustomerTable) -> "Customer":
        return Customer(
            customerId=dto['customerId'],
            customerFirstName=dto['customerFirstName'],
            customerLastName=dto['customerLastName'],
            streetAddress1=dto['streetAddress1'],
            streetAddress2=dto['streetAddress2'],
            city=dto['city'],
            stateOrProvince=dto['stateOrProvince'],
            postalCode=dto['postalCode'],
            country=dto['country'],
            homePhone=dto['homePhone'],
            mobilePhone=dto['mobilePhone'],
            primaryEmailAddress=dto['primaryEmailAddress'],
            secondaryEmailAddress=dto['secondaryEmailAddress']
        )

    @staticmethod
    def readCustomer(customerId: str) -> "Customer":
        """
        Suppose there is a process that retrieves customer information
         matching customerId from the persistence layer.
        """
        print(customerId)
        customer: Customer = Customer.from_dto(dto=example_customer)
        return customer

    def saveCustomer(self, customer: "Customer") -> None:
        """
        Suppose there is a process that retrieves customer information
         matching customerId from the persistence layer.
        """
        self.to_dto(customer=customer)

    def setCustomerFirstName(self, customerFirstName: str):
        self.customerFirstName = customerFirstName

    def setCustomerLastName(self, customerLastName: str):
        self.customerLastName = customerLastName

    def setStreetAddress1(self, streetAddress1: str):
        self.streetAddress1 = streetAddress1

    def setStreetAddress2(self, streetAddress2: str):
        self.streetAddress2 = streetAddress2

    def setCity(self, city: str):
        self.city = city

    def setStateOrProvince(self, stateOrProvince: str):
        self.stateOrProvince = stateOrProvince

    def setPostalCode(self, postalCode: str):
        self.postalCode = postalCode

    def setCountry(self, country: str):
        self.country = country

    def setHomePhone(self, homePhone: str):
        self.homePhone = homePhone

    def setMobilePhone(self, mobilePhone: str):
        self.mobilePhone = mobilePhone

    def setPrimaryEmailAddress(self, primaryEmailAddress: str):
        self.primaryEmailAddress = primaryEmailAddress

    def setSecondaryEmailAddress(self, secondaryEmailAddress: str):
        self.secondaryEmailAddress = secondaryEmailAddress


def saveCustomer(customerId: str,
                 customerFirstName: Optional[str] = None,
                 customerLastName: Optional[str] = None,
                 streetAddress1: Optional[str] = None,
                 streetAddress2: Optional[str] = None,
                 city: Optional[str] = None,
                 stateOrProvince: Optional[str] = None,
                 postalCode: Optional[str] = None,
                 country: Optional[str] = None,
                 homePhone: Optional[str] = None,
                 mobilePhone: Optional[str] = None,
                 primaryEmailAddress: Optional[str] = None,
                 secondaryEmailAddress: Optional[str] = None,
                 ) -> None:
    """
    The first bad example .
    So-called super class ....
    Furthermore, it is given the same name as the persistence method.
    """
    customerDao = Customer.from_dto(dto=example_customer)
    customer: Customer = customerDao.readCustomer(customerId)

    if customerFirstName is not None:
        customer.setCustomerFirstName(customerFirstName=customerFirstName)
    if customerLastName is not None:
        customer.setCustomerLastName(customerLastName=customerLastName)
    if streetAddress1 is not None:
        customer.setStreetAddress1(streetAddress1=streetAddress1)
    if streetAddress2 is not None:
        customer.setStreetAddress2(streetAddress2=streetAddress2)
    if city is not None:
        customer.setCity(city=city)
    if stateOrProvince is not None:
        customer.setStateOrProvince(stateOrProvince=stateOrProvince)
    if postalCode is not None:
        customer.setPostalCode(postalCode=postalCode)
    if country is not None:
        customer.setCountry(country=country)
    if homePhone is not None:
        customer.setHomePhone(homePhone=homePhone)
    if mobilePhone is not None:
        customer.setMobilePhone(mobilePhone=mobilePhone)
    if primaryEmailAddress is not None:
        customer.setPrimaryEmailAddress(primaryEmailAddress=primaryEmailAddress)
    if secondaryEmailAddress is not None:
        customer.setSecondaryEmailAddress(secondaryEmailAddress=secondaryEmailAddress)

    customerDao.saveCustomer(customer)
