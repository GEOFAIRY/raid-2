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
      }

      this.infoTextUpdate(null, null)


      this.email = ''
      this.password = ''
      this.displayName = ''
      this.steamId = ''
    },

    login(email, password) {
      // method to contact token endpoint and get a user token
      this.$http
        .get(this.serverAddress + 'token', {
          auth: {username: email, password: password}
        })
        .then(
          response => {
            // this.setToken(response.data.token)
            this.$store.dispatch('LOGIN', response.data.token)
            this.$router.push({name: 'raid-selector'})
          },
          error => {
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


      if (this.email === '') {
        // missing email
        this.infoTextUpdate(true, 'All fields required')
        this.updateButtonState(false)
      }
      if (this.password === '') {
        // missing password
        this.infoTextUpdate(true, 'All fields required')
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

      if (this.email === '') {
        // missing email
        this.infoTextUpdate(true, 'All fields required')
        this.updateButtonState(false)
      }
      if (this.password === '') {
        // missing password
        this.infoTextUpdate(true, 'All fields required')
        this.updateButtonState(false)
      }
      if (this.displayName === '') {
        // missing displayName
        this.infoTextUpdate(true, 'All fields required')
        this.updateButtonState(false)
      }
      if (this.steamId === '') {
        // missing steamId
        this.infoTextUpdate(true, 'All fields required')
        this.updateButtonState(false)
      }
      if (!this.infoToggle) {
        // passed client validation
        this.register(this.steamId, this.password, this.displayName, this.email)
      }
    },

    register: function() {
      // method to contact user endpoint to post a new user
      this.$http
        .post(this.serverAddress + 'users', {
          steamId: this.steamId,
          password: this.password,
          displayName: this.displayName,
          email: this.email
        })
        .then(
          function() {
            // success
            this.swapFrame()
            this.infoTextUpdate(false, 'Successfully registered! Please login')
            this.updateButtonState(false)
          },
          function(error) {
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
        this.infoText = text
        this.infoToggle = true
      } else if (!error) {
        //  serve info text as info
        this.infoText = text
        this.infoToggle = true
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
#login {
  width: 100vw;
  height: 100vh;
  background: #191919;
}

.login {
  width: 300px;
  padding: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: #000000;
  text-align: center;
}
</style>