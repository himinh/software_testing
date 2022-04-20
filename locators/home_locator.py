class HomeLocator():
  login_page_url = 'https://social-network-awesome.herokuapp.com/auth/login'

  textarea_button = '#buttonPostFormModal'
  textarea_post = '#postTextarea'

  text_post = 'Good morning! '
  submit_create_post = '#submitCreatePost'

  first_post = '.posts .post:first-child'
  posted_post = '.posts .post:first-child .post_body span'

  container_like_first_post = '.posts .post:first-child .pink .post_button-container_content'
  like_first_post = '.posts .post:first-child button.like-button'
  liked_first_post_active = '.posts .post:first-child .pink .active'

  pin_first_post = '.posts > .post:first-child button.button-pinned-post'
  confirm_pinned_post = '#submitPinPost'
  pined_text = '.posts .post:first-child .pinnedText'

  delete_first_post = '.posts > .post:first-child button.button-delete-post'
  confirm_deleted_post = '#submitDeletePost'
