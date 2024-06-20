<template>
 <div class="container">
    <div class="up-profile">
      <div class="profile-photo">
        <img src="/profile.png" alt="Profile Photo">
      </div>
      <div class="other-profile-info">
        <h1 class="name">Adı:</h1>
        <h1 class="name">CANBERK</h1>
        <h1 class="surname">Soyadı:</h1>
        <h1 class="surname">ARMAN</h1>
        <h1 class="account-id">ID:</h1>
        <h1 class="account-id">11111</h1>
        <h1 class="position">Position:</h1>
        <h1 class="position">Student</h1>
        <div class="label-acc">
          <div class="label-acc11">
            <h1 class="logout-time">Time ETC</h1>
            <h1 class="tcp-ipp">TCP IP</h1>

          </div>
          <!-- Bu buttona basıldığında logout olup tekrardan giriş ekranına gitmesi gerekiyor. Bunun için fonksiyonu yazılmalı. -->
          <button class="logout">Logout</button>
        </div>
      </div>
    </div>
    <div class="History">
      <h1 class="h1">History</h1>
      <!-- Kullanıcının history kısmı  -->
      <div class="port-scanner-info">
        <div class="up-port">
          <div class="label1">
            <div class="table-texts">
              <h1 class="ProblemT">Problems</h1>
              <h1 class="ProblemT1">Names</h1>
            </div>
            <!-- Burdaki problemler kısmının içeriğini script kısmındaki problems arrayinden alıyor bunu jsondan almalı. -->
            <div v-for="(item, index) in problems" :key="index" class="Problem" @click="selectProblem(index)">
              <h1 :class="{'selected': selectedIndex === index}" class="Problems">{{ item.problem }}</h1>
              <h1 :class="{'selected': selectedIndex === index}" class="Names">{{ item.name }}</h1>
            </div>
          </div>
          <div class="buttons">
            <!-- Kullanıcının problemleri silmesi ve temizlemesi için koyduğum buttonlar. -->
            
            <button class="clear" @click="clearItems">Clear</button>
            <button class="delete" @click="deleteItem">Delete</button>
          </div>
        </div>
        <div class="Storage">
          <h1 class="Storage1">Storage</h1>
        </div>
        <div class="menu">
          <!-- Burda bir button var upload files adında bizim back-end de oluşturduğumuz storage kısmına burdan dosya yüklüyoruz. -->
          <button class="btnpopup" @click="toggleUploadPopup">Upload Files</button>
          <div class="modal" v-if="showUploadPopup">
            <div class="modal-content">
              <button class="close-btn" @click="closeUploadPopup">Close</button>
              <input type="file" @change="handleFileUpload" multiple>
              <ul>
                <li v-for="file in fileList" :key="file.name">
                  <span>{{ file.name }} - {{ formatSize(file.size) }}</span>
                  <button @click="downloadFile(file)">Download</button>
                  <span v-if="isImage(file)">
                    <img :src="file.url" :alt="file.name" style="max-width: 100px;">
                  </span>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="Order">
      <h1 class="o1">Order</h1>
      <h2>Menü</h2>
      <div class="menu-components">
        <!-- Burası order menüsü kısmı burda kullanıcı tarih,saat ve işlem seçicek. -->
        <div>
          <label for="tarih">Tarih:</label>
          <input type="date" v-model="tarih" id="tarih">
        </div>
        <div>
          <label for="saat">Saat:</label>
          <input type="time" v-model="saat" id="saat">
        </div>
        <div>
          <label for="islem">İşlem:</label>
          <select v-model="islem" id="islem">
            <option value="" disabled>İşlem seçin</option>
            <option value="DDOS ATTACK">DDOS ATTACK</option>
            <option value="SESSION ATTACK">SESSION ATTACK</option>
          </select>
        </div>
        <div>
          <label for="isim">İsim:</label>
          <input type="text" v-model="isim" id="isim">
        </div>
        <!-- Bu kaydet buttonu ile işlem kaydedilecek. -->
        <button @click="kaydet">Kaydet</button>
      </div>
      <div class="down-order">
        <div class="label1">
          <h1>İşlem Listesi</h1>
          <ul>
            <!-- Kaydedilen kayıtlar bu kısımda gösterilecek. -->
            <li v-for="(record, index) in kayitlar" :key="index" @click="selectKayit(index)">
              <span :class="{'selected': selectedKayitIndex === index}">{{ record }}</span>
            </li>
          </ul>
        </div>
        <!-- Bu button sayesinde seçilen kayıtlar silinecek. -->
        <button class="btndelete1" @click="sil">Sil</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const showUploadPopup = ref(false);
