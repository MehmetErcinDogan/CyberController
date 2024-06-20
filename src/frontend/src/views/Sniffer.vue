<template>
    <div class="container">
      <div class="table-container">
        <!-- Bu kısımda bir sniffer tablomuz var. -->
        <table class="data-table">
          <thead>
            <tr>
              <th>Name</th>
              <th>TCP-IP</th>
              <th>IP</th>
              <th>DECAP</th>
            </tr>
          </thead>
          <tbody>
            <!-- Tablodaki bu değerleri script kısmındaki items adında bir arrayden alıyorum. Bu json formatında alınacak. -->
            <tr v-for="(item, index) in items" :key="index" @click="selectItem(item)">
              <td>{{ item.name }}</td>
              <td>{{ item.tcpip }}</td>
              <td>{{ item.ip }}</td>
              <td>{{ item.decap }}</td>
            </tr>
          </tbody>
        </table>
        <!-- Bu buttona ait startAction fonksiyonunun içeriğinin yazılması lazım. Sanırım bu fonksiyon json formatında değerleri getirecek. -->
        <button @click="startAction">Start</button>
      </div>
      
      <div v-if="selectedItem" class="popup">
        <!-- Seçilen tablonun satırına göre o elemana ait verilerin gösterildiği pop-up menü  -->
        <div class="popup-content">
          <h2>Item Details</h2>
          <p><strong>Name:</strong> {{ selectedItem.name }}</p>
          <p><strong>TCP-IP:</strong> {{ selectedItem.tcpip }}</p>
          <p><strong>IP:</strong> {{ selectedItem.ip }}</p>
          <p><strong>DECAP:</strong> {{ selectedItem.decap }}</p>
          <button @click="closePopup">Close</button>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const items = ref([
    { name: 'Item 1', tcpip: '192.168.1.1', ip: '10.0.0.1', decap: 'Decap 1' },
    { name: 'Item 2', tcpip: '192.168.1.2', ip: '10.0.0.2', decap: 'Decap 2' },
    { name: 'Item 3', tcpip: '192.168.1.3', ip: '10.0.0.3', decap: 'Decap 3' },
    { name: 'Item 4', tcpip: '192.168.1.4', ip: '10.0.0.4', decap: 'Decap 4' },
  ]);
  
  const selectedItem = ref(null);
  
  function selectItem(item) {
    selectedItem.value = item;
  }
  
  function closePopup() {
    selectedItem.value = null;
  }
  //Bu aşağıdaki fonksiyonun içeriği yazılmalı.
  function startAction() {
    alert('Start button clicked!');
  }
  </script>
  
  <style scoped>
  .container {
    position: relative;
    width: 100vw; /* Ekran genişliği kadar */
    height: 100vh; /* Ekran yüksekliği kadar */
    overflow: scroll;

  }
  
  .table-container {
    width: 50%;
    height: 50%;
    margin-top: 10%;
  }
  
  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 20px;
    font-weight: bold;
    color: white;
    margin-left: 10%;
  }
  
  .data-table th, .data-table td {
    border: 1px solid #d2cece;
    padding: 8px;
  }
  
  .data-table th {
    background-color: #2b2727;
    text-align: left;
  }
  
  .data-table tr:hover {
    background-color: #80907c;
    cursor: pointer;
  }
  
  button {
    margin-top: 30px;
    padding: 10px 20px;
    
    margin-left: 9%;
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
  
  .popup {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .popup-content {
    background-color: #fff;
    padding: 30px;
    border-radius: 10px;
    width: 400px;
    text-align: center;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    animation: fadeIn 0.3s ease-in-out;
  }
  
  .popup-content h2 {
    margin-bottom: 20px;
    color: #333;
  }
  
  .popup-content p {
    margin-bottom: 10px;
    color: #666;
  }
  
  .popup-content button {
    padding: 10px 20px;
    border: none;
    outline: none;
    background: #ff5945;
    color: #fff;
    font-size: 18px;
    cursor: pointer;
    border-radius: 5px;
    transition: background 0.3s ease;
    font-family: "Roboto Flex", sans-serif;

  }
  
  .popup-content button:hover {
    background: #e04e3d;
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
      transform: scale(0.9);
    }
    to {
      opacity: 1;
      transform: scale(1);
    }
  }
  </style>
  
  