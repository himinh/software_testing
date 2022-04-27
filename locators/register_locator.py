class RegisterLocator():
  page_url = 'https://social-network-awesome.herokuapp.com/'
  xpath_sign_up_btn='//a[text()="Sign Up"]'
  first_name_input='#firstname'
  last_name_input='#lastname'
  email_input='input[name=email]'
  password_input='input[name=password]'
  submit_btn='//button[text()="Register"]'
  error_message=".alert.alert-danger .message"
  success_message=".alert.alert-success .message"
