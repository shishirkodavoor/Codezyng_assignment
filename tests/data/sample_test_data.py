
from utils.data_utils import DataUtils


def create_sample_test_data():
    """Create sample test data files - Shishir's implementation"""
    data_utils = DataUtils()
    
    # Login test data - used by Rajesh and Priya
    login_data = [
        {"username": "demo@opencart.com", "password": "demo", "expected": "success"},
        {"username": "shishir@codezyng.com", "password": "wrong", "expected": "failure"},
        {"username": "", "password": "demo", "expected": "failure"},
        {"username": "demo@opencart.com", "password": "", "expected": "failure"},
        {"username": "test@codezyng.com", "password": "codezyng", "expected": "failure"},
    ]
    
    # Registration test data - Amit's test cases
    registration_data = [
        {
            "first_name": "Shishir",
            "last_name": "Kodavoor",
            "email": "shishir.kodavoor@test.com",
            "telephone": "8310650475",
            "password": "password123",
            "confirm_password": "password123",
            "expected": "success"
        },
        {
            "first_name": "Priya",
            "last_name": "Sharma",
            "email": "priya.sharma@test.com",
            "telephone": "9123456789",
            "password": "password456",
            "confirm_password": "password456",
            "expected": "success"
        },
        {
            "first_name": "Rajesh",
            "last_name": "Patel",
            "email": "rajesh.patel@test.com",
            "telephone": "9555555555",
            "password": "password789",
            "confirm_password": "different_password",
            "expected": "failure"
        }
    ]
    
    # Checkout test data - Deepak's test cases
    checkout_data = [
        {
            "first_name": "Shishir",
            "last_name": "Kodavoor",
            "company": "Codezyng Technologies",
            "address_1": "123 MG Road",
            "address_2": "Apt 1",
            "city": "Udupi",
            "postcode": "560001",
            "country": "India",
            "region": "Karnataka",
            "email": "shishir.kodavoor@codezyng.com",
            "telephone": "9876543210",
            "expected": "success"
        },
        {
            "first_name": "Priya",
            "last_name": "Sharma",
            "company": "Digital Innovations",
            "address_1": "456 Connaught Place",
            "address_2": "Suite 2",
            "city": "New Delhi",
            "postcode": "110001",
            "country": "India",
            "region": "Delhi",
            "email": "priya.sharma@test.com",
            "telephone": "9123456789",
            "expected": "success"
        }
    ]
    
    # Product search data - Amit's test cases
    search_data = [
        {"search_term": "iPhone", "expected_results": True},
        {"search_term": "Samsung", "expected_results": True},
        {"search_term": "MacBook", "expected_results": True},
        {"search_term": "Canon", "expected_results": True},
        {"search_term": "Nikon", "expected_results": True},
        {"search_term": "xyz123nonexistent", "expected_results": False},
    ]
    
    # Coupon codes - Rajesh's test data
    coupon_data = [
        {"code": "WELCOME10", "discount": 10, "type": "percentage"},
        {"code": "SAVE20", "discount": 20, "type": "percentage"},
        {"code": "FREESHIP", "discount": 0, "type": "shipping"},
        {"code": "INVALID123", "discount": 0, "type": "invalid"},
    ]
    
    # Create Excel files
    try:
        data_utils.write_excel_data(login_data, "login_test_data.xlsx", "Login")
        data_utils.write_excel_data(registration_data, "registration_test_data.xlsx", "Registration")
        data_utils.write_excel_data(checkout_data, "checkout_test_data.xlsx", "Checkout")
        data_utils.write_excel_data(search_data, "search_test_data.xlsx", "Search")
        data_utils.write_excel_data(coupon_data, "coupon_test_data.xlsx", "Coupons")
        
        print("Sample test data files created successfully!")
        
    except Exception as e:
        print(f"Failed to create test data files: {str(e)}")


if __name__ == "__main__":
    create_sample_test_data()
