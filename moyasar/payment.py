import json

from moyasar.resource import Resource
from moyasar.actions.refund import Refund
from moyasar.helpers import Constructor
from moyasar.helpers import Format


class Source(Constructor):

    @classmethod
    def build(cls, source):
        if source['type'] == "creditcard":
            source = Source.source_to_creditcard(source)
        else:
            source = Source.source_to_sadad(source)
        return source

    @classmethod
    def source_to_creditcard(cls, data):
        data.pop('type')
        # Because dumps() in helpers.py works with basic types (str, int, float, bool, None)
        # CreditCard obj needs to be returned as str to pass Payment's __str__()
        return json.dumps(CreditCard(data).__dict__)

    @classmethod
    def source_to_sadad(cls, data):
        data.pop('type')
        return Sadad(data)


class CreditCard(Source):
    def __str__(self):
        return json.dumps(self.__dict__)


class Sadad(Source):
    pass


class Payment(Resource, Refund, Format):

    def __init__(self, data):
        super().__init__(data)
        self.source = Source.build(self.source)

    def refund(self, amount=None):
        super().refund(amount)
        self.source = Source.build(self.source)
        return self