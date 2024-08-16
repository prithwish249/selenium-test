from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the webdriver (assuming Chrome)
driver = webdriver.Chrome()

# Navigate to the page containing the form
driver.get("http://localhost:5173/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Fill out the form
try:
    # Project Details
    customer_name = wait.until(EC.presence_of_element_located((By.ID, "customer_name")))
    customer_name.send_keys("Customer Name123")

    work_order_no = driver.find_element(By.ID, "work_order_no")
    work_order_no.send_keys("WO123456")

    work_order_date = driver.find_element(By.ID, "work_order_date")
    work_order_date.send_keys("08-08-2024")

    project_capacity = driver.find_element(By.ID, "project_capacity")
    project_capacity.send_keys("100")

    project_details = driver.find_element(By.ID, "project_details")
    project_details.send_keys("This is a sample project")

    handover_date = driver.find_element(By.ID, "handover_date")
    handover_date.send_keys("08-08-2024")

    completion_certificate = driver.find_element(By.ID, "completion_certificate")
    completion_certificate.send_keys("CC123456")

    warranty_upto = driver.find_element(By.ID, "warranty_upto")
    warranty_upto.send_keys("08-08-2024")

    signed_ic_certificate = driver.find_element(By.ID, "signed_ic_certificate")
    signed_ic_certificate.send_keys("IC123456")

    as_built_drawing = driver.find_element(By.ID, "as_built_drawing")
    as_built_drawing.send_keys("Drawing123")

    # Solar PV Details
    spv_capacity = driver.find_element(By.ID, "spv_capacity")
    spv_capacity.send_keys("50")

    spv_qty = driver.find_element(By.ID, "spv_qty")
    spv_qty.send_keys("100")

    spv_make = driver.find_element(By.ID, "spv_make")
    spv_make.send_keys("SolarCo")

    spv_invoice_nos = driver.find_element(By.ID, "spv_invoice_nos")
    spv_invoice_nos.send_keys("INV123,INV456")

    spv_invoice_date = driver.find_element(By.ID, "spv_invoice_date")
    spv_invoice_date.send_keys("08-08-2024")

    spv_warranty_certificate = driver.find_element(By.ID, "spv_warranty_certificate")
    spv_warranty_certificate.send_keys("WC123456")

    # Battery Details
    battery_capacity = driver.find_element(By.ID, "battery_capacity")
    battery_capacity.send_keys("200")

    battery_qty = driver.find_element(By.ID, "battery_qty")
    battery_qty.send_keys("5")

    battery_make = driver.find_element(By.ID, "battery_make")
    battery_make.send_keys("BatteryCo")

    battery_invoice_nos = driver.find_element(By.ID, "battery_invoice_nos")
    battery_invoice_nos.send_keys("BINV123,BINV456")

    battery_invoice_date = driver.find_element(By.ID, "battery_invoice_date")
    battery_invoice_date.send_keys("08-08-2024")

    battery_warranty_certificate = driver.find_element(By.ID, "battery_warranty_certificate")
    battery_warranty_certificate.send_keys("BWC123456")

    # Inverter Details 
    inverter_location = driver.find_element(By.ID, "location-0")
    inverter_location.send_keys("Main Building")

    inverter_capacity = driver.find_element(By.ID, "capacity-0")
    inverter_capacity.send_keys("75")

    inverter_model_no = driver.find_element(By.ID, "modelNo-0")
    inverter_model_no.send_keys("INVModel123")

    inverter_serial_no = driver.find_element(By.ID, "serialNo-0")
    inverter_serial_no.send_keys("123456")

    inverter_make = driver.find_element(By.ID, "make-0")
    inverter_make.send_keys("InverterCo")

    inverter_purchase_invoice_nos = driver.find_element(By.ID, "purchaseInvoiceNos-0")
    inverter_purchase_invoice_nos.send_keys("INV789,INV101")

    inverter_invoice_date = driver.find_element(By.ID, "inverterInvoiceDate-0")
    inverter_invoice_date.send_keys("08-08-2024")

    inverter_warranty_certificate = driver.find_element(By.ID, "warrantyCertificate-0")
    inverter_warranty_certificate.send_keys("WCI123456")

    # RMS Details 
    rms_sl_no_of_slave = driver.find_element(By.ID, "slNoOfSlave-0")
    rms_sl_no_of_slave.send_keys("789")

    rms_location_of_slave = driver.find_element(By.ID, "locationOfSlave-0")
    rms_location_of_slave.send_keys("Building A")

    rms_sl_no_of_master = driver.find_element(By.ID, "slNoOfMaster-0")
    rms_sl_no_of_master.send_keys("456")

    rms_location_of_master = driver.find_element(By.ID, "locationOfMaster-0")
    rms_location_of_master.send_keys("Building B")

    rms_make = driver.find_element(By.XPATH, "//div[contains(@class, 'rmake')]//input[@id='make']")
    rms_make.send_keys("RMSCo")

    rms_url = driver.find_element(By.ID, "url-0")
    rms_url.send_keys("http://rms.example.com")

    rms_user_id = driver.find_element(By.ID, "userId-0")
    rms_user_id.send_keys("admin")

    rms_password = driver.find_element(By.ID, "password-0")
    rms_password.send_keys("password123")

    rms_invoice_no = driver.find_element(By.ID, "invoiceNo-0")
    rms_invoice_no.send_keys("INV456")

    rms_sim_nos = driver.find_element(By.ID, "simNos-0")
    rms_sim_nos.send_keys("SIM789,SIM101")

    rms_service_provider = driver.find_element(By.ID, "serviceProvider-0")
    rms_service_provider.send_keys("ProviderCo")

    rms_warranty_period = driver.find_element(By.ID, "warrantyPeriod-0")
    rms_warranty_period.send_keys("3 years")

    rms_warranty_certificate = driver.find_element(By.XPATH, "//div[contains(@class, 'rwarrantyCertificate')]//input[@id='warrantyCertificate']")
    rms_warranty_certificate.send_keys("WCR456789")


    rms_contact_no_for_support = driver.find_element(By.ID, "contactNoForSupport-0")
    rms_contact_no_for_support.send_keys("+1234567890")

    # Maintenance Details
    maintenance_frequency = driver.find_element(By.ID, "maintenance_frequency")
    maintenance_frequency.send_keys("Monthly")

    cleaning_frequency = driver.find_element(By.ID, "cleaning_frequency")
    cleaning_frequency.send_keys("Weekly")

    payment_realisation = driver.find_element(By.ID, "payment_realisation")
    payment_realisation.send_keys("30 days")

    remarks = driver.find_element(By.ID, "remarks")
    remarks.send_keys("No additional remarks")

    #  earthing values
    sl_no = driver.find_element(By.ID, "slNo-0")
    sl_no.send_keys("13")

    earth_resistance = driver.find_element(By.ID, "earthResistance-0")
    earth_resistance.send_keys("200")

    # Submit the form
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # Wait for submission confirmation or next page load
    time.sleep(10)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
