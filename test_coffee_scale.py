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
        cs._currentWeight = 20
        cs._threshold = 5
        shouldLogItem = cs.shouldLogWeight(21)
        self.assertEquals(False, shouldLogItem)

    def test_whenValueChangesGreaterThanThreshold_LogIsWritten(self):
        cs._currentWeight = 1
        cs._threshold = 5
        shouldLogItem = cs.shouldLogWeight(7)
        self.assertEquals(True, shouldLogItem)

    def test_whenValueIsAtLowThreshold_PotHasBeenLifted(self):
        cs._lowThreshold = 10
        cs._currentWeight = 0
        potIsLifted = cs.potIsLifted()
        self.assertEquals(True, potIsLifted)

    def test_whenLoopedConfiguredTimes_PostMessageToHipchat(self):
        cs._loopCount = 40
        self.assertEquals(True, cs.shouldPostToHipChat())

    def test_whenLoopCountNotEqualConfiguredTimes_MessageNotPostedToHipChat(self):
        for i in range(40):
            cs._loopCount = i
            self.assertEquals(False, cs.shouldPostToHipChat())

    def test_hipchatUserIsGiven_WithAMultipleOfNumberOfMugsInPot(self):
        cs._currentWeight = 2600
        self.assertEquals(6, cs.getAvailableMugs())

        cs._currentWeight = 2264
        self.assertEquals(5, cs.getAvailableMugs())

        cs._currentWeight = 1999
        self.assertEquals(4, cs.getAvailableMugs(), "{0} did not equal 4 mugs".format(cs._currentWeight))

        cs._currentWeight = 1733
        self.assertEquals(3, cs.getAvailableMugs())

        cs._currentWeight = 1467
        self.assertEquals(2, cs.getAvailableMugs())

        cs._currentWeight = 1201
        self.assertEquals(1, cs.getAvailableMugs())

    def test_whenWeightWithin90PercentMinus10GramsOfFullMug_RegisterNextAvailableMug(self):
        cs._currentWeight = 1164
        self.assertEquals(1, cs.getAvailableMugs())

        cs._currentWeight = 1430
        self.assertEquals(2, cs.getAvailableMugs())

        cs._currentWeight = 1696
        self.assertEquals(3, cs.getAvailableMugs())

        cs._currentWeight = 1962
        self.assertEquals(4, cs.getAvailableMugs())

        cs._currentWeight = 2228
        self.assertEquals(5, cs.getAvailableMugs())

    def test_hipChatMessage_IncludesNumberOfMugs_AndWeightOfPot(self):
        cs._currentWeight = 1173
        params = cs.getHipchatParameters()
        totalAvailableMugs = len(cs._mugAmounts)
        self.assertEquals("{0} / {1}".format(
            cs.getAvailableMugs(), totalAvailableMugs), params['from'])

        self.assertEquals("{0} / {1}".format(
            cs._currentWeight, cs._mugAmounts[totalAvailableMugs - 1]), 
            params['message'])


    @unittest.skip("Only run manually if testing Initial State Integration")
    def test_InitialStateIntegration(self):
        for j in range(5):
            for i in range(5, 30, 2):
                cs._currentWeight = i
                cs.logToInitialState()

def main():
    unittest.main()

if __name__ == '__main__':
    main()

