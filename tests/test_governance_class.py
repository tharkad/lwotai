from labyrinth_test_case import LabyrinthTestCase
from lwotai import FAIR
from lwotai import Governance
from lwotai import Governances


class GovernanceClassTest(LabyrinthTestCase):

    def test_with_good_index(self):
        gov = Governances.with_index(2)
        self.assertEquals(FAIR, gov)

    def test_with_too_high_index(self):
        try:
            Governances.with_index(5)
            self.fail("Should have raised a ValueError")
        except ValueError as e:
            self.assertEquals("Invalid governance value - 5", e.message)

    def test_str(self):
        gov = Governance("Anarchy", 5, -2)
        self.assertEquals("Anarchy", str(gov))

    def test_repr(self):
        gov = Governance("Anarchy", 5, -2)
        self.assertEquals('Governance("Anarchy", 5, -2)', repr(gov))

    def test_equality(self):
        name = "some name"
        max_roll = 3
        gov1 = Governance(name, max_roll, 0)
        gov2 = Governance(name, max_roll, 0)
        self.assertEquals(gov1, gov2)

    def test_inequality_by_name(self):
        gov1 = Governance("name 1", 0, 1)
        gov2 = Governance("name 2", 0, 1)
        self.assertNotEqual(gov1, gov2)

    def test_inequality_by_max_roll(self):
        gov1 = Governance("name 1", 1, 2)
        gov2 = Governance("name 1", 2, 2)
        self.assertEqual(gov1, gov2)

    def test_successful_roll(self):
        max_roll = 4
        gov = Governance("some name", max_roll, 0)
        for roll in range(1, max_roll + 1):
            self.assertTrue(gov.is_success(roll))
        for roll in range(max_roll + 1, max_roll + 2):
            self.assertFalse(gov.is_success(roll))

    @staticmethod
    def test_instances_are_hashable():
        gov = Governance("anything", 0, 0)
        hash(gov)