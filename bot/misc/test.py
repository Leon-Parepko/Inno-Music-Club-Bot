import unittest

from bot.misc.util import get_class_field_value_by_name, phone_parse


class TestSomeUtils(unittest.TestCase):
    class TestClasses:
        class ClassA:
            class EmptyClass:
                pass

            def __init__(self):
                self.field1 = 1
                self.field2 = '2'

            field1: int = 1
            field2: str = '2'
            empty_field1: int
            empty_field2: str
            empty_field3: EmptyClass

    test_table = [
        # get_class_field_by_name(TestClasses.ClassA(), 'empty_field2'): None,
        [get_class_field_value_by_name(TestClasses.ClassA(), 'field1'), 1, 'field1'],
        [get_class_field_value_by_name(TestClasses.ClassA(), 'field2'), '2', 'field2'],
        [get_class_field_value_by_name(TestClasses.ClassA(), 'empty_field1'), 0, 'empty_field1'],
        [get_class_field_value_by_name(TestClasses.ClassA(), 'empty_field2'), '', 'empty_field2'],
        [type(get_class_field_value_by_name(TestClasses.ClassA(), 'empty_field3')), TestClasses.ClassA.EmptyClass, 'empty_field3'],
        [get_class_field_value_by_name(TestClasses.ClassA(), ''), None, '<empty str>'],
        [get_class_field_value_by_name(TestClasses.ClassA(), 'Not Field'), None, 'Not Field'],
    ]

    def test_get_class_field_by_name(self):
        # print(self.test_table)
        # print(self.TestClasses.ClassA().__dict__)
        # print(self.TestClasses.ClassA().__class__.__dict__.get('__annotations__'))
        fields = self.TestClasses.ClassA().__class__.__dict__.get("__annotations__")
        for item in self.test_table:
            actual, expect = item[0], item[1]
            self.assertEqual(expect, actual, f'fields: {fields}; tryed to find: {item[2]}')

        self.assertEqual(15024920491020, phone_parse('1e%~`ASxK5&0p2ecl\'\'49:2049102-sdalfjkasjfo0t'))


if __name__ == '__main__':
    unittest.main()
