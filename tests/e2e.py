from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from selenium import webdriver
from selenium.webdriver.common.by import By


# ---------------------------------------------------------------------------------
# -------------------- Test properties --------------------------------------------
# ---------------------------------------------------------------------------------


TEST_SUBJECT_PROT = 'http'  # no certificates
TEST_SUBJECT_HOST = 'scores'  # docker compose service name
TEST_SUBJECT_PORT = '5000'  # internal docker port

TEST_NAME = '[WoG] Test scores are displayed'


# ---------------------------------------------------------------------------------
# ------------------- Setting up drivers ------------------------------------------
# ---------------------------------------------------------------------------------

def get_firefox_driver():
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-gpu")
    firefox_options.set_capability('se:name', '{} (FirefoxTests)'.format(TEST_NAME))

    return webdriver.Remote('http://selenium-hub:4444', options=firefox_options)


def get_chrome_driver():
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.set_capability('se:name', '{} (ChromeTests)'.format(TEST_NAME))

    return webdriver.Remote('http://selenium-hub:4444', options=chrome_options)


def get_edge_driver():
    edge_options = EdgeOptions()
    edge_options.add_argument("--headless")
    edge_options.add_argument("--disable-gpu")
    edge_options.set_capability('se:name', '{} (EdgeTests)'.format(TEST_NAME))

    return webdriver.Remote('http://selenium-hub:4444', options=edge_options)


# ---------------------------------------------------------------------------------
# ------------------- Setting up PageObjectModels ---------------------------------
# ---------------------------------------------------------------------------------

class ScoresPage:
    # https://www.selenium.dev/documentation/test_practices/encouraged/page_object_models/
    driver: webdriver.Remote

    def __init__(self, webdriver: webdriver.Remote):
        self.driver = webdriver
        if 'Scores Game' != webdriver.title:
            raise Exception("This is not scores page! Current page is: {}".format(webdriver.title))

    def get_scores(self) -> list[dict[str, str]]:
        table = self.driver.find_element(By.TAG_NAME, 'table')
        table_rows = table.find_elements(By.TAG_NAME, 'tr')

        scores = []
        i = 0
        for row in table_rows:
            if 0 == i:
                continue  # skip headers

            cells = row.find_elements(By.TAG_NAME, 'td')
            if len(cells) != 2:
                raise Exception("The scores table should consist of 2 columns")

            scores.append({
                'name': cells[0].text,
                'score': cells[1].text,
            })

        return scores


# ---------------------------------------------------------------------------------
# ------------------- Expected test result ----------------------------------------
# ---------------------------------------------------------------------------------

def get_expected_data():
    return [
        {'name': 'Damian', 'score': '1000'},
        {'name': 'Patryk', 'score': '900'},
        {'name': 'Matthew', 'score': '800'},
        {'name': 'Don Kichot', 'score': '700'},
    ]

# ---------------------------------------------------------------------------------
# ------------------- Test --------------------------------------------------------
# ---------------------------------------------------------------------------------


print('Preparing drivers..')

drivers = [
    ('chrome', get_chrome_driver()),
    ('firefox', get_firefox_driver()),
    ('edge', get_edge_driver()),
]

print('Drivers ready..')

for name, driver in drivers:
    print("Running tests on driver ", name)
    try:
        driver.get("{}://{}:{}".format(TEST_SUBJECT_PROT, TEST_SUBJECT_HOST, TEST_SUBJECT_PORT))

        scores_page = ScoresPage(driver)

        i = 0
        for score in scores_page.get_scores():
            assert score == get_expected_data()[i]['name']
            assert score == get_expected_data()[i]['score']
            i += 1

    finally:
        driver.quit()
