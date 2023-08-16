<template>
  <iframe
    src="https://daocloud.io"
    title="demo"
    class="iframe-container"
  />
</template>

<style lang="scss">
html,
body {
  height: 100%;
}

#app {
  display: flex;
  height: 100%;
  .iframe-container {
    border: 0;
    flex: 1 1 0;
  }
}
</style>
