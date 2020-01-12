<template>
  <div id="login">
    <form class="login">
      <h1 v-if="currentFrame === 'Register'">Register</h1>
      <h1 v-if="currentFrame === 'Login'">Welcome</h1>
      <input id="email" type="text" name="" placeholder="Email" v-model="email"/>
      <input id="steamId" type="text" name="" placeholder="Steam Id" v-model="steamId" v-if="currentFrame === 'Register'"/>
      <input id="displayName" type="text" name="" placeholder="Display Name" v-model="displayName" v-if="currentFrame === 'Register'"/>
      <input id="password" type="password" name="" placeholder="Password" v-model="password"/>
      <p id="infoText" v-show="infoToggle">{{ this.infoText }}</p>
      <button type="submit" id="loginBtn" v-on:click="loginUser()" v-if="currentFrame === 'Login'">
        Login
      </button>
      <button type="submit" id="loginBtn" v-on:click="registerUser()" v-if="currentFrame === 'Register'">
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
  data () {
    return {
      currentFrame: 'Login',
      infoToggle: false,
      infoText: '',
      loginRegisterSwapBtnText: 'Register',
      email: '',
      password: '',
      displayName: '',
      steamId: ''
    }
  },
  mounted: function () {},
  methods: {
    swapFrame: function () {
      if (this.currentFrame === 'Login') {
        this.currentFrame = 'Register'
        this.loginRegisterSwapBtnText = 'Existing User'
      } else {
        this.currentFrame = 'Login'
        this.loginRegisterSwapBtnText = 'Register'
        document.getElementById('displayName').style.borderColor = '#3498db'
        document.getElementById('steamId').style.borderColor = '#3498db'
      }
      this.infoToggle = false
      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'

      this.email = ''
      this.password = ''
      this.displayName = ''
      this.steamId = ''
    },
    login: function (email, password) {
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
              this.infoText = 'Email/Password not recognised'
            } else {
              this.infoText = error.response.data
            }
            this.infoToggle = true
            document.getElementById('infoText').style.color = 'red'
            let buttons = document.getElementsByTagName('button')
            for (let i = 0; i < buttons.length; i++) {
              buttons[i].disabled = false
            }
          }
        )
    },
    loginUser: function () {
      let buttons = document.getElementsByTagName('button')
      for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true
      }

      this.infoToggle = false
      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'
      if (this.email === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('email').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (this.password === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('password').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (!this.infoToggle) {
        this.login(this.email, this.password)
      }
    },
    registerUser: function () {
      let buttons = document.getElementsByTagName('button')
      for (let i = 0; i < buttons.length; i++) {
        buttons[i].disabled = true
      }

      this.infoToggle = false
      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'
      document.getElementById('displayName').style.borderColor = '#3498db'
      document.getElementById('steamId').style.borderColor = '#3498db'

      if (this.email === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('email').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (this.password === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('password').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (this.displayName === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('displayName').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (this.steamId === '') {
        this.infoToggle = true
        this.infoText = 'All fields required'
        document.getElementById('steamId').style.borderColor = 'red'
        document.getElementById('infoText').style.color = 'red'
        for (let i = 0; i < buttons.length; i++) {
          buttons[i].disabled = false
        }
      }
      if (!this.infoToggle) {
        this.$http
          .post(this.serverAddress + 'users', {
            steamId: this.steamId,
            password: this.password,
            displayName: this.displayName,
            email: this.email
          })
          .then(
            () => {
              this.swapFrame()
              this.infoText = 'Successfully registered! Please login'
              this.infoToggle = true
              document.getElementById('infoText').style.color = 'lime'
              for (let i = 0; i < buttons.length; i++) {
                buttons[i].disabled = false
              }
            },
            (error) => {
              this.infoText = error.response.data
              this.infoToggle = true
              document.getElementById('infoText').style.color = 'red'
              for (let i = 0; i < buttons.length; i++) {
                buttons[i].disabled = false
              }
            }
          )
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
#loginRegisterSwapBtn:hover {
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
.login button:hover {
  background: #2ecc71;
}
.login button:disabled {
  background: gray;
  border: 2px solid gray;
}
</style>
