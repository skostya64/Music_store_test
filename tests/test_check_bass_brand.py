

def test_check_bass_brand(app):
    app.admin_panel_login_page.open()
    app.check_four_strings_bass_page.click_menu_bass_guitars()
    app.check_four_strings_bass_page.click_electric_bass_guitars()
    app.check_four_strings_bass_page.click_four_strings()
    app.check_bass_name_page.select_name_brand()