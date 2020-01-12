<template>
  <div id="login">
    <form class="login">
      <h1 v-if="registerShown === true">Register</h1>
      <h1 v-if="registerShown === false">Welcome</h1>
      <input
        id="email"
        type="text"
        name=""
        placeholder="Email"
        v-model="email"
      />
      <input
        id="steamId"
        type="text"
        name=""
        placeholder="Steam Id"
        v-model="steamId"
        v-if="registerShown === true"
      />
      <input
        id="displayName"
        type="text"
        name=""
        placeholder="Display Name"
        v-model="displayName"
        v-if="registerShown === true"
      />
      <input
        id="password"
        type="password"
        name=""
        placeholder="Password"
        v-model="password"
      />
      <p id="infoText" v-show="infoToggle">{{ this.infoText }}</p>
      <button
        type="submit"
        id="loginBtn"
        v-on:click="loginUser()"
        v-if="registerShown === false"
      >
        Login
      </button>
      <button
        type="submit"
        id="loginBtn"
        v-on:click="registerUser()"
        v-if="registerShown === true"
      >
        Register
      </button>
      <button type="button" id="loginRegisterSwapBtn" v-on:click="swapFrame()">
        {{ this.loginRegisterSwapBtnText }}
      </button>
    </form>
  </div>
</template>

<script>
export default {
  name: 'login',
  data() {
    return {
      registerShown: false, //  if registration elements are shown
      infoToggle: false, //  if the info element is shown
      infoText: '', //  text of the info element
      loginRegisterSwapBtnText: 'Register', //  text of respetive button
      //  entered user infomation
      email: '',
      password: '',
      displayName: '',
      steamId: ''
    }
  },
  methods: {
    swapFrame: function() {
      //  method to change to and from registration and login frames
      if (this.registerShown === false) {
        this.registerShown = true
        this.loginRegisterSwapBtnText = 'Existing User'
      } else {
        this.registerShown = false
        this.loginRegisterSwapBtnText = 'Register'
        document.getElementById('displayName').style.borderColor = '#3498db'
        document.getElementById('steamId').style.borderColor = '#3498db'
      }

      this.infoTextUpdate(null, null)

      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'

      this.email = ''
      this.password = ''
      this.displayName = ''
      this.steamId = ''
    },

    login: function(email, password) {
      // method to contact token endpoint and get a user token
      this.$http
        .get(this.serverAddress + 'token', {
          auth: {username: email, password: password}
        })
        .then(
          (response) => {
            this.token = response.data.token
            this.$router.push({name: 'raid-selector'})
          },
          (error) => {
            if (error.response.status === 403) {
              // user doesnt exist
              this.infoTextUpdate(true, 'Email/Password not recognised')
            } else {
              // other error
              this.infoTextUpdate(true, error.response.data)
            }
            this.updateButtonState(false)
          }
        )
    },

    loginUser: function() {
      // method to check login inputs and prepare for successful or failed get token request
      this.updateButtonState(true)
      this.infoTextUpdate(null, null)

      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'

      if (this.email === '') {
        // missing email
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('email').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (this.password === '') {
        // missing password
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('password').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (!this.infoToggle) {
        // passed client validation
        this.login(this.email, this.password)
      }
    },

    registerUser: function() {
      // method to check registration inputs and prepare for successful or failed post users request
      this.updateButtonState(true)
      this.infoTextUpdate(null, null)
      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'
      document.getElementById('displayName').style.borderColor = '#3498db'
      document.getElementById('steamId').style.borderColor = '#3498db'

      if (this.email === '') {
        // missing email
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('email').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (this.password === '') {
        // missing password
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('password').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (this.displayName === '') {
        // missing displayName
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('displayName').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (this.steamId === '') {
        // missing steamId
        this.infoTextUpdate(true, 'All fields required')
        document.getElementById('steamId').style.borderColor = 'red'
        this.updateButtonState(false)
      }
      if (!this.infoToggle) {
        // passed client validation
        this.register(this.steamId, this.password, this.displayName, this.email)
      }
    },

    register: function(steamId, password, displayName, email) {
      // method to contact user endpoint to post a new user
      this.$http
        .post(this.serverAddress + 'users', {
          steamId: this.steamId,
          password: this.password,
          displayName: this.displayName,
          email: this.email
        })
        .then(
          () => {
            // success
            this.swapFrame()
            this.infoTextUpdate(false, 'Successfully registered! Please login')
            this.updateButtonState(false)
          },
          (error) => {
            // failed
            this.infoTextUpdate(true, error.response.data)
            this.updateButtonState(false)
          }
        )
    },

    infoTextUpdate: function(error, text) {
      // method to handle info text updates
      if (error === null) {
        //  reset and remove infoText
        this.infoToggle = false
      } else if (error) {
        //  serve info text as an error
        document.getElementById('infoText').style.color = 'red'
        this.infoText = text
        this.infoToggle = true
      } else if (!error) {
        //  serve info text as info
        this.infoText = text
        this.infoToggle = true
        document.getElementById('infoText').style.color = 'lime'
      }
    },

    updateButtonState: function(disableState) {
      // method to handle all button state changes
      let buttons = document.getElementsByTagName('button')
      for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = disableState
      }
    }
  }
}
</script>

<style scoped>
body {
  margin: 0;
  padding: 0;
  font-family: sans-serif;
  background: #34495e;
}
.login {
  width: 300px;
  padding: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #191919;
  text-align: center;
}
.login h1 {
  color: white;
  text-transform: uppercase;
  font-weight: 500;
  font-family: neue-haas-grotesk-display, sans-serif;
}
.login p {
  color: red;
  font-family: neue-haas-grotesk-display, sans-serif;
}
.login input[type='text'],
.login input[type='password'] {
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #3498db;
  padding: 14px 10px;
  width: 200px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  font-family: neue-haas-grotesk-display, sans-serif;
}
.login input[type='text']:focus,
.login input[type='password']:focus {
  width: 280px;
  border-color: #2ecc71;
  font-family: neue-haas-grotesk-display, sans-serif;
}
#loginRegisterSwapBtn {
  border: 2px solid #fd7c03;
}
#loginRegisterSwapBtn:hover,
#loginRegisterSwapBtn:focus {
  background: #fd7c03;
}
#loginRegisterSwapBtn:disabled {
  background: gray;
  border: 2px solid gray;
}
.login button {
  background: none;
  display: block;
  margin: 20px auto;
  text-align: center;
  border: 2px solid #2ecc71;
  padding: 14px 40px;
  outline: none;
  color: white;
  border-radius: 24px;
  transition: 0.25s;
  cursor: pointer;
  font-family: neue-haas-grotesk-display, sans-serif;
}
.login button:hover,
button:focus {
  background: #2ecc71;
}
.login button:disabled {
  background: gray;
  border: 2px solid gray;
}
</style>
