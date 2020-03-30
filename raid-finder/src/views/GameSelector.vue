<template>
  <div id="body">
    <div id="headerBar">
      <div class="divButton" @click="navigateRaidSelector()">
        <b>Raids</b>
      </div>
      <h4>Games for {{ this.raid.name }}</h4>
      <div class="divButton">
        <b>Create</b>
      </div>
    </div>
    <table>
      <tr>
        <th>Players</th>
        <th>Leader</th>
        <th>Phase</th>
        <th>Status</th>
        <th>Sherpa</th>
      </tr>
      <tr v-for="game in games" v-bind:key="game.id">
        <td>{{ game.users.length }}</td>
        <td>
          {{ game.users.find((user) => user.leader == true).displayName }}
        </td>
        <td>{{ game.phase }}</td>
        <td>{{ game.status }}</td>
        <td>{{ game.sherpa }}</td>
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
    },
    navigateRaidSelector: function() {
      this.$router.push({name: 'raid-selector'})
    }
  }
}
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  color: white;
  text-transform: uppercase;
  font-weight: 500;
  font-family: neue-haas-grotesk-display, sans-serif;
}
#headerBar {
  display: inline-grid;
  grid-template-columns: auto auto auto;
  padding-bottom: 10px;
  width: 900px;
}
.divButton {
  border: 1px solid #ddd;
  border-radius: 4px;
  margin-left: 20%;
  margin-right: 20%;
}
table {
  border-collapse: collapse;
  width: 100%;
}
td,
th {
  border: 1px solid #dddddd;
  text-align: left;
  padding: 8px;
}
tr:nth-child(even) {
  background-color: #dddddd;
}
</style>