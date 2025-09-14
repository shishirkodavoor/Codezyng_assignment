import sys
from pathlib import Path

# Add current directory to Python path
sys.path.append(str(Path(__file__).parent))

def test_imports():
    """test if modules can be imported"""
    print(" Testing imports...")
    
    try:
        from utils.driver_manager import DriverManager
        print(" DriverManager imported succesfully")
    except Exception as e:
        print(f" DriverManager import failed: {e}")
        return False
    
    try:
        from utils.config_reader import ConfigReader
        print(" ConfigReader imported succesfully")
    except Exception as e:
        print(f" ConfigReader import failed: {e}")
        return False
    
    try:
        from selenium import webdriver
        print(" Selenium imported succesfully")
    except Exception as e:
        print(f" Selenium import failed: {e}")
        return False
    
    try:
        from loguru import logger
        print(" Loguru imported succesfully")
    except Exception as e:
        print(f" Loguru import failed: {e}")
        return False
    
    return True

def test_config():
    """test config loading"""
    print("\nTesting configuration...")
    
    try:
        from utils.config_reader import ConfigReader
        config = ConfigReader()
        
        print(f" Base URL: {config.get_base_url()}")
        print(f" Browser: {config.get_browser()}")
        print(f" Headless: {config.get_headless()}")
        
        return True
    except Exception as e:
        print(f" Configuration test failed: {e}")
        return False

def test_driver_creation():
    """test driver creation (without starting browser)"""
    print("\nTesting driver creation...")
    
    try:
        from utils.driver_manager import DriverManager
        driver_manager = DriverManager(browser="chrome", headless=True)
        print(" DriverManager created succesfully")
        
        print(" Driver creation test passed (skipped actual browser startup)")
        return True
    except Exception as e:
        print(f" Driver creation test failed: {e}")
        return False

def main():
    """Main demo function"""
    print(" E-commerce Automation Framework - Simple Demo")
    print("=" * 55)
    
    success = True
    
    # Test imports
    if not test_imports():
        success = False
    
    # Test configuration
    if not test_config():
        success = False
    
    # Test driver creation
    if not test_driver_creation():
        success = False
    
    print("\n" + "=" * 55)
    if success:
        print(" All tests passed!! Framework is ready to use.")
        print("\n Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Run full demo: python demo.py")
        print("3. Run tests: python run_tests.py --suite smoke")
    else:
        print(" Some tests failed. Please check the errors above.")
    
    return success

if __name__ == "__main__":
    main()
