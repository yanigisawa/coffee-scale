import unittest
import coffee_scale as cs

class CoffeeTest(unittest.TestCase):
    def setUp(self):
        self.scale = cs.CoffeeScale()

    def test_whenValueChangesLessThanThreshold_LogIsNotWritten(self):
        self.scale._currentWeight = 20
        self.scale._threshold = 5
        shouldLogItem = self.scale.shouldLogWeight(21)
        self.assertEquals(False, shouldLogItem)

    def test_whenValueChangesGreaterThanThreshold_LogIsWritten(self):
        self.scale._currentWeight = 1
        self.scale._threshold = 5
        shouldLogItem = self.scale.shouldLogWeight(7)
        self.assertEquals(True, shouldLogItem)

    def test_whenValueIsAtLowThreshold_PotHasBeenLifted(self):
        potIsLifted = self.scale.potIsLifted()
        self.assertEquals(True, potIsLifted)

    def test_whenLoopedConfiguredTimes_PostMessageToHipchat(self):
        self.scale._loopCount = 40
        self.assertEquals(True, self.scale.shouldPostToHipChat())

    def test_whenLoopCountNotEqualConfiguredTimes_MessageNotPostedToHipChat(self):
        for i in range(40):
            self.scale._loopCount = i
            self.assertEquals(False, self.scale.shouldPostToHipChat())

    def test_hipchatUserIsGiven_WithAMultipleOfNumberOfMugsInPot(self):
        self.scale._currentWeight = 2264
        self.assertEquals(5, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1999
        self.assertEquals(4, self.scale.getAvailableMugs(), "{0} did not equal 4 mugs".format(self.scale._currentWeight))

        self.scale._currentWeight = 1733
        self.assertEquals(3, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1467
        self.assertEquals(2, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1201
        self.assertEquals(1, self.scale.getAvailableMugs())

    def test_whenWeightWithin90PercentMinus10GramsOfFullMug_RegisterNextAvailableMug(self):
        self.scale._currentWeight = 1164
        self.assertEquals(1, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1430
        self.assertEquals(2, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1696
        self.assertEquals(3, self.scale.getAvailableMugs())

        self.scale._currentWeight = 1962
        self.assertEquals(4, self.scale.getAvailableMugs())

        self.scale._currentWeight = 2228
        self.assertEquals(5, self.scale.getAvailableMugs())

    def test_hipChatMessage_IncludesNumberOfMugs_AndWeightOfPot(self):
        self.scale._currentWeight = 1173
        params = self.scale.getHipchatParameters()
        totalAvailableMugs = len(self.scale._mugAmounts)
        self.assertEquals("{0} / {1}".format(
            self.scale.getAvailableMugs(), totalAvailableMugs), params['from'])

        self.assertEquals("{0} / {1}".format(
            self.scale._currentWeight, self.scale._mugAmounts[totalAvailableMugs - 1]), 
            params['message'])

    def test_environmentVariables_AreSet(self):
        self.assertTrue(self.scale.initialStateKey)
        self.assertTrue(self.scale.hipchatKey)
        self.assertTrue(self.scale.environment)
        self.assertTrue(self.scale.ledServiceUrl)


    @unittest.skip("Only run manually if testing Initial State Integration")
    def test_InitialStateIntegration(self):
        for j in range(5):
            for i in range(5, 30, 2):
                self.scale._currentWeight = i
                self.scale.logToInitialState()

def main():
    unittest.main()

if __name__ == '__main__':
    main()

