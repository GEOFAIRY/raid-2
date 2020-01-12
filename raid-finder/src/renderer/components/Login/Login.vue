<template>
  <div id="login">
    <form class="login" v-if="currentFrame === 'Login'">
      <h1>Welcome</h1>
      <input
        id="email"
        type="text"
        name=""
        placeholder="Email"
        v-model="email"
      />
      <input
        id="password"
        type="password"
        name=""
        placeholder="Password"
        v-model="password"
      />
      <p id="infoText" v-show="infoToggle">{{ this.infoText }}</p>
      <button type="submit" id="loginBtn" v-on:click="loginUser()">
        Login
      </button>
      <button type="button" id="registerBtn" v-on:click="swapFrame()">
        Register
      </button>
    </form>
    <form class="login" v-if="currentFrame === 'Register'">
      <h1>Register</h1>
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
      />
      <input
        id="displayName"
        type="text"
        name=""
        placeholder="Display Name"
        v-model="displayName"
      />
      <input
        id="password"
        type="password"
        name=""
        placeholder="Password"
        v-model="password"
      />
      <p id="infoText" v-show="infoToggle">{{ this.infoText }}</p>
      <button type="submit" id="loginBtn" v-on:click="registerUser()">
        Register
      </button>
      <button type="button" id="registerBtn" v-on:click="swapFrame()">
        Existing User
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
      } else {
        this.currentFrame = 'Login'
        document.getElementById('displayName').style.borderColor = '#3498db'
        document.getElementById('steamId').style.borderColor = '#3498db'
      }
      this.infoToggle = false
      document.getElementById('email').style.borderColor = '#3498db'
      document.getElementById('password').style.borderColor = '#3498db'

      this.email = ''
      this.password = ''
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
#registerBtn {
  border: 2px solid #fd7c03;
}
#registerBtn:hover {
  background: #fd7c03;
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
#registerBtn:disabled {
  background: gray;
  border: 2px solid gray;
}
</style>
