class AnonymousSurvey():
    responses = []
    """Collect anonymous answers to a survey quesion"""
    def __init__(self,question):
        """store a question,and prepare to store responses."""
        self.responses = []  # define a empty list,here the empty list can't define
        self.question = question  # pass the question from class instance

    def show_question(self):
        """Show the survey question"""
        print(question)

    def store_response(self,new_response):
        """store a single response to the survey"""
        self.responses.append(new_response)

    def show_results(self):
        """show all the responses that have been given."""
        print("Survey results: ")
        for response in responses:
            print('-' + response)





