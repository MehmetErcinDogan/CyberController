<template>
  <div class="full-screen-container">
    <div class="up-container">
      <div class="listing-devices">
        <h1 class="l1">Listing Devices</h1>
        <h1 class="l2" v-for="device in devices" :key="device">{{ device }}</h1>
      </div>
      <!-- Bu aşağıdaki Scan buttonu yukarıdaki Listing devices kısmında cihazları listeleyecek. -->
      <button class="btn-scan" @click="scanDevices">Scan</button>
    </div>
    <div class="down-container">
      <!-- Portlar için burada bir tablo oluşturdum. Aşağıda portun içeriği için bir array kullandım. -->
      <table class="ports-table">
        <thead>
          <tr>
            <th>Port Number</th>
            <th>Click Status</th>
            <th>Able</th>
          </tr>
        </thead>
        <tbody>
          <!-- Bu bilgiler script kısmında arrayden geliyor.  -->
           <!-- Aşağıdaki showDetails fonksiyonu portun içindeki bir elemana tıklandığında portun bilgilerinin gösterildiği bir modal açılıyor. -->
           <tr v-if="showPorts" v-for="port in ports" :key="port.portNumber" @click="showDetails(port)">
            <td>{{ port.portNumber }}</td>
            <td>{{ port.clickStatus }}</td>
            <td>{{ port.able }}</td>
          </tr>
        </tbody>
      </table>
      <!-- Bu search fonksiyonu yapılması lazım click olduğunda sanırım bu buttona basıldığında port tablosunun içeriğini dolduracak.  -->
      <button class="btn-search" @click="searchPorts">Search</button>
    </div>
    <div v-if="selectedPort" class="modal">
      <div class="modal-content">
        <!-- Bu kısım seçilen porta göre modalın içeriği gösteriliyor. -->
        <span class="close" @click="closeModal">&times;</span>
        <h2 class="ptdetails">Port Details</h2>
        <!-- İstediğin daha fazla özellik varsa bunları arraye yazıp çekebilirsin. -->
        <p>Packet ID: {{ selectedPort.packetId }}</p>
        <p>Packet Name: {{ selectedPort.packetName }}</p>
        <p>Port Number: {{ selectedPort.portNumber }}</p>
        <p>Click Status: {{ selectedPort.clickStatus }}</p>
        <p>Able: {{ selectedPort.able }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Bu arrayi json formatında çekilmesi gerekiyor.
const ports = ref([
  { portNumber: '123456', clickStatus: 'clickable', able: 1 , packetId: '9974', packetName: 'Elma' },
  { portNumber: '234567', clickStatus: 'unclickable', able: 0, packetId: '9975', packetName: 'Armut'  },
  { portNumber: '345678', clickStatus: 'clickable', able: 1, packetId: '9976', packetName: 'Çilek'  },
]);

const devices = ref([]);

const selectedPort = ref(null);
const showPorts = ref(false);


const showDetails = (port) => {
  selectedPort.value = port;
};

const closeModal = () => {
  selectedPort.value = null;
};
const searchPorts = () => {
  showPorts.value = true;
};

const scanDevices = () => {
  // Örnek cihaz isimleri
  devices.value = ['Device1', 'Device2', 'Device3'];
};
</script>



<style scoped>
.full-screen-container {
  width: 100vw;
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  overflow-x: hidden;
  box-sizing: border-box;

}
.full-screen-container::-webkit-scrollbar {
  width: 10px;
}

.full-screen-container::-webkit-scrollbar-thumb {
  background-color: #b0b0b0; /* Gümüş grisi renk */
  border-radius: 5px;
}

.full-screen-container::-webkit-scrollbar-thumb:hover {
  background-color: #a0a0a0; /* Hover sırasında biraz daha koyu gri */
}

.full-screen-container::-webkit-scrollbar-track {
  background-color: #f0f0f0; /* Açık gri arka plan */
}

.up-container {
  height: 45%;
  width: 100%;
  margin-top: 10%;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  margin-bottom: 20px; /* Aradaki mesafeyi azaltmak için */
  
  
  padding: 0 5%;

}

.down-container {
  height: 45%;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 10%;
  position: relative; /* Search button'u hizalamak için relative konumlandırma */
  border-radius: 10px;
  
  
  
}

.listing-devices {
  width: 33%;
  height: 100%;
  border-radius: 5px;
  background-color: rgba(204, 31, 161, 0.245);
  
  align-items: center;
  justify-content: center;
  padding: 20px;
  box-sizing: border-box;
  border-radius: 10px;

}

.ports-table {
  width: 30%;
  height: 100%;
  border-collapse: collapse;
  background-color: rgba(204, 31, 161, 0.245);
  border-radius: 15px;
  
  margin-right: 60%;
}

.ports-table th,
.ports-table td {
  border: 1px solid #ddd;
  padding: 18px;
  text-align: center;
  color: white;
  font-family: "Roboto Flex", sans-serif;
  
}

.ports-table th {
  background-color: #075df1;
  color: white;
}

.ports-table tbody tr {
  cursor: pointer;
}

.ports-table tbody tr:hover {
  background-color: rgba(255, 255, 255, 0.1);
}

h1 {
  font-size: 18px;
  color: white;
  font-family: "Roboto Flex", sans-serif;
}

.l1 {
  font-size: 24px;
  margin-bottom: 5px; /* Listing Devices başlığına daha fazla boşluk eklemek için */
  color: white;
  font-family: "Roboto Flex", sans-serif;
  margin-left: 5%;
  color: #075df1;
}

.l2 {
  margin-bottom: 5px;
  margin-left: 5%;
}

.btn-scan {
  margin-top: 20px;
  margin-left: 20%;
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
}

.btn-search {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  
  margin-left: 12%;
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
}

.btn-scan:hover,
.btn-search:hover {
  background-color: #843a6990;
}

.modal {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.5);
}

.modal-content {
  background-color: #fefefe;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  width: 80%;
  max-width: 500px;
  border-radius: 10px;
  font-family: "Roboto Flex", sans-serif;
  color: #333;
}


.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
}
</style>
