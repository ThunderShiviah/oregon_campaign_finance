""" An ORESTAR (Oregon Campaign Finance Database) python API wrapper using
requests. Written for Hack Oregon Campaign Finance Project.

Summer 2015

Author: Thunder Shiviah"""

import requests


# Multiple strings are concatenated at compile time. See 
# https'://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation
website_base = ('https://secure.sos.state.or.us/orestar/'
                'gotoPublicTransactionSearchResults.do')
 
payload = { 'cneSearchButtonName': 'search',
            'cneSearchPageIdx': '',
            'cneSearchContributorTypeName': '',
            'cneearchTranTypeName': '', 
            'cneSearchTranSubTypeName': '',
            'cneSearchTranPurposeName': '',
            'cneSearchFilerCommitteeId': '',
            'cneSearchFilerCommitteeTxt': '',
            'cneSearchFilerCommitteeTxtSearchType': '',
            'cneSearchTranStartDate': '',
            'cneSearchTranEndDate': '',
            'cneSearchTranFiledStartDate': '' ,
            'cneSearchTranFiledEndDate': '',
            'transactionId': '',
            'cneSearchTranType': '',
            'cneSearchTranAmountFrom': '',
            'cneSearchTranAmountTo': '',
            'cneSearchContributorTxt': '',
            'cneSearchContributorTxtSearchType': '',
            'cneSearchContributorType': '',
            'addressLine1': '',
            'city': '',
            'state': '' ,
            'zip': '',
            'zipPlusFour': '',
            'occupation': '',
            'employer': '',
            'employerCity': '',
            'employerState': ''}

website_excel_request = 'https://secure.sos.state.or.us/orestar/XcelCNESearch'
