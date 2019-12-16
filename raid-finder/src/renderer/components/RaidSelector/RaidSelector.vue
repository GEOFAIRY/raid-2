<template>
  <div id="cards">
    <div class="card" v-for="card in cards" v-bind:key="card.id">
      <img class="card-image" :src="card.image" alt="Cannot find image" />
      <div class="container">
        <h4>
          <b>{{ card.title }}</b>
        </h4>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'raid-selector',
  data: () => ({
    cards: [
      {
        title: 'Leviathan',
        id: 1,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raid_gluttony.jpg'
      },
      {
        title: 'Eater of worlds',
        id: 2,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raids_leviathan_eater_of_worlds.jpg'
      },
      {
        title: 'Spire of stars',
        id: 3,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raid_greed.jpg'
      },
      {
        title: 'The Last Wish',
        id: 4,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raid_beanstalk.jpg'
      },
      {
        title: 'Scourge of the Past',
        id: 5,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raids.1305rh0093145r13t5hn10tnz.raid_sunset.jpg'
      },
      {
        title: 'Crown of Sorrow',
        id: 6,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raid_eclipse.jpg'
      },
      {
        title: 'Garden of Salvation',
        id: 7,
        image:
          'https://stats.bungie.net/img/destiny_content/pgcr/raid_garden_of_salvation.jpg'
      }
    ]
  })
}
</script>

<style scoped>
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
