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

def main():
    unittest.main()

if __name__ == '__main__':
    main()