const fileList = ref([]);

const tarih = ref('');
const saat = ref('');
const islem = ref('');
const isim = ref('');
const sonuc = ref('');

const kayitlar = ref([]);
const selectedKayitIndex = ref(null);

// Bu fonksiyon order kısmında yeni kayıtları kaydedicek.
const kaydet = () => {
  const yeniKayit = `Tarih: ${tarih.value}, Saat: ${saat.value}, İşlem: ${islem.value}, İsim: ${isim.value}`;
  kayitlar.value.push(yeniKayit);
  tarih.value = '';
  saat.value = '';
  islem.value = '';
  isim.value = '';
  selectedKayitIndex.value = null;  // Reset the selected index after saving a new record
};
//Bu fonksiyon ile kayıtlardan biri seçilebilecek.
const selectKayit = (index) => {
  selectedKayitIndex.value = index;
};
//Seçilen order silinecek.
const sil = () => {
  if (selectedKayitIndex.value !== null) {
    kayitlar.value.splice(selectedKayitIndex.value, 1);
    selectedKayitIndex.value = null;
  }
};
//Pop-up menüyü açıyor.
function toggleUploadPopup() {
  showUploadPopup.value = !showUploadPopup.value;
}

function handleFileUpload(event) {
  const files = event.target.files;
  for (let i = 0; i < files.length; i++) {
    const file = files[i];
    const fileObject = {
      name: file.name,
      size: file.size,
      type: file.type,
      url: URL.createObjectURL(file)
    };
    fileList.value.push(fileObject);
  }
}

function isImage(file) {
  return file.type.startsWith('image');
}

function downloadFile(file) {
  // Dosya indirme işlemi burada gerçekleştirilebilir
  console.log('Dosya indiriliyor:', file.name);
}

function formatSize(bytes) {
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB'];
  if (bytes === 0) return '0 Byte';
  const i = parseInt(Math.floor(Math.log(bytes) / Math.log(1024)));
  return Math.round(bytes / Math.pow(1024, i), 2) + ' ' + sizes[i];
}
//Dosya yüklemek için açılan pop-up menüyü kapatıyor.
function closeUploadPopup() {
  showUploadPopup.value = false;
}
//Problemlerin bulunduğu array
const problems = ref([
  { problem: 'Problem1', name: 'Name1' },
  { problem: 'Problem2', name: 'Name2' },
  { problem: 'Problem3', name: 'Name3' },
  { problem: 'Problem4', name: 'Name4' },
])
//Problemi seçmek için fonksiyon
const selectedIndex = ref(null)
const selectProblem = (index) => {
  selectedIndex.value = index
}


// Problemleri clear etmek için
const clearItems = () => {
  problems.value = []
  selectedIndex.value = null

}
//Problemleri silmek için
const deleteItem = () => {
  if (selectedIndex.value !== null) {
    problems.value.splice(selectedIndex.value, 1)
    selectedIndex.value = null
  } else {
    alert('Please select a problem to delete.')
  }
}


</script>

<style scoped>

.container{
    
    width: 100%;
    height: 100%;
    
    font-family: "Roboto Flex", sans-serif;

    
    
   
    
}
.container::-webkit-scrollbar{
  display: none;
}
.up-profile{
    display: flex;
    width: 100%;
    height: 30%;
    
 
 color: white;
 
    
}
.profile-photo{
    margin-top: 50px;
    scale: 0.4;
    
}
.other-profile-info{
    margin-top: 150px;
    display: flex;
    gap: 20px;
    font-size: 12px;
    font-family: "Roboto Flex", sans-serif;

    


}
.label-acc{
    
    margin-left: 50px;
    width: 300px;
    height: 100px;
    border-radius: 5px;
    background-color: rgba(204, 31, 161, 0.245);
    font-family: "Roboto Flex", sans-serif;


  margin-right: 20px;
  margin-bottom: 10px; /* Listing Devices başlığını bir miktar aşağı kaydır */
  display: flex;
}
.label-acc11{
  font-size: 10px;
}
.logout {
    margin-left: 40%;
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 14px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 30px;
    font-family: "Roboto Flex", sans-serif;

}

