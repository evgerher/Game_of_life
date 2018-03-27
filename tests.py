import unittest
import interface
import field

class TestField(unittest.TestCase):
    def test_similarity_1(self):
        f = field.Field(3, 3)
        f.fields[0] = [[True, True, True], [False, True, False], [False, False, True]]
        f.fields[1] = [[True, True, True], [False, True, False], [False, False, True]]
        self.assertTrue(f.field_similarity())

    def test_similarity_2(self):
        f = field.Field(3, 3)
        f.fields[0] = [[True, True, True], [False, True, False], [False, False, True]]
        f.fields[2] = [[True, True, True], [False, True, False], [False, False, True]]
        self.assertTrue(f.field_similarity())

    def test_blinker(self):
        f = field.Field(5, 5)
        f.fields[0] = [[False, False, False, False, False], 
                        [False, False, False, False, False], 
                        [False, True, True, True, False], 
                        [False, False, False, False, False], 
                        [False, False, False, False, False]
                        ]
        step_later = [[False, False, False, False, False],
                        [False,False, True, False, False], 
                        [False,False, True, False, False], 
                        [False,False, True, False, False],
                        [False, False, False, False, False]]
        two_steps_later = f.fields[0][:]
        
        new_field, condition = f.process_field()
        self.assertEqual(new_field, step_later)
        # Not end 
        self.assertTrue(condition)
        new_field, condition = f.process_field()
        self.assertEqual(new_field, two_steps_later)
        # End
        self.assertFalse(condition)

    def test_cell(self):
        f = field.Field(5, 5)
        f.fields[0] = [[False, False, False, False, False],
                        [False, True, False, True, False], 
                        [False, False, True, False, False], 
                        [False, False, False, True, False], 
                        [False, False, False, False, False]
                        ]
        cell_00 = (False, 1)
        cell_01 = (False, 1)
        cell_02 = (False, 2)
        cell_03 = (False, 1)
        cell_04 = (False, 1)

        cell_10 = (False, 1)
        cell_11 = (False, 1)
        cell_12 = (True, 3)
        cell_13 = (False, 1)
        cell_14 = (False, 1)
     
        cell_20 = (False, 1)
        cell_21 = (False, 2)
        cell_22 = (True, 3)
        cell_23 = (True, 3)
        cell_24 = (False, 2)

        cell_30 = (False, 0)
        cell_31 = (False, 1)
        cell_32 = (False, 2)
        cell_33 = (False, 1)
        cell_34 = (False, 1)

        cell_40 = (False, 0)
        cell_41 = (False, 0)
        cell_42 = (False, 1)
        cell_43 = (False, 1)
        cell_44 = (False, 1)

        self.assertEqual(cell_00, (f.process_cell(0, 0), f.count_neighbours(0, 0)))
        self.assertEqual(cell_01, (f.process_cell(0, 1), f.count_neighbours(0, 1)))
        self.assertEqual(cell_02, (f.process_cell(0, 2), f.count_neighbours(0, 2)))
        self.assertEqual(cell_03, (f.process_cell(0, 3), f.count_neighbours(0, 3)))
        self.assertEqual(cell_04, (f.process_cell(0, 4), f.count_neighbours(0, 4)))

        self.assertEqual(cell_10, (f.process_cell(1, 0), f.count_neighbours(1, 0)))
        self.assertEqual(cell_11, (f.process_cell(1, 1), f.count_neighbours(1, 1)))
        self.assertEqual(cell_12, (f.process_cell(1, 2), f.count_neighbours(1, 2)))
        self.assertEqual(cell_13, (f.process_cell(1, 3), f.count_neighbours(1, 3)))
        self.assertEqual(cell_14, (f.process_cell(1, 4), f.count_neighbours(1, 4)))

        self.assertEqual(cell_20, (f.process_cell(2, 0), f.count_neighbours(2, 0)))
        self.assertEqual(cell_21, (f.process_cell(2, 1), f.count_neighbours(2, 1)))
        self.assertEqual(cell_22, (f.process_cell(2, 2), f.count_neighbours(2, 2)))
        self.assertEqual(cell_23, (f.process_cell(2, 3), f.count_neighbours(2, 3)))
        self.assertEqual(cell_24, (f.process_cell(2, 4), f.count_neighbours(2, 4)))

        self.assertEqual(cell_30, (f.process_cell(3, 0), f.count_neighbours(3, 0)))
        self.assertEqual(cell_31, (f.process_cell(3, 1), f.count_neighbours(3, 1)))
        self.assertEqual(cell_32, (f.process_cell(3, 2), f.count_neighbours(3, 2)))
        self.assertEqual(cell_33, (f.process_cell(3, 3), f.count_neighbours(3, 3)))
        self.assertEqual(cell_34, (f.process_cell(3, 4), f.count_neighbours(3, 4)))

        self.assertEqual(cell_40, (f.process_cell(4, 0), f.count_neighbours(4, 0)))
        self.assertEqual(cell_41, (f.process_cell(4, 1), f.count_neighbours(4, 1)))
        self.assertEqual(cell_42, (f.process_cell(4, 2), f.count_neighbours(4, 2)))
        self.assertEqual(cell_43, (f.process_cell(4, 3), f.count_neighbours(4, 3)))
        self.assertEqual(cell_44, (f.process_cell(4, 4), f.count_neighbours(4, 4)))


if __name__ == '__main__':
    unittest.main()