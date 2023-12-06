<template>
    <div>
      <iframe title="demo-dev" src="https://dce5.visionet.cn:31450/kpanda/clusters" ref="iframe">
      </iframe>
    </div>
  </template>
  
  <script setup lang="ts">
  import {
    ref, onMounted,
  } from 'vue';
  
  const iframe = ref<HTMLIFrameElement>();
  
  onMounted(() => {
    iframe.value?.addEventListener('load', () => {
      const styleElement = document.createElement('style');
  
      const styles = [
        '.ghippo-header { display: none; }',
      ];
  
      styleElement.textContent = styles.join('');
      iframe.value?.contentWindow?.document.head.appendChild(styleElement);
    });
  });
  </script>
  
  <style lang="scss">
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }
  
  html,
  body {
    width: 100%;
    height: 100%;
    padding: 0;
    margin: 0;
  }
  
  div {
    width: 100%;
    height: 100%;
    margin: 0px;
    padding: 0px;
    border-width: 0px;
  }
  
  iframe {
    width: 100%;
    height: 100%;
    margin: 0px;
    padding: 0px;
    border-width: 0px;
  }
  </style>
  