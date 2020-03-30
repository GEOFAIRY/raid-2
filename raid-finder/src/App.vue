<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'raid-finder'
}
</script>

<style>
#app {
  background: #34495e;
}
::-webkit-scrollbar {
  width: 12px;
  background: #191919;
}
/* Handle */
::-webkit-scrollbar-thumb {
  -webkit-border-radius: 10px;
  border-radius: 10px;
  background: rgba(146, 146, 146, 0.8);
  -webkit-box-shadow: inset 0 0 6px rgba(80, 80, 80, 0.5);
  box-shadow: inset 0 0 6px rgba(80, 80, 80, 0.5);
}
::-webkit-scrollbar-thumb:window-inactive {
  background: rgba(146, 146, 146, 0.322);
}
</style>
