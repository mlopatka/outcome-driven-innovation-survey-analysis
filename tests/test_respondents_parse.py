from utils import respondents_parse

import numpy as np
import pandas as pd
import sompy
from utils.respondents_parse import *

PATH_TO_TEST_RESPONSES = \
    '/Users/mlopatka/repos/outcome-driven-innovation-survey-analysis/sample-survey-data.csv'

QUESTIONAIRE_SCHEMA = ['sat_Q6', 'sat_Q7', 'sat_Q4', 'sat_Q5', 'sat_Q2', 'sat_Q3', 'sat_Q1',
                       'Org.Size', 'imp_pers_Q5', 'row ID', 'Clients', 'imp_pers_Q4',
                       'Consultant', 'imp_pers_Q6', 'imp_pers_Q7', 'imp_pers_Q1',
                       'imp_pers_Q2', 'imp_pers_Q3', 'Team.Manager', 'Team.Size',
                       'imp_org_Q1', 'imp_org_Q3', 'imp_org_Q2', 'imp_org_Q5',
                       'imp_org_Q4', 'imp_org_Q7', 'imp_org_Q6']


def test_csv_parser():
    a = respondents_parse.load_csv(PATH_TO_TEST_RESPONSES)
    assert len(a) == 183
    assert set(a[0].keys()) & set(QUESTIONAIRE_SCHEMA)
    assert a[-1]['row ID'] == '81c6edcaa322381a43b232c147d57574'


def test_sompy_basic():
    # Evaluates the basic functioning of the sompy library as a prerequisite for further analysis
    d1 = pd.DataFrame(data=1 * np.random.rand(100, 2))
    d1.values[:, 1] = (d1.values[:, 0][:, np.newaxis] + .42 * np.random.rand(100, 1))[:, 0]

    d2 = pd.DataFrame(data=1 * np.random.rand(100, 2) + 1)
    d2.values[:, 1] = (-1 * d2.values[:, 0][:, np.newaxis] + .62 * np.random.rand(100, 1))[:, 0]

    data1 = np.concatenate((d1, d2))

    som = sompy.SOMFactory.build(data1, [20, 20], mask=None, mapshape='planar', lattice='rect', normalization='var',
                                 initialization='pca', neighborhood='gaussian', training='batch', name='sompy')
    som.train(n_job=1, verbose=None)
    assert som is not None

    cl = som.cluster(n_clusters=2)
    # Verify only two labels fo two clusters.
    assert set(cl) == set([0, 1])
    ones = 0
    zeros = 0
    for i in cl:
        if i == 0:
            zeros += 1
        if i == 1:
            ones += 1
        else:
            return False
    # Verify correct classification into two equal sized clusters.
    assert ones == zeros


def test_response_object_create():
    a = load_csv(PATH_TO_TEST_RESPONSES)
    test_response = SingleSurveyResponse(a[-1])
    assert test_response.client_id == '81c6edcaa322381a43b232c147d57574'
    assert test_response.answers['Team.Size'] == "2-4"
    assert test_response.complete

    test_response = SingleSurveyResponse(a[0])
    assert test_response.client_id == "f311a55b829601478f2416a5e34fb26e"
    # TODO: reinstate this test.
    # assert not test_response.complete
