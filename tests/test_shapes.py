import unittest
from io import StringIO
import sys
from unittest.mock import patch
import shapes

class MyTestCase(unittest.TestCase):

    def test_area_square(self):
        self.assertEqual(shapes.area_square(4), 16)
        self.assertEqual(shapes.area_square(1), 1)
        self.assertEqual(shapes.area_square(0), 0)

    def test_area_triangle(self):
        self.assertAlmostEqual(shapes.area_triangle(10, 5), 25.0)
        self.assertAlmostEqual(shapes.area_triangle(6, 4), 12.0)
        self.assertAlmostEqual(shapes.area_triangle(0, 4), 0.0)

    def test_area_circle(self):
        self.assertAlmostEqual(shapes.area_circle(3), 3.14 * 3 * 3, places=2)
        self.assertAlmostEqual(shapes.area_circle(1), 3.14, places=2)
        self.assertAlmostEqual(shapes.area_circle(0), 0.0, places=2)

    def test_area_rectangle(self):
        self.assertEqual(shapes.area_rectangle(5, 3), 15)
        self.assertEqual(shapes.area_rectangle(10, 2), 20)
        self.assertEqual(shapes.area_rectangle(0, 7), 0)
        
    def test_4_square(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_square(4)

        self.assertEqual("""****
****
****
****
""",text_capture.getvalue())

    def test_5_square(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_square(10)

        self.assertEqual("""**********
**********
**********
**********
**********
**********
**********
**********
**********
**********
""",text_capture.getvalue())

    def test_6_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_triangle_reversed(3)

        self.assertEqual("""1 1 1 
2 2 
3 
""",text_capture.getvalue())

    def test_7_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_triangle_reversed(5)

        self.assertEqual("""1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5 
""",text_capture.getvalue())

    def test_8_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_triangle(3)

        self.assertEqual("""1 
1 2 
1 2 3 
""",text_capture.getvalue())

    def test_9_triangle(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_triangle(5)

        self.assertEqual("""1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
""",text_capture.getvalue())


    def test_12_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_pyramid(3)

        self.assertEqual("""  *
 ***
*****
""",text_capture.getvalue())

    def test_13_pyramid(self):
        
        text_capture = StringIO()
        sys.stdout = text_capture
        shapes.draw_pyramid(5)

        self.assertEqual("""    *
   ***
  *****
 *******
*********
""",text_capture.getvalue())



if __name__ == '__main__':
    unittest.main()
