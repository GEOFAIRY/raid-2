<template>
  <div id="cards">
    <div class="card" v-for="raid in raids" v-bind:key="raid.id">
      <img class="card-image" :src="raid.image" alt="Cannot find image" />
      <div class="container">
        <h4>
          <b class="text">{{ raid.name }}</b>
        </h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'raid-selector',
  data () {
    return {
      raids: {}
    }
  },
  mounted: function () {
    this.getRaids()
  },
  methods: {
    getRaids: function () {
      // gets the raids
      this.$http.get(this.serverAddress + 'raids').then((response) => {
        this.raids = response.data
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
  font-family: neue-haas-grotesk-display, sans-serif;
}

#cards {
  display: inline-grid;
  grid-template-columns: auto auto auto;
}

.card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(255, 255, 255, 0.2);
  transition: 0.3s;
  padding: 10px;
  width: 412px;
  margin: 5px;
}

/* On mouse-over, add a deeper shadow */
.card:hover {
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
</style>
