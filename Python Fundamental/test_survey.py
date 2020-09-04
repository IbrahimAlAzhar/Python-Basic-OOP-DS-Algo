import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase): # this class is inherits from unittest.TestCase
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods"""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question) # setup method store the values initially for all method
        self.responses = ['English','Spanish','German']

    def test_store_single_response(self):
        """Test the single response is stored properly"""
        question = "What language did you first learn to speak"
        # my_survey = AnonymousSurvey(question) # creating a instance 'my_survey' with the question to test the behavior of the class
        my_survey.store_response(self.responses[0]) # insert the dummy data 'English'
        self.assertIn(self.responses[0],my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        #question = "What language did you first learn to speak?" # we don't need define these here,we define in setup method
        #my_survey = AnonymousSurvey(question) # create a instance of the class and pass the parameter 'question'
        #responses = ['English','Spanish','German'] # define a list where describe the languages
        for i in responses:
            my_survey.store_response(i)  # append the responses in 'responses' list in 'my_survey' instance
        for i in responses:
            self.assertIn(i, my_survey.responses) # check every items in list(just now which one we create) with the 'responses' list in 'my_survey' instance

unittest.main()
