# Author: Martin Lopatka (mlopatka@mozilla.com)

import csv


def load_csv(path_to_file):
    list_of_rows = []
    with open(path_to_file, 'rb') as csvfile:
        response_reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
        for row in response_reader:
            list_of_rows.append(row)
    return list_of_rows


def populate_responses(survey_results_file):
    raw_response_list = load_csv(survey_results_file)
    response_list = []
    for i in raw_response_list:
        response_list.append(SingleSurveyResponse(i))
    return response_list


def impute_missing_answer(singe_question):
    # TODO: implement regression based multiple imputation as per
    #  James R, Carpenter and Michael G. Kenward solution.
    out_question = []
    for q in singe_question:
        if q is None:
            q = 3.0


def impute_missing_responses(responses):
    for row in responses:
        impute_missing_answer(row)


class SingleSurveyResponse:
        """
        Survery Respondent response data 
        
        :param client_id: the survey participant id, a unique but anonymous 
            identifer for the survery participant.
        :param answers: respondent answers to the survey questions, 
            represented as a list of XXX ordered ,
            as inputs and m cols as input features
        :param complete: Boolean value indicating whether all questions were answered.
        """
        def __init__(self, indict):
            self.answers = {}
            self.client_id = indict["row ID"]
            for k, v in indict.iteritems():
                if k != "row ID":
                    self.answers[k] = v
            # TODO: Verify this logic!!!
            self.complete = all([len(x) >= 1 and x for x in self.answers])

