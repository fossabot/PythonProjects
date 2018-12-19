import unittest as ut
import random
import logging
import traceback as tb

# Logging Levels - DEBUG, INFO, WARNING, ERROR, CRITICAL

# Configuration
logging.basicConfig(filename='application.log',
                    filemode='w',
                    format="%(asctime)s : %(levelname)s => %(message)s",
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')

print('-' * 70)

# Function to validate the mail id
def val_mail_id(mail_id):
    status = 'Invalid'

    if mail_id.endswith('@cypress.com', 5):
        status = 'Valid'

    return status

chk_palin = lambda string: string == string[::-1]

'''
Assertions

assertTrue
assertFalse
assertEqual
assertNotEqual
assertIn
assertNotIn
assertListEqual
assertTupleEqual
assertDictEqual
'''

class ut1(ut.TestCase):
    def setUp(self):
        logging.debug('Executing {}'.format(self.shortDescription()))

    def tearDown(self):
        logging.debug('{} Completed'.format(self.shortDescription()))

    def test_mail_id_1(self):
        'TEST_MAIL_ID_1'
        try:
            self.assertEqual(val_mail_id('justin@cypress.com'),
                             'Valid')
            self.assertAlmostEqual(1.2345678, 1.23456789, 5)
        except Exception as e:
            logging.error(tb.format_exc())

    @ut.skip('skipping')
    def test_mail_id_2(self):
        'TEST_MAIL_ID_2'
        try:
            self.assertListEqual(val_mail_id('just@cypress.com'),
                                 ['Valid', 'Invalid'])
        except Exception as e:
            logging.error(tb.format_exc())

    def test_random(self):
        'TEST_RANDOM'
        try:
            self.assertIn(random.randrange(100, 600, 100),
                          [100, 200, 300, 400, 500])
        except Exception as e:
            logging.error(tb.format_exc())

class ut2(ut.TestCase):
    def setUp(self):
        logging.debug('Executing {}'.format(self.shortDescription()))

    def tearDown(self):
        logging.debug('{} Completed'.format(self.shortDescription()))

    def test_palin_1(self):
        'TEST_PALIN_1'
        try:
            self.assertTrue(chk_palin('php'))
        except Exception as e:
            logging.error(tb.format_exc())

    @ut.skip('skipping')
    def test_palin_2(self):
        'TEST_PALIN_2'
        try:
            self.assertTrue(chk_palin('phpa'))
        except Exception as e:
            logging.error(tb.format_exc())

# Test Suite
def create_test_suite():
    suite = ut.TestSuite()

    # Add the test
    #suite.addTest(ut1('test_mail_id_1'))
    #suite.addTest(ut2('test_palin_1'))
    suite = ut.TestLoader().loadTestsFromTestCase(ut1)
    return suite

if __name__ == '__main__':
    # ut.main()
    runner = ut.TextTestRunner()
    runner.run(create_test_suite())

print('-' * 70)
