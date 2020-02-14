<template>
  <div id="cards">
    <div
      class="card"
      v-for="raid in raids"
      v-bind:key="raid.id"
      @click="gameSelector(raid.id)"
    >
      <img class="card-image" :src="raid.image" alt="Cannot find image" />
      <div class="container">
        <h4>
          <b class="text">{{ raid.name }}</b>
        </h4>
      </div>
    </div>
    <div id="logoutCard" v-on:click="logout()">
      <img
        class="logout-image"
        src="~@/assets/logout.png"
        alt="Cannot find image"
      />
      <h4>Logout</h4>
    </div>
  </div>
</template>

<script>
export default {
  name: 'raid-selector',
  data() {
    return {
      raids: {}
    }
  },
  mounted: function() {
    this.getRaids()
  },
  methods: {
    getRaids: function() {
      // gets the raids
      this.$http.get(this.serverAddress + 'raids').then((response) => {
        this.raids = response.data
      })
    },
    logout: function() {
      // logout current user
      this.$store.dispatch('LOGOUT')
      this.$router.push({name: 'login'})
    },
    gameSelector: function(raidId) {
      // move to game seletor with a raid id
      this.$router.push({name: 'game-selector', params: {raidId: raidId}})
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

.text {
  color: white;
  text-transform: uppercase;
  font-weight: 500;
  font-family: neue-haas-grotesk-display, sans-serif;
}

#cards {
  display: inline-grid;
  grid-template-columns: auto auto auto;
  background: #191919;
}

#logoutCard {
  transition: 0.3s;
  padding: 10px;
  margin: 5px;
  background: black;
  width: 200px;
  height: 150px;
  text-align: center;
  margin-top: 13%;
  margin-left: 27%;
}

.card {
  transition: 0.3s;
  padding: 10px;
  width: 412px;
  margin: 5px;
  background: black;
  text-align: center;
}

/* On mouse-over, add a deeper shadow */
.card:hover,
#logoutCard:hover {
  box-shadow: 0 8px 16px 0 rgba(255, 255, 255, 0.2);
}

/* Add some padding inside the card container */
.container {
  padding: 2px 16px;
}

.card-image {
  width: 100%;
  height: 100%;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.logout-image {
  width: 75px;
  height: 75px;
  margin-top: 10%;
}
</style>
