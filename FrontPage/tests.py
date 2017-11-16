from django.test import TestCase

# Create your tests here.

class requestTest(TestCase):

    def test_request(self):
        # requestTime, loginModeId, loginFlag, memberType, memberName, businessId
        test_data = {'env':'test','partner_id':'100001','interface_name':'createMember','requestTime':1456993043232,'loginModeId':13,'loginFlag':'testpython','memberType':1,'memberName':'firstpython','businessId':1}
        response = self.client.post('/frontpage/tools/sendRequest/',data=test_data)
