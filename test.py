import unittest
from kata04.converter_service import ConverterService

class testCases (unittest.TestCase):

    def testSimpleMatrix(self):
        convertedMatrix= ConverterService.convertMatrix('1 1\n.')
        self.assertEqual(convertedMatrix,"Field #1:\n0\n")

    def test3x3Matrix(self):
        convertedMatrix= ConverterService.convertMatrix("3 3\n...\n...\n...")
        self.assertEqual(convertedMatrix, "Field #1:\n000\n000\n000\n")

    def test3x3Mines(self):
        convertedMatrix= ConverterService.convertMatrix("4 4\n*...\n....\n.*..\n....\n0 0")
        self.assertEqual(convertedMatrix, "Field #1:\n*100\n2210\n1*10\n1110\n")

    def testMultipleMatrixes(self):
        convertedMatrix= ConverterService.convertMatrix("4 4\n*...\n....\n.*..\n....\n3 5\n**...\n.....\n.*...\n0 0")
        self.assertEqual(convertedMatrix, "Field #1:\n*100\n2210\n1*10\n1110\nField #2:\n**100\n33200\n1*100\n")
if __name__ == '__main__':
    unittest.main()