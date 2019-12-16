<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script>
const customTitlebar = require('custom-electron-titlebar')
/* eslint-disable */
new customTitlebar.Titlebar({
  backgroundColor: customTitlebar.Color.fromHex('#474747'),
  menu: null
})
/* eslint-enable */

export default {
  name: 'raid-finder'
}
</script>

<style>
#app {
  color: white;
}

::-webkit-scrollbar {
  width: 12px;
}

/* Track */
::-webkit-scrollbar-track {
  -webkit-box-shadow: inset 0 0 6px rgba(255, 255, 255, 0.164);
  -webkit-border-radius: 10px;
  border-radius: 10px;
}

/* Handle */
::-webkit-scrollbar-thumb {
  -webkit-border-radius: 10px;
  border-radius: 10px;
  background: rgba(146, 146, 146, 0.8);
  -webkit-box-shadow: inset 0 0 6px rgba(80, 80, 80, 0.5);
}
::-webkit-scrollbar-thumb:window-inactive {
  background: rgba(146, 146, 146, 0.322);
}
</style>
