from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # # 打開谷歌地圖
        # page.goto("https://www.google.com/maps")

        # # 等待搜索欄出現
        # page.get_by_placeholder("Search Google Maps").click()

        # # # 在搜索欄輸入HKU
        # page.fill("Search Google Maps", "HKU")

        # # # 按下回車鍵進行搜索
        # page.press("Search Google Maps", "Enter")

        # # # 等待搜索結果出現
        # page.wait_for_load_state("networkidle")

        # # 確保跳轉到搜索結果頁面
        # print("搜索完成，已跳轉到搜索結果頁面")


        page.goto("https://demo.playwright.dev/todomvc/")
        page.get_by_placeholder("What needs to be done?").click()
        page.get_by_placeholder("What needs to be done?").fill("hello")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.get_by_placeholder("What needs to be done?").fill("world")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.get_by_placeholder("What needs to be done?").fill("yes")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.get_by_placeholder("What needs to be done?").fill("no")
        page.get_by_placeholder("What needs to be done?").press("Enter")

        page.get_by_role("listitem").filter(has_text="world").get_by_role("checkbox", name="Toggle Todo").check()
        page.get_by_role("button", name="Clear completed").click()
        # 關閉瀏覽器
        browser.close()

# 執行主函數
if __name__ == "__main__":
    main()
