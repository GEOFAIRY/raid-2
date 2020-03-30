<template>
  <div id="cards">
    <div class="card" style="width: 18rem;" v-for="raid in raids"
      v-bind:key="raid.id"
      @click="gameSelector(raid.id)">
      <img class="card-img-top" :src="raid.image" alt="Card image cap" />
      <div class="card-body">
        <p class="card-text">
          {{ raid.name }}
        </p>
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


</style>
