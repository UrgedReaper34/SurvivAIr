from playwright.sync_api import sync_playwright
import cv2 as cv
import numpy as np
import time
import io
from PIL import Image
from io import BytesIO


with sync_playwright() as p:
    browser = p.chromium.launch(args=['--start-maximized'], headless=False)
    page = browser.new_page(no_viewport=True)
    page.goto("https://surviv.io/")
    page.is_visible("[data-l10n='ftue-no']")
    page.locator("[data-l10n='ftue-no']").click()
    page.is_visible("[data-l10n='index-cancel']")
    page.locator("[data-l10n='index-cancel']").click()
    page.is_visible("#modal-news > .modal-content > .modal-header > .close >> nth=0")
    page.locator("#modal-news > .modal-content > .modal-header > .close >> nth=0").click()
    page.is_visible("[data-l10n='index-play-battle']")
    page.click("[data-l10n='index-play-battle']")
    for i in range(3):
        page.is_visible("[data-l10n='ftue-next']")
        page.click("[data-l10n='ftue-next']")
    page.wait_for_timeout(1000)
    loop_time = time.time()
    while(True):
        #screenshot = ImageGrab.grab()
        #screenshot = np.array(screenshot)
        #screenshot = screenshot[:, :, ::-1].copy() - 1st option
        #2nd option:
        screenshot = cv.cvtColor(screenshot, cv.COLOR_RGB2BGR)
        #3rd option:
        #screenshot_bytes = page.screenshot()
        #screenshot = Image.open(io.BytesIO(screenshot_bytes))
        #print(screenshot)
        #cv.imshow('Computer Vision', screenshot)

        #print("FPS {}".format(1 / (time.time() - loop_time)))
        #loop_time = time.time()

        if cv.waitKey(1) == ord('q'):
            #cv.destroyAllWindows()
            break

    print('Done')
    
 
    
    
    

#<span data-l10n="ftue-no">No</span>
#<h3 class="close close-footer" data-l10n="index-cancel">Cancel</h3>
#<span class="close close-corner"></span>
# <span class="close close-corner"></span> aka playwright.$(".close.close-corner >> nth=0")
#2) <span class="close close-corner"></span> aka playwright.$("#modal-no-gp > .modal-content > .modal-header > .close >> nth=0")
#<a id="btn-start-battle" class="btn-green btn-darken menu-option btn-battle btn-custom-mode-no-indent" data-l10n="index-play-battle">Battle</a>
#<span data-l10n="ftue-next">NEXT</span>flex