import unittest
import coffee_scale as cs

class CoffeeTest(unittest.TestCase):
    def setUp(self):
        self.parser = cs.getParser()

    def test_empty_args_throws_exception(self):
        with self.assertRaises(SystemExit):
            self.parser.parse_args([])

    def test_files_are_extracted(self):
        args = self.parser.parse_args(['/file/temp', '/file/perm', '1'])
        print(args)
        self.assertEquals(args.tempFile, '/file/temp')
        self.assertEquals(args.permanentDirectory, '/file/perm')
        self.assertEquals(args.logRotateTimeMinutes, 1)

    def test_whenValueChangesLessThanThreshold_LogIsNotWritten(self):
        cs._currentWeight = 1
        cs._threshold = 5
        shouldLogItem = cs.shouldLogWeight(5)
        self.assertEquals(False, shouldLogItem)

    def test_whenValueChangesGreaterThanThreshold_LogIsWritten(self):
        cs._currentWeight = 1
        cs._threshold = 5
        shouldLogItem = cs.shouldLogWeight(6)
        self.assertEquals(True, shouldLogItem)

    def test_whenValueIsAtLowThreshold_PotHasBeenLifted(self):
        cs._lowThreshold = 10
        cs._currentWeight = 0
        potIsLifted = cs.potIsLifted()
        self.assertEquals(True, potIsLifted)

    def test_InitialStateIntegration(self):
        for j in range(5):
            for i in range(5, 30, 2):
                cs._currentWeight = i
                cs.logToInitialState()

def main():
    unittest.main()

if __name__ == '__main__':
    main()

