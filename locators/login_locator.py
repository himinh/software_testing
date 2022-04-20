class LoginLocator():
  login_page_url = 'https://social-network-awesome.herokuapp.com/auth/login'
  heading_text = 'h1.title'
  email='#emailLogin'
  password='#passwordLogin'
  submit=".submit-btn"
  error_message=".alert.alert-danger .message"

class LoginAdminLocator():
  email_login='form.sign-in input[name="email"]'
  password_login='form.sign-in input[name="password"]'
  submit_login='//button[text()="Sign in"]'
