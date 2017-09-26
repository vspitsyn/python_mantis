def test_login(app):
    app.session.ensure_login("admin","secret")
    #app.session.ensure_login("admin", "secret")
    #app.session.logout()
    assert app.session.is_logget_in_as()=="admin"