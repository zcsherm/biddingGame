
from cards import *
from players import *
from collectionsitems import *
import unittest
TEST_ITEMS = {"Item One":(1,2),
              "Item Two":(3,4),
              "Item Three":(5,6)
             }
TEST_CONTRACTS = {"Contract One":(1,2,3),
                  "Contract Two":(4,5,6),
                  "Contract Three":(7,8,9)
                 }

class testCards(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self._test_items = []
        self._test_contracts = []
        for card_name in TEST_ITEMS:
            attributes = TEST_ITEMS[card_name]
            self._test_items.append(Item(card_name,*attributes))
        for card_name in TEST_CONTRACTS:
            attributes = TEST_CONTRACTS[card_name]
            self._test_contracts.append(Contract(card_name,*attributes))

    def testCardGeneration(self):
        test_item = Item("Item One",1,2)
        test_contract = Contract("Contract One",1,2,3)
        # Test generic creation and default values
        self.assertEqual(test_item.get_name(),"Item One")
        self.assertEqual(test_item.get_cost(),1)
        self.assertEqual(test_item.get_value(),2)
        self.assertEqual(test_contract.get_name(),"Contract One")
        self.assertEqual(test_contract.get_budget(),1)
        self.assertEqual(test_contract.get_target(),2)
        self.assertEqual(test_contract.get_points(),3)
        self.assertIsNone(test_contract.get_owner())
        self.assertIsNone(test_item.get_owner())

        # Test the generated cards against the test cases
        for card in self._test_items:
            attributes = (card.get_cost(),card.get_value())
            self.assertEqual(TEST_ITEMS[card.get_name()], attributes)
        for card in self._test_contracts:
            attributes = (card.get_budget(), card.get_target(), card.get_points())
            self.assertEqual(TEST_CONTRACTS[card.get_name()], attributes)

        # Test for invalid inputs

    def testCardTypes(self):
        pass

    def testModifyCards(self):
        pass

class testDeck(unittest.TestCase):

    def testDeckGeneration(self):
        pass

    def testDrawCards(self):
        pass

    def testShuffle(self):
        pass

    def testCards(self):
        pass

class testPlayer(unittest.TestCase):

    def testAddPoints(self):
        pass

    def testRemovePoints(self):
        pass

    def testPickItem(self):
        pass

    def testAddContract(self):
        pass

    def testAssignItems(self):
        pass

if __name__ == '__main__':
    unittest.main()
