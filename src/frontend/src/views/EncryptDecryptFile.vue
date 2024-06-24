<template>
    <div class="container">
      <div class="controls">
        <div class="file-select">
          <!-- Bu select file kısmı daha önce storage kısmına kaydettiğimiz dosyaları seçebilmek için kullanıyoruz. Şuan yanlış yapıyor.  -->
           <!-- Şuan dosyaları bilgisayardan seçiyor bizim back-end de bir storage oluşturup,profil kısmında bu storage kısmına dosya yükleyip, -->
            <!-- Bu encyrpt kısmında o storage kısmından seçmemiz lazım. -->
          <label for="file">Select File:</label>
          <input class="file1" type="file" id="file" @change="handleFileSelect">
        </div>
        <div class="dropdown">
          <label for="method">Encrypt Method:</label>
          <select class="method1" id="method" v-model="selectedMethod">
            <option class="method1" value="AES">AES</option>
            <option class="method1" value="RSA">RSA</option>
            <option class="method1" value="DES">DES</option>
          </select>
        </div>
        <div class="radio-buttons">
          <input type="radio" id="encrypt" value="encrypt" v-model="action">
          <label for="encrypt">Encrypt</label>
          <input type="radio" id="decrypt" value="decrypt" v-model="action">
          <label for="decrypt">Decrypt</label>
        </div>
      </div>
      <div class="actions">
        <!-- Burdaki buttonlarda seçilen methoda, dosyaya veya encrypt veya decrypt olaylarına göre işlemler yapılacak. Bu fonksiyonlar yazılmalı. -->
        <button class="btnstart" @click="startProcess">Start</button>
        <button class="btnselect" @click="selectOutputPath">Output Path</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const selectedMethod = ref('AES');
  const action = ref('encrypt');
  
  const handleFileSelect = (event) => {
    const file = event.target.files[0];
    console.log('File selected:', file);
  };
  
  const startProcess = () => {
    console.log('Starting process with method:', selectedMethod.value, 'and action:', action.value);
  };
  
  const selectOutputPath = () => {
    console.log('Output path selected');
  };
  </script>
  
  <style scoped>
  .container {
    position: relative;
    width: 100vw; /* Ekran genişliği kadar */
    height: 100vh; /* Ekran yüksekliği kadar */
    overflow: scroll;

  }
  .container::-webkit-scrollbar{
    display: none;
  }
  
  .controls {
    display: flex;
    align-items: center;
    margin-top: 100px;
    gap: 20px;
    margin-left: 10%;
  }
  
  .file-select {
    display: flex;
    flex-direction: column;
    font-size: 24px;
    color: white;
    font-weight: bold;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;

  }
  .file1{
    font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

  }
  .method1{
    font-family: "Roboto Flex", sans-serif;
  font-weight: bold;
  font-size: 14px;
  color: #b4049c;
  font-style: italic;

  }
  
  .dropdown {
    display: flex;
    flex-direction: column;
    font-size: 24px;
    color: white;
    font-weight: bold;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;

  }
  
  .radio-buttons {
    display: flex;
    align-items: center;
    gap: 10px;
    font-size: 24px;
    color: white;
    font-weight: bold;
    font-family: "Roboto Flex", sans-serif;
    font-style: italic;

  }
  
  .actions {
    margin-top: 10%;
    display: flex;
    gap: 20px;
  }
  .btnstart{
    margin-top: 20px;
    
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
    margin-left: 10%;
    font-family: "Roboto Flex", sans-serif;
    font-weight: bold;
    font-style: italic;



  }
  .btnselect{
    margin-top: 20px;
    
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
    margin-left: 5%;
    font-family: "Roboto Flex", sans-serif;
    font-weight: bold;
    font-style: italic;



  }
  </style>
  