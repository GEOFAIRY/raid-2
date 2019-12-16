<template>
  <div class="title-bar">
    <div class="window-controls-container">
      <div id="minimize-button" class="minimize-button" v-on:click="minimize">
        <svg name="minimize-svg" width="12" height="12" viewbox="0 0 12 12">
          <rect fill="white" width="10" height="1" x="1" y="6"></rect>
        </svg>
      </div>
      <div id="min-max-button" class="min-max-button" v-on:click="minMax">
        <svg name="min-max-svg" width="12" height="12" viewbox="0 0 12 12">
          <rect
            width="9"
            height="9"
            x="1.5"
            y="1.5"
            fill="none"
            stroke="white"
          ></rect>
        </svg>
      </div>
      <div id="close-button" class="close-button" v-on:click="close">
        <svg name="close-svg" width="12" height="12" viewbox="0 0 12 12">
          <polygon
            fill="white"
            points="11 1.576 6.583 6 11 10.424 10.424 11 6 6.583 1.576 11 1 10.424 5.417 6 1 1.576 1.576 1 6 5.417 10.424 1"
          ></polygon>
        </svg>
      </div>
    </div>
  </div>
</template>

<script>
const { remote } = require('electron')

export default {
  methods: {
    close: function (event) {
      remote.app.quit()
    },
    minMax: function (event) {
      const currentWindow = remote.getCurrentWindow()
      if (currentWindow.isMaximized()) {
        currentWindow.unmaximize()
      } else {
        currentWindow.maximize()
      }
    },
    minimize: function (event) {
      remote.getCurrentWindow().minimize()
    }
  }
}
</script>

<style scoped>
    .title-bar {
    -webkit-app-region: drag;
    margin: 0;
    display: flex;
    background-color: #474747;
    width: 100%;
    height: 25px;
    }

    .window-controls-container {
    display: flex;
    justify-content: flex-end;
    align-items: center;
    flex-grow: 1;
    }

    .minimize-button {
    -webkit-app-region: no-drag;
    border: none;
    width: 30px;
    height: 25px;
    text-align: center;
    }

    .minimize-button:hover {
    background-color: grey;
    }

    .min-max-button {
    -webkit-app-region: no-drag;
    border: none;
    width: 30px;
    height: 25px;
    text-align: center;
    }

    .min-max-button:hover {
    background-color: grey;
    }

    .close-button {
    -webkit-app-region: no-drag;
    border: none;
    width: 30px;
    height: 25px;
    text-align: center;
    }

    .close-button:hover {
    background-color: grey;
    }
</style>
