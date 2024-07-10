    def testMultipleMatrixes(self):
        convertedMatrix= Converter.convertMatrix("3 3\n*..\n...\n3 3\n*..\n.**")
        self.assertEqual(convertedMatrix, "Field #1:\n*10\n110\nField #2:\n*32\n2**\n")