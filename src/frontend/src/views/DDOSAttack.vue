<template>
    <div class="container">
      <div class="ddos-components">
        <div>
          <!-- Bu kısım da kullanıcıdan bir target-ip alınacak  -->
          <label for="target-ip">Target-IP:</label> 
          <input type="text" v-model="targetIp" id="target-ip">
        </div>
        <div>
          <!-- Bu kısımda ne zaman ddos atılacağı belirlenecek  -->
          <label for="timeout">Timeout:</label>
          <input type="time" v-model="timeout" id="timeout">
        </div>
      </div>
      <!-- Bu buttona basıldığında yazılan target-ip ve ne zaman atılacağı bilgilerinin alınıp ddos atma fonksiyonu çalışacak.  -->
      <button class="btnstart" @click="startDDOS">Start</button>
      <div class="progressbar-container">
        <div class="progressbar" :style="progressStyle">{{ progress }}%</div>
      </div>
      <!-- Bu log kısmı bizim görmek ddos atılırken görmek istediğimiz kısımları göstericek. -->
      <div class="log-container">
        <div class="log">
          <div v-for="(log, index) in logs" :key="index">{{ log }}</div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, computed } from 'vue';
  
  const targetIp = ref('');
  const timeout = ref('');
  const progress = ref(0);
  const logs = ref([]);
  
  const progressStyle = computed(() => ({
    width: `${progress.value}%`,
    backgroundColor: progress.value === 100 ? 'green' : 'red'
  }));
  
  const startDDOS = () => {
    logs.value.push(`Started DDOS attack on ${targetIp.value}`);
    progress.value = 0;
    const interval = setInterval(() => {
      if (progress.value < 100) {
        progress.value++;
        logs.value.push(`DDOS attack in progress on ${targetIp.value}... (${progress.value}%)`);
      } else {
        clearInterval(interval);
        logs.value.push(`DDOS attack on ${targetIp.value} completed.`);
      }
    }, 200); // 20 saniye için her %1 artış 200 ms sürer.
  };
  </script>
  
  <style scoped>
  .container {
    position: relative;
    width: 100vw; /* Ekran genişliği kadar */
    height: 100vh; /* Ekran yüksekliği kadar */
    overflow: scroll;
  }
  
  .ddos-components {
    display: flex;
    gap: 20%;
    margin-top: 100px;
    color: white;
    font-size: 24px;
    font-weight: bold;
    font-family: "Roboto Flex", sans-serif;

  }
  
  .ddos-components div {
    margin-bottom: 10px;
  }
  
  .btnstart {
    margin-top: 20px;
    margin-left: 10%;
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 24px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 50px;
    font-family: "Roboto Flex", sans-serif;
    font-weight: bold;


  }
  
  .progressbar-container {
    width: 100%;
    max-width: 100%;
    background-color: #ccc;
    border: 1px solid #000;
    height: 50px;
    margin-top: 10px;
    position: relative;
    font-weight: bold;
    font-family: "Roboto Flex", sans-serif;

  }
  
  .progressbar {
    height: 100%;
    color: #fff;
    text-align: center;
    line-height: 50px;
    transition: width 0.2s ease-in-out, background-color 0.2s ease-in-out;
  }
  
  .log-container {
    
    width: 100%;
    height: 500px;
    background-color: rgba(204, 31, 161, 0.245);

    overflow-y: auto;
    padding: 10px;
  }
  
  .log {
    font-weight: bold;
    color: white;
    font-size: 20px;
    font-family: "Roboto Flex", sans-serif;

  }
  </style>
  
  