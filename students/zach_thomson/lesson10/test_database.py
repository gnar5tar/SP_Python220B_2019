'''
tests for the MongoDB database assignment
'''
#pylint: disable=C0103
from unittest import TestCase
from database import import_data, show_available_products, show_rentals, MongoDBConnection

def clear_db():
    '''func to clear database of entries'''
    mongo = MongoDBConnection()

    with mongo:
        db = mongo.connection.media
        product_db = db['product']
        customer_db = db['customer']
        rentals_db = db['rentals']
        product_db.drop()
        customer_db.drop()
        rentals_db.drop()

class MongoDBTest(TestCase):
    '''tests for basic operations'''

    def test_import_data(self):
        '''tests csv files are imported correctly with
        correct tuples being returned'''
        clear_db()
        test_import = import_data('csv_files', 'product_file.csv',
                                  'customer_file.csv', 'rental_file.csv')
        self.assertEqual(test_import, [(4, 2, 2), (0, 0, 0)])


    def test_import_data_failure(self):
        '''tests exception handing on import data function'''
        clear_db()
        test_import = import_data('csv_files', 'nofile1.csv',
                                  'nofile2.csv', 'nofile3.csv')
        self.assertEqual(test_import, [(0, 0, 0), (1, 1, 1)])


    def test_show_available_products(self):
        '''tests show_available_products function'''
        clear_db()
        import_data('csv_files', 'product_file.csv', 'customer_file.csv', 'rental_file.csv')
        actual_output = show_available_products()
        expected_dict = {'prd001':{'description':'60-inch TV stand',
                                   'product_type':'livingroom', 'quantity_available':'3'},
                         'prd002':{'description':'L-shaped sofa',
                                   'product_type':'livingroom', 'quantity_available':'1'},
                         'prd004':{'description': '60-inch dining table',
                                   'product_type': 'diningroom', 'quantity_available': '2'}}
        self.assertEqual(actual_output, expected_dict)


    def test_show_rentals(self):
        '''tests show_rentals function'''
        clear_db()
        import_data('csv_files', 'product_file.csv', 'customer_file.csv', 'rental_file.csv')
        actual_output = show_rentals('prd002')
        expected_dict = {'user001':{'name':'Elisa Miles', 'address':'4490 Union Street',
                                    'phone_number':'206-922-0882', 'email':'elisa.miles@yahoo.com'}}
        self.assertEqual(actual_output, expected_dict)
