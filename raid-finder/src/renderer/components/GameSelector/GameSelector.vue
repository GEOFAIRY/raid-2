<template>
  <div id="body">
    <h4>Games for {{ this.raid.name }}</h4>
    <table>
      <tr>
        <th>Players</th>
        <th>Leader</th>
        <th>Raid</th>
        <th>Phase</th>
        <th>Status</th>
        <th>Sherpa</th>
      </tr>
      <tr v-for="game in games" v-bind:key="game.id">
        <th> {{ game. }}</th>
      </tr>
    </table>
  </div>
</template>

<script>
export default {
  name: 'game-selector',
  data() {
    return {
      raidId: this.$route.params.raidId,
      raid: {},
      games: {}
    }
  },
  mounted: function() {
    this.getRaid()
    this.getGames()
  },
  methods: {
    getRaid: function() {
      this.$http
        .get(this.serverAddress + 'raids/' + this.raidId)
        .then((response) => {
          this.raid = response.data
        })
    },
    getGames: function() {
      this.$http
        .get(this.serverAddress + 'game?raidId=' + this.raidId, {
          auth: {username: this.$store.state.Token.token, password: null}
        })
        .then((response) => {
          this.games = response.data
          console.log(this.games)
        })
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
</style>
