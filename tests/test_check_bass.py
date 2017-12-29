
def test_check_four_strings_bass(app):
    app.admin_panel_login_page.open()
    app.check_four_strings_bass_page.click_menu_bass_guitars()
    app.check_four_strings_bass_page.click_electric_bass_guitars()
    app.check_four_strings_bass_page.click_four_strings()
    app.check_four_strings_bass_page.check_quantity_four_strings_guitars()
    assert len(check_quantity_four_strings_guitars) == 12