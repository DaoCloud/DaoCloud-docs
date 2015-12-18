---
form:
  fields:
    -
      name: username
      type: text
      placeholder: "Choose a username"
      validate:
        required: true

    -
      name: email
      type: text
      placeholder: "Enter your email"
      validate:
        required: true

    -
      name: password1
      type: password
      label: Enter a password
      validate:
        required: true

    -
      name: password2
      type: password
      label: Enter the password again
      validate:
        required: true


  buttons:
      -
          type: submit
          value: Submit
      -
          type: reset
          value: Reset

  process:
      register_user: true
      message: "You are logged in"
---

# Register