.logout:hover {
    background: #a59290; /* Hover sırasında arka plan rengini değiştirin */
}
.btnpopup{
  
    border: none;
    outline: none;
    padding: 8px 20px; /* Buton boyutunu küçültmek için padding'i azaltın */
    background: #ff5945;
    color: #fff;
    font-size: 14px; /* Font boyutunu biraz küçültün */
    cursor: pointer;
    border-radius: 15px; /* Daha yuvarlak köşeler için border-radius'u artırın */
    transition: background 0.3s ease; /* Hover efektini yumuşak hale getirin */
    height: 30px;
    font-family: "Roboto Flex", sans-serif;


}
.History{
    margin-left: 50px;
    width: 100%;
    height: 500px;
    border-radius: 5px;
    background-color: rgba(204, 31, 161, 0.245);

  margin-right: 20px;
  margin-bottom: 10px; /* Listing Devices başlığını bir miktar aşağı kaydır */
  color: white;
  font-family: "Roboto Flex", sans-serif;

  

  


  
}

.up-port{
    width: 100%;
    height: 300px;
    display: flex;
}
.label1{
    width: 100%;
    height: 200px;
    border-radius: 5px;
    background-color: rgba(204, 31, 161, 0.522);

    
    gap: 20px;
    font-size: 12px;
    font-family: "Roboto Flex", sans-serif;


}
.table-texts{
    display: flex;
    gap: 20px;
    font-family: "Roboto Flex", sans-serif;

}
.Problem{
    display: flex;
    gap: 20px;
    cursor: pointer;
    font-family: "Roboto Flex", sans-serif;

}

.clear{
    border: none;
    outline: none;
    padding: 16px 40px;
    background: #ff5945;
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    border-radius: 40px;
    height: 40px;
    font-family: "Roboto Flex", sans-serif;
    
    

}

.delete{
    border: none;
    outline: none;
    padding: 16px 40px;
    background: #ff5945;
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    border-radius: 40px;
    height: 40px;
    font-family: "Roboto Flex", sans-serif;
    


}
.selected {
  background-color: rgba(65, 133, 65, 0.907);
}
.modal {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-content {
  background-color: black;
  color: white;
  padding: 20px;
  border-radius: 10px;
  width: 400px;
  max-height: 90%;
  overflow-y: auto;
  font-family: "Roboto Flex", sans-serif;

}

.close-btn {
  border: none;
  outline: none;
  background: red;
  color: white;
  padding: 10px;
  cursor: pointer;
  border-radius: 5px;
  margin-bottom: 10px;
  margin-left: 300px;
  font-family: "Roboto Flex", sans-serif;

}
.menu1 {
  margin-left: 35%;
  border-radius: 10px;
  background-color: black;
  color: white;
  font-family: sans-serif;
  font-size: 14px;
  overflow-x: hidden;
  font-family: "Roboto Flex", sans-serif;

}


.Order{
    margin-left: 50px;
    width: 100%;
    height: 500px;
    border-radius: 5px;
    background-color: rgba(31, 192, 204, 0.245);

  margin-right: 20px;
  margin-bottom: 10px; /* Listing Devices başlığını bir miktar aşağı kaydır */
  color: white;
  font-family: "Roboto Flex", sans-serif;

  

  

}
.menu-components{
  display: flex;
  gap: 30px;
  font-family: "Roboto Flex", sans-serif;
  margin-top: 5%;

}
.down-order{
  margin-top: 100px;
  display: flex;
}
.label1{
  width: 50%;
}
.btndelete1{
  border: none;
  border: none;
    outline: none;
    padding: 16px 40px;
    background: #ff5945;
    color: #fff;
    font-size: 20px;
    cursor: pointer;
    border-radius: 40px;
    height: 40px;
    font-family: "Roboto Flex", sans-serif;
    margin-top: 5%;
    margin-left: 10%;


}
.buttons{
  margin-left: 10%;
  margin-top: 5%;
  display: flex;
  gap: 50px;
}


</style>