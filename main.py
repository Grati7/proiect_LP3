from selenium import webdriver
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_facebook_login_post(email, password, image_path, post_text):
    start_time = time.time()  # Salvează timpul de început

    # Inițializează driverul Chrome și accesează pagina de login Facebook
    driver_service = webdriver.ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=driver_service)
    driver.get('https://www.facebook.com/')

    def click(args):
        driver.execute_script("arguments[0].click();", args)

    # Login
    try:
        # Găsește câmpurile de email și parolă, și butonul de login
        email_field = driver.find_element(By.ID, 'email')
        password_field = driver.find_element(By.ID, 'pass')
        login_button = driver.find_element(By.NAME, 'login')

        # Completează câmpurile de email și parolă și face click pe butonul de login
        email_field.send_keys(email)
        password_field.send_keys(password)

        click(login_button)

        # Așteaptă câteva secunde pentru a permite finalizarea autentificării
        time.sleep(5)

        # Verifică dacă autentificarea a fost reușită
        if "Facebook" in driver.title:
            print("Login reușit")
        else:
            print("Login nereușit")
            driver.quit()  # Închide driverul
            return

    except Exception as e:
        print(f"Login nereușit: {e}")
        driver.quit()  # Închide driverul
        return

    # Postare a unei imagini cu descriere
    try:
        # Găsește caseta de postare și face click pe ea
        go_home = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@aria-label='Home']"))
        )
        click(go_home)

        # Găsește caseta de postare și face click pe ea
        post_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[contains(text(), \"What's on your mind,\")]"))
        )
        click(post_box)

        # TODO Sa deschida dialogul de selectie imagine si selectare a imaginii
        # button_with_image = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@aria-label=\"Photo/video\"]"))
        # )
        # click(button_with_image)
        #
        # photo_video_button = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(), \"Add Photos/Videos\")]"))
        # )
        # click(photo_video_button)
        #
        # retries = 3
        # for _ in range(retries):
        #     try:
        #         file_input = WebDriverWait(driver, 10).until(
        #             EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
        #         )
        #         file_input.send_keys(image_path)
        #         click(file_input)
        #         break
        #     except StaleElementReferenceException:
        #         continue

        # Apasa pe text area pentru a scrie textul postarii
        text_area = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[@aria-label=\"What's on your mind, Petre?\"]"))
        )
        click(text_area)
        text_area.send_keys(post_text)

        # Apasă pe butonul de postare si trimite postarea pe feed
        post_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@aria-label='Post']"))
        )
        click(post_button)

        print("Postare reușită")

    except Exception as e:
        print(f"Postare nereușită: {e}")

    finally:
        driver.quit()  # Închide driverul
        end_time = time.time()  # Salvează timpul de sfârșit
        print(f"Timp total de execuție: {end_time - start_time:.2f} secunde")


# Înlocuiește cu datele tale de test și calea imaginii
test_email = "proiectlp33@gmail.com"
test_password = "zxcvbnm123()"
test_image_path = "C:/Users/iulia/OneDrive/Pictures/Saved Pictures/imagine.jpeg"
test_post_text = "Aceasta este o postare de test."

# Apelează funcția de testare cu datele specificate
test_facebook_login_post(test_email, test_password, test_image_path, test_post_text)
